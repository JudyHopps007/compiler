import re  # for generate regular expression
import time  # for measuring 'p' run time
import json  # for symbol table {access and storage}

# ====================================== LEXICAL ANALYZER PHASE =====================================================
# ===================================================================================================================

# Define regular expression patterns for different types of tokens(assigning tokens to lexemes)
patterns_rg = [
    #(r'#include', 'INCLUDE_ID'),
    #(r'<[A-Za-z]+.h>', 'INCLUDE_DIRECTIVE'),
    (r'#include <[A-Za-z]+.h>', 'PREPROCESSOR_DIRECTIVE'),
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

print("\n============== TOKENS ================ \n ", tokens)
for token in tokens:  # print each token at a time
    print(token)

def parse(tokens):

    # Create a stack to store the parsed tokens
    stack = []

    # Iterate over the tokens
    for token in tokens:
        # If the token is a keyword or an identifier, push it onto the stack
        if token[0] in ["KEYWORD", "IDENTIFIER"]:
            stack.append(token)

        # If the token is an operator, pop two tokens off the stack and push the result of the operation onto the stack
        elif token[0] in ["PLUS", "MINUS", "MULTIPLY", "DIVIDE", "EQUAL", "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", "LESS_THAN_EQUAL", "GREATER_THAN_EQUAL"]:
            right_operand = stack.pop()
            left_operand = stack.pop()
            result = eval(left_operand[1] + token[1] + right_operand[1])
            stack.append((token[0], result))

        # If the token is a left parenthesis, push it onto the stack
        elif token[0] == "LEFT_PAREN":
            stack.append(token)

        # If the token is a right parenthesis, pop the top two tokens off the stack and push the result of the expression onto the stack
        elif token[0] == "RIGHT_PAREN":
            if len(stack) == 0:
                raise SyntaxError("Unbalanced parentheses")
            right_operand = stack.pop()
            left_operand = stack.pop()
            print("we ", right_operand)
            print("we ",left_operand)
            #result = eval(left_operand[1] + token[1] + right_operand[1])
            #stack.append((token[0], result))

        # If the token is a semicolon, pop the top token off the stack
        elif token[0] == "SEMICOLON":
            stack.pop()

        # If the token is a keyword that indicates the beginning of a statement, pop the top token off the stack and push the result of the statement onto the stack
        elif token[0] in ["IF", "ELSE", "WHILE", "RETURN"]:
            statement = stack.pop()
            stack.append((token[0], statement))

        # If the token is a keyword that indicates the beginning of a declaration, pop the top token off the stack and push the result of the declaration onto the stack
        elif token[0] in ["INT", "FLOAT", "CHAR", "VOID"]:
            declaration = stack.pop()
            stack.append((token[0], declaration))

        # If the token is a keyword that indicates the beginning of a type, pop the top token off the stack and push the result of the type onto the stack
        elif token[0] in ["STRUCT", "UNION"]:
            type = stack.pop()
            stack.append((token[0], type))

        # If the token is an identifier that indicates the beginning of a variable, pop the top token off the stack and push the result of the variable onto the stack
        elif token[0] == "IDENTIFIER" and token[1].isalpha():
            variable = stack.pop()
            stack.append((token[0], variable))

        # If the token is an identifier that indicates the beginning of a function, pop the top token off the stack and push the result of the function onto the stack
        elif token[0] == "IDENTIFIER" and token[1].isalpha() and token[1].isupper():
            function = stack.pop()
            stack.append((token[0], function))

        # If the token is a preprocessor directive, push it onto the stack
        elif token[0] == "PREPROCESSOR_DIRECTIVE":
            stack.append(token)

        # If the token is anything else, raise an error
        else:
            raise ValueError("Unexpected token: " + token[1])

    # If the stack is not empty, there is a syntax error
    if len(stack) > 0:
        raise SyntaxError("Syntax error: Unbalanced parentheses")

    # Return the top token on the stack, which is the result of the parse
    return stack[-1]

parse(tokens)