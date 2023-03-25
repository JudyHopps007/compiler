import lexical_Analyzer

tokens = lexical_Analyzer.lex('program.c')

# Define a class to represent a node in the parse tree
class ParseTreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def add_child(self, child):
        self.children.append(child)


# Define the production rules for the language
# This is a simplified set of rules for illustration purposes only
rules = [
    ('<program>', ['<include-list>',  '<declaration>']),
    ('<include-list>', ['INCLUDE_DIRECTIVE']),

    ('<declaration>', ['<function_declaration>*']),
    ('<declaration>', []),


    ('<function_declaration>', ['<type_specifier>', '<identifier>', '<parameter_list>',  '<compound_statement>']),

    #('<function_declaration_closure>', ['<type_specifier>', '<identifier>', '<parameter_list>',  '<compound_statement>']),

    ('<parameter_list>', ['LEFT_PAREN', '<type_specifier>', '<identifier>', 'RIGHT_PAREN']),
    ('<more_parameters>', ['COMMA', '<type_specifier>', '<identifier>', '<more_parameters>']),
    ('<more_parameters>', []),

    ('<type_specifier>', ['KEYWORD']),
    ('<identifier>', ['IDENTIFIER']),
    ('<identifier>', ['main_f']),

    ('<comma>', ['COMMA']),
    ('<compound_statement>', ['LEFT_BRACE', 'RIGHT_BRACE']),


]






# ('<function_declaration>', ['<type_specifier>', '<identifier>', 'LEFT_PAREN', 'RIGHT_PAREN', '<compound_statement>']),

# Define a function that recursively generates a parse tree from the token stream using the production rules
def lex(filename):
    with open(filename, 'r') as f:
        program = f.read()
    tokens = []
    position = 0
    while position < len(program):
        best_match = None
        best_pattern = None
        best_token_type = None
        best_probability = 0.0

        # Skip over empty lines
        if program[position] == '\n':
            position += 1
            continue

        # Skip over whitespace
        if re.match(r'\s', program[position]):
            position += 1
            continue

        for pattern, token_type, probability in patterns:
            regex = re.compile(pattern)
            match = regex.fullmatch(program[position:])

            # get rid of code comments
            if match:
                if token_type != 'COMMENT': # the tokenization logic skips over comment tokens
                    if probability > best_probability:
                        best_match = match.group(0)
                        best_pattern = pattern
                        best_token_type = token_type
                        best_probability = probability
                position += len(match.group(0))
                break

        if not best_match:
            print("Illegal character: " + program[position])
            position += 1
        else:
            tokens.append((best_token_type, best_match))

    return tokens



# Define a function that runs the syntax analyzer on the token stream
def syntax_analyze(tokens):
    tree = parse(tokens, rules[0])
    if tokens:
        raise ValueError("Unexpected tokens at end of input")
    return tree


print('\nTOKENS\n\t', tokens)
tree = syntax_analyze(tokens)
print("tree", tree)
