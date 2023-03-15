import re

# Define regular expression patterns for different types of tokens
patterns = [
    (r'#include\s+<.*?>', 'INCLUDE_DIRECTIVE'),
    (r'\b(int|char|void|bool|if|else|while|for|continue|break|for|return|float|long)\b', 'KEYWORD'),
    (r'\b(true|false)\b', 'BOOLEAN'),
    (r'\b([0-9]+)\b', 'NUMBER'),
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
    (r',', 'COMMA')
]

# Define a function that reads a program from a text file and generates a list of tokens and a symbol table
def lex(filename):
    with open(filename, 'r') as f:
        program = f.read()

    tokens = []
    symbol_table = {}
    position = 0

    while position < len(program):
        match = None

        # Skip over whitespace and comments
        if re.match(r'\s', program[position]):
            position += 1
            continue
        if re.match(r'//', program[position:]):
            position = program.index('\n', position)
            continue

        # Try to match a pattern for each token type
        for pattern, token_type in patterns:
            regex = re.compile(pattern)
            match = regex.match(program, position)

            if match:
                lexeme = match.group(0)
                if token_type != 'COMMENT':
                    tokens.append((token_type, lexeme))
                    if token_type == 'IDENTIFIER' and lexeme not in symbol_table:
                        symbol_table[lexeme] = len(symbol_table) + 1
                position += len(lexeme)
                break

        if not match:
            print("Illegal character: " + program[position])
            position += 1

    return tokens, symbol_table

# Example usage
tokens, symbol_table = lex('program.txt')
print(tokens)
print(symbol_table)