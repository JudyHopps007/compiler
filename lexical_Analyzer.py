input_code = '#include <stdio.h> \nint main() { \nprintf("Hello, World!"); \nreturn 0;'
import re


# Define regular expression patterns for different types of tokens
patterns = [
    (r'\b(int|char|void|bool|if|else|while|for)\b', 'KEYWORD'),
    (r'\b(true|false)\b', 'BOOLEAN'),
    (r'\b([0-9]+)\b', 'NUMBER'),
    (r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', 'IDENTIFIER'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'MULTIPLY'),
    (r'/', 'DIVIDE'),
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
    #(r'&&', 'AND'),
    #(r'||', '0R'),
    #(r'!', 'NOT'),
    (r'//.*$|/\*.*?\*/', 'COMMENT')
]

# Define a function that reads a program from a text file and generates a list of tokens
def lex(filename):
    with open(filename, 'r') as f:
        program = f.read()
    tokens = []
    position = 0
    while position < len(program):
        match = None
        for pattern, token_type in patterns:
            regex = re.compile(pattern)
            match = regex.match(program, position)

            if match:
                tokens.append((token_type, match.group(0)))
                position = match.end(0)
                break

        if not match:
            print("Illegal character: " + program[position])
            position += 1

    return tokens

# Example usage
tokens = lex('program.c')
print(tokens)