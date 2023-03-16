import re

symbol_table = {}


# Define regular expression patterns for different types of tokens(assigning tokens to lexemes)
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

# Define a function that reads a program from a text file and generates a list of tokens
def lex(filename):
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

        for pattern, token_type in patterns:
            regex = re.compile(pattern)
            match = regex.match(program, position)

            # get rid of code comments
            if match:
                if token_type != 'COMMENT': # the tokenization logic skips over comment tokens
                    tokens.append((token_type, match.group(0)))
                position = match.end(0)
                break

        if not match:
            print("Illegal character: " + program[position])
            position += 1

    return tokens

# Example usage
tokens = lex('program.c')
print("tokens: \n", tokens )



# ================================================================================
# Define a function to parse a list of tokens and check for syntax errors
def parse(tokens):
    position = 0
    # Helper function to parse an expression
    def parse_expression():
        nonlocal position
        token_type, lexeme = tokens[position]

        # An expression can be a number, identifier, or a parenthesized expression
        if token_type == 'NUMBER' or token_type == 'IDENTIFIER':
            position += 1
            return True
        elif token_type == 'LEFT_PAREN':
            position += 1
            if parse_expression():
                token_type, lexeme = tokens[position]
                if token_type == 'RIGHT_PAREN':
                    position += 1
                    return True
                else:
                    print('Error: expected )')
                    return False
            else:
                return False
        else:
            print(f'Error: expected number, identifier, or (, but got {lexeme}')
            return False

    # Parse statements one by one
    while position < len(tokens):
        token_type, lexeme = tokens[position]

        if token_type == 'KEYWORD':
            if lexeme == 'if':
                # Parse if statement
                position += 1
                if not parse_expression():
                    return False
                if parse(tokens[position:]) and len(tokens) > position and tokens[position][1] == 'else':
                    position += 1
                    if parse(tokens[position:]):
                        return True
                    else:
                        return False
                else:
                    return True
            elif lexeme == 'while':
                # Parse while loop
                position += 1
                if not parse_expression():
                    return False
                if parse(tokens[position:]):
                    return True
                else:
                    return False
            elif lexeme == 'for':
                # Parse for loop
                position += 1
                if not parse_expression():
                    return False
                if len(tokens) > position + 2 and tokens[position + 1][1] == ',' and parse_expression():
                    if len(tokens) > position and tokens[position][1] == ')':
                        position += 1
                        if parse(tokens[position:]):
                            return True
                        else:
                            return False
                    else:
                        print('Error: expected )')
                        return False
                else:
                    print('Error: expected ,')
                    return False
            else:
                print(f'Error: unknown keyword {lexeme}')
                return False
        elif token_type == 'LEFT_BRACE':
            # Parse a block of statements
            position += 1
            while position < len(tokens) and tokens[position][1] != '}':
                if not parse(tokens[position:]):
                    return False
            if position < len(tokens) and tokens[position][1] == '}':
                position += 1
                return True
            else:
                print('Error: expected }')
                return False
        elif token_type == 'SEMICOLON':
            # Empty statement, skip over it
            position += 1
        else:
            print(f'Error: unexpected token {lexeme}')
            return False
    return True


if parse(tokens):
    print('Syntax analysis succeeded')
else:
    print('Syntax analysis failed')