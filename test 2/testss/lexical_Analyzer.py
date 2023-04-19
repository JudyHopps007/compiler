import re  # for generate regular expression
import time  # for measuring 'p' run time
import json  # for symbol table {access and storage}

# ====================================== LEXICAL ANALYZER PHASE =====================================================
# ===================================================================================================================

# Define regular expression patterns for different types of tokens(assigning tokens to lexemes)

patterns_rg = [
    (r'#include', 'INCLUDE_ID'),
    (r'<[A-Za-z]+.h>', 'INCLUDE_DIRECTIVE'),
    (r'\b(int|void|char|bool|float|long|return)\b', 'KEYWORD'),
    (r'\b(if)\b', 'IF'),
    (r'\b(else)\b', 'ELSE'),
    (r'\b(while)\b', 'WHILE'),
    (r'\b(true|false)\b', 'BOOLEAN'),
    (r'[0-9]+[.][0-9]+', 'FLOATING_POINT'),
    (r'\b[0-9]+\b', 'INTEGER'),
    (r"'.'", 'CHAR'),
    (r"[\"][^']*[\"]", 'STRING'),
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
                    token_list.append((token_type, match.group(0)))  # adding found token in the token_list
                curser_position = match.end(0)
                break

        if not match:  # catch errors or illegal charachers that don't conform to the defined regular expressions
            print("Illegal character: " + program[curser_position], "at Line ", line_number_track)
            curser_position += 1 # incrementing cursor position
    return token_list


start_run_time_time = time.time()  # Record the Start run time-time of lexical_analyzer
tokens = lexical_analyzer('program.c')  # calling the lexical_analyzer()
End_run_time_time = time.time()  # Record the End run time-time of lexical_analyzer
Program_Run_time = End_run_time_time - start_run_time_time  # Calculate the elapsed time (run time of lexical_analyzer function)
print(f"\nProgram Runtime  :  {Program_Run_time} seconds")

