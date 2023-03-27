import re  # generate regular expression
import time  # measure the run time
import json
# ===================================================================== LEXICAL ANALYZER PHASE ==============================================================================================
# ===========================================================================================================================================================================================

# Define regular expression patterns for different types of tokens(assigning tokens to lexemes)
patterns_rg = [
    (r'#include\s+<.*?>', 'INCLUDE_DIRECTIVE'),
    (r'\b(int|void|char|bool|float|long|return)\b', 'KEYWORD'),
    (r'\b(if)\b', 'if'),
    (r'\b(if)\b', 'else'),
    (r'\b(if)\b', 'while'),
    (r'\b(true|false|1|0)\b', 'BOOLEAN'),
    (r'\b\d+\.\d+\b', 'floating_point'),
    (r'\b\d+\b', 'integer'),
    (r"'.'", 'char'),
    (r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', 'IDENTIFIER'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'MULTIPLY'),
    (r'(\/\/[^\n\r]*[\n\r])|\/\*[\s\S]*?\*\/', 'COMMENT'),
    (r'/(?![\/\*])[\n\s]*', 'DIVIDE'),
    (r'%', 'MODULUS'),
    (r'=', 'ASSIGN'),
    (r'==', 'EQUAL'),
    (r'!=', 'NOT_EQUAL'),
    (r'<', 'LESS_THAN'),
    (r'>', 'GREATER_THAN'),
    (r'<=', 'LESS_THAN_EQUAL'),
    (r'>=', 'GREATER_THAN_EQUAL'),
    (r'\(', 'LEFT_PAREN'),
    (r'\)', 'RIGHT_PAREN'),
    (r'\{', 'LEFT_BRACE'),
    (r'\}', 'RIGHT_BRACE'),
    (r';', 'SEMICOLON'),
    (r',', 'COMMA'),
    (r'\|\|', 'OR'),
    (r'\&\&', 'AND'),
    (r'\!', 'NOT'),
]


# ================================================ Define a function that reads a program from a  and generates a list of tokens ===============================================================================================
def lexical_analyzer(filename):
    with open(filename, 'r') as f:
        program = f.read()
    tokens = []
    position = 0
    while position < len(program):
        match = None
        # Skip over empty lines
        if program[position] == '\n':
            position += 1
            continue
        # Skip over whitespace
        if re.match(r'\s', program[position]):
            position += 1
            continue
        for pattern, token_type in patterns_rg:
            regex = re.compile(pattern)
            match = regex.match(program, position)
            # get rid of code comments
            if match:
                if token_type != 'COMMENT':  # the tokenization logic skips over comment tokens
                    tokens.append((token_type, match.group(0)))
                position = match.end(0)
                break
        if not match:
            print("Illegal character: " + program[position])
            position += 1
    return tokens


start_run_time_time = time.time()  # Record the Start run time-time of lexical_analyzer
tokens = lexical_analyzer('program.c')
End_run_time_time = time.time()  # Record the End run time-time of lexical_analyzer
Program_Run_time = End_run_time_time - start_run_time_time  # Calculate the elapsed time
print(f"\nProgram Runtime  :  {Program_Run_time} seconds")

print("\nTOKENS \n\t", tokens)


# ==============================================================================SYMBOL TABLE PHASE================================================================================================================================
# ================================================================================================================================================================================================================================
def generate_symbol_table(tokens):
    symbol_table = {}

    for token_type, value in tokens:
        if token_type == 'IDENTIFIER':
            if value not in symbol_table:
                symbol_table[value] = {
                    'type': None,
                    'value': None,
                    'line_number': None
                }

    return symbol_table


symbol_table = generate_symbol_table(tokens)


# print("\nSYMBOL_TABLE \n\t", symbol_table)
# =======================================================================================================================


with open('test.json') as json_file:
    data = json.load(json_file)

symbol_table = data['Symbol_table']
def generate_symbol_table(tokens):

    current_scope = []
    current_type = None
    directives_table = []
    for i in range(len(tokens)):
        token_type, token_value = tokens[i]
        print('=============', token_type, token_value)
        if token_type == 'INCLUDE_DIRECTIVE':
            directives_table.append(token_value)
        if token_type == 'IDENTIFIER':
            for k in range(len(symbol_table)):
                if data['Symbol_table'][k]['IDENTIFIER'] == token_value:
                    print('found')
                    if data['Symbol_table'][k]['DATA_TYPE'] == None:

                        print('data type null',  tokens[i-1][1])
                        data_type = tokens[i+1]
                    break

    return directives_table


table = generate_symbol_table(tokens)

print(table)
