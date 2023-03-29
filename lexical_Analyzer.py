import re  # for generate regular expression
import time  # for measure the run time
import json  # for symbol table

# ===================================================================== LEXICAL ANALYZER PHASE ==============================================================================================
# ===========================================================================================================================================================================================

# Define regular expression patterns for different types of tokens(assigning tokens to lexemes)
# (r"['][a-zA-Z0-9_?]*[\s]*[']", 'STRING'),
patterns_rg = [
    (r'#include', 'INCLUDE_ID'),
    (r'<[A-Za-z]+.h>', 'INCLUDE_DIRECTIVE'),
    (r'\b(int|void|char|bool|float|long|return)\b', 'KEYWORD'),
    (r'\b(if)\b', 'if'),
    (r'\b(else)\b', 'else'),
    (r'\b(while)\b', 'while'),
    (r'\b(true|false)\b', 'BOOLEAN'),
    (r'[0-9]+[.][0-9]+', 'floating_point'),
    (r'\b[0-9]+\b', 'integer'),
    (r"'.'", 'char'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
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


# ========= Define a function that reads a program from a  and generates a list of tokens ===
def lexical_analyzer(filename):

    with open(filename, 'r') as f:  # load the program file into the lexical analyzer
        program = f.read()

    line_number_track = 1  # keep track of position
    token_list = []  # initialized to empty list
    curser_position = 0  # initialized to zero
    while curser_position < len(program):
        match = None

        if program[curser_position] == '\n':  # Skip over empty lines
            line_number_track += 1  # incrementing line number
            curser_position += 1  # incrementing cursor position
            continue

        if re.match(r'\s', program[curser_position]):  # Skip over whitespace
            curser_position += 1
            continue

        for pattern, token_type in patterns_rg:
            regex = re.compile(pattern)
            match = regex.match(program, curser_position)
            # get rid of code comments logic skips over comment token_list
            if match:
                if token_type != 'COMMENT':
                    token_list.append((token_type, match.group(0))) # adding found token in the token_list
                curser_position = match.end(0)
                break

        if not match:  # catch errors or illegal charachers that don't conform to the defined regular expressions
            print("Illegal character: " + program[curser_position], "Line : ", line_number_track)
            curser_position += 1
    return token_list


start_run_time_time = time.time()  # Record the Start run time-time of lexical_analyzer
tokens = lexical_analyzer('program.c')  # calling the lexical_analyzer()
End_run_time_time = time.time()  # Record the End run time-time of lexical_analyzer
Program_Run_time = End_run_time_time - start_run_time_time  # Calculate the elapsed time (run time of lexical_analyzer function)
print(f"\nProgram Runtime  :  {Program_Run_time} seconds")

print("\n============== TOKENS ================ \n")
for token in tokens:  # print each token at a time
    print(token)


# ============================================================================== SYMBOL TABLE PHASE====================================================================================
# =====================================================================================================================================================================================

def generate_symbol_table(tokens):
    clear_json = {"Symbol_table": []}
    with open("symbol_table.json", 'w') as f:
        json.dump(clear_json, f)

    with open('symbol_table.json') as json_file:
        data = json.load(json_file)
    symbol_table = data['Symbol_table']
    directives_table = []
    for i in range(len(tokens)):
        token_type, token_value = tokens[i]
        if token_type == 'INCLUDE_DIRECTIVE':
            directives_table.append(token_value)
        if token_type == 'IDENTIFIER':
            data_type = None
            value = None
            if any(d.get('IDENTIFIER') == token_value for d in symbol_table):
                # print("found ", token_value)
                for k in range(len(symbol_table)):
                    if symbol_table[k]['IDENTIFIER'] == token_value:
                        if symbol_table[k]['DATA_TYPE'] == None:
                            if tokens[i - 1][0] == 'KEYWORD':
                                data_type = tokens[i - 1][1]

                        if tokens[i + 1][1] != '(':
                            if tokens[i + 1][1] != ',':
                                if tokens[i + 1][1] == '=':
                                    if symbol_table[k]['VALUE'] == None:
                                        p = 0
                                        value = ''
                                        while tokens[i + 2 + p][1] != ';':
                                            value += tokens[i + 2 + p][1]
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
                'SCOPE': None
            }
            symbol_table.append(dictionary)
            with open('symbol_table.json', 'w') as json_file_write:
                json.dump(data, json_file_write, indent=4)


generate_symbol_table(tokens)
