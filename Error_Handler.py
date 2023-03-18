import re
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
        ('<statement>', ['<type_specifier>', 'IDENTIFIER', 'ASSIGN', 'integer', 'SEMICOLON']),
        ('<type_specifier>',  ['']),
        ('<type_specifier>', ['void_kw']),



]

"""
    ('<function_declaration>', ['<type_specifier>', '<identifier>', 'LEFT_PAREN', 'parameter_list', 'RIGHT_PAREN', '<block>']),
    ('<parameter>', ['<type_specifier>', '<identifier>']),
    ('<block>', ['SEMICOLON', '<statement_list>', 'SEMICOLON']),
    ('<identifier>', ['IDENTIFIER']),
    
    ('<expression>', ['integer'])
('<statement>', ['<if_statement>']),
('<statement>', ['<while_statement>']),
('<statement>', ['<expression_statement>']),
('<if_statement>', ['if', 'LEFT_PAREN', '<identifier>', 'RIGHT_PAREN', 'LEFT_BRACE', 'RIGHT_BRACE']),
('<while_statement>', ['while', 'LEFT_PAREN', '<expression>', 'RIGHT_PAREN', '<statement>']),
('<expression_statement>', ['<expression>', ';']),
('<expression>', ['<identifier>', 'ASSIGN', '<expression>']),
('<expression>', ['<simple_expression>']),

('<simple_expression>', ['<term>', '<additive_operator>', '<term>']),
('<term>', ['<factor>', '<multiplicative_operator>', '<factor>']),
('<factor>', ['<identifier>']),
('<factor>', ['<number>']),
('<identifier>', ['IDENTIFIER']),
('<number>', ['NUMBER']),
('<additive_operator>', ['+', '-']),
('<multiplicative_operator>', ['*', '/'])
"""


# Define a function that recursively generates a parse tree from the token stream using the production rules
def parse(tokens, rule):
    node = ParseTreeNode(rule[0])
    print(rule[0])
    for production in rule[1]:
        if production.startswith('<'):
            # If the production is a non-terminal, recursively generate a subtree using the corresponding rule
            subrule = next((r for r in rules if r[0] == production), None)
            if not subrule:
                raise ValueError("Invalid production rule: " + production)
            child = parse(tokens, subrule)
            node.add_child(child)
        else:
            # If the production is a terminal, consume a token from the token stream and match it against the production
            if not tokens:
                raise ValueError("Unexpected end of input")
            token = tokens.pop(0)
            if token[0] != production:
                raise ValueError(f"Expected token type {production}, got {token[0]}: {token[1]}")
            node.add_child(ParseTreeNode(token))

    return node

# Define a function that runs the syntax analyzer on the token stream
def syntax_analyze(tokens):
    tree = parse(tokens, rules[0])
    if tokens:
        raise ValueError("Unexpected tokens at end of input")
    return tree

# Example usage
import lexical_Analyzer

tokens = lexical_Analyzer.lex('program.c')
print(tokens)
tree = syntax_analyze(tokens)
print("tree", tree.value)
