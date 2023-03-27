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
with open('test.json') as json_file:
    data = json.load(json_file)

symbol_table = data['Symbol_table']
def generate_symbol_table(tokens):

    directives_table = []
    for i in range(len(tokens)):
        token_type, token_value = tokens[i]
        #print('=============', token_type, token_value)
        if token_type == 'INCLUDE_DIRECTIVE':
            directives_table.append(token_value)
        if token_type == 'IDENTIFIER':
            data_type = None
            value = None
            if any(d.get('IDENTIFIER') == token_value for d in data['Symbol_table']):
                print("found ", token_value)
                for k in range(len(symbol_table)):
                    if data['Symbol_table'][k]['IDENTIFIER'] == token_value:
                        #print('found')
                        if data['Symbol_table'][k]['DATA_TYPE'] == None:
                            if tokens[i - 1][0] == 'KEYWORD':
                                data_type = tokens[i - 1][1]

                        if tokens[i+1][1] != '(':
                            if tokens[i+1][1] != ',':
                                if tokens[i + 1][1] == '=':
                                  if data['Symbol_table'][k]['VALUE'] == None:
                                      p = 0
                                      value = ''
                                      while tokens[i+2 + p][1] != ';':
                                        value += tokens[i+2+ p][1]
                                        p += 1
                        else:
                            value = None

            else:
                    if tokens[i - 1][0] == 'KEYWORD':
                        data_type = tokens[i - 1][1]
                    if tokens[i + 1][1] != '(':
                        if tokens[i + 1][1] != ',':
                            if tokens[i + 1][1] == '=':
                                p = 0
                                value = ''
                                while tokens[i + 2 + p][1] != ';':
                                    value += tokens[i + 2 + p][1]

                                    p += 1
            dictionary = {
                'IDENTIFIER': token_value,
                'DATA_TYPE': data_type,
                'VALUE': value,
                'SCOPE': 'dguest_room_type'
            }
            symbol_table.append(dictionary)
            with open('test.json', 'w') as json_file_write:
                json.dump(data,json_file_write, indent=4)

    return directives_table


table = generate_symbol_table(tokens)

print(table)
