import lexical_Analyzer

tokens = lexical_Analyzer.lex('program.c')

# Define the production rules for the language
# This is just an example, you'll need to define your own rules for your specific language
# Each rule is represented as a tuple where the first element is the name of the nonterminal symbol
# and the remaining elements are the symbols in the production
rules = [
    ('program', 'declaration_list'),
    ('declaration_list', 'declaration'),
    ('declaration_list', 'declaration_list declaration'),
    ('declaration', 'variable_declaration'),
    ('declaration', 'function_declaration'),
    ('variable_declaration', 'type ID ;'),
    ('function_declaration', 'type ID ( parameter_list ) compound_statement'),
    ('parameter_list', 'parameter'),
    ('parameter_list', 'parameter_list , parameter'),
    ('parameter', 'type ID'),
    ('type', 'int'),
    ('type', 'float'),
    ('type', 'bool'),
    ('compound_statement', '{ statement_list }'),
    ('statement_list', 'statement'),
    ('statement_list', 'statement_list statement'),
    ('statement', 'expression_statement'),
    ('statement', 'variable_declaration'),
    ('statement', 'if_statement'),
    ('statement', 'while_statement'),
    ('expression_statement', 'expression ;'),
    ('if_statement', 'if ( expression ) statement'),
    ('if_statement', 'if ( expression ) statement else statement'),
    ('while_statement', 'while ( expression ) statement'),
    ('expression', 'ID = expression'),
    ('expression', 'expression + expression'),
    ('expression', 'expression - expression'),
    ('expression', 'expression * expression'),
    ('expression', 'expression / expression'),
    ('expression', '( expression )'),
    ('expression', 'ID'),
    ('expression', 'NUMBER'),
    ('expression', 'BOOLEAN'),
]

# Define a function to perform syntax analysis on a list of tokens
def parse(tokens):
    tree = []
    position = 0

    # Start with the start symbol of the grammar
    symbol = 'program'

    # Define a function to match a token to a terminal symbol
    def match(token, symbol):
        return token[0] == symbol

    # Define a function to generate a subtree from a production rule
    def generate_subtree(rule, children):
        return (rule[0], children)

    # Define a function to recursively parse a nonterminal symbol
    def parse_nonterminal(symbol):
        nonlocal position
        children = []

        # Try each production rule for the symbol
        for rule in rules:
            if rule[0] == symbol:
                print(12)
                for symbol in rule[1:]:
                    # If the symbol is a nonterminal, recursively parse it
                    if symbol.isupper():
                        subtree = parse_nonterminal(symbol)
                        if subtree:
                            children.append(subtree)
                            continue

                    # If the symbol is a terminal, match it with the current token
                    elif match(tokens[position], symbol):
                        children.append(tokens[position])
                        position += 1
                        continue

                    # If the symbol does not match, backtrack and try the next production rule
                    break

                # If all symbols match, generate a subtree and return it
                else:
                    return generate_subtree(rule, children)

        # If no production rule matches, return None to indicate a syntax error
        return None

    # Start parsing with the start symbol
    tree = parse_nonterminal(symbol)
    print(tree)
    # If the parse was successful, make sure we consumed all the tokens
    if tree and position == len(tokens):
        print('fail')
        return tree


x = parse(tokens)
print(x)
