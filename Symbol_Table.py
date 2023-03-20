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
    ('<program>', ['<include-list>',  '<declaration>']),
    ('<include-list>', ['INCLUDE_DIRECTIVE']),
    ('<declaration>', ['<function_declaration>']),
    ('<function_declaration>', ['<type_specifier>', '<identifier>', 'LEFT_PAREN', '<parameter_list>', 'RIGHT_PAREN', '<compound_statement>']),
    ('<type_specifier>', ['KEYWORD']),
    ('<identifier>', ['IDENTIFIER']),
    ('<parameter_list>', ['<statement>', 'COMMA', '<statement>']),
    ('<statement>', ['<type_specifier>', 'IDENTIFIER']),
    ('<compound_statement>', ['LEFT_BRACE', '<type_specifier>', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'PLUS', 'IDENTIFIER', 'SEMICOLON', 'KEYWORD', 'IDENTIFIER', 'SEMICOLON', 'RIGHT_BRACE']),
]




# Define a function that recursively generates a parse tree from the token stream using the production rules
def parse(tokens, rule):
    node = ParseTreeNode(rule[0])
    print(rule[0])
    for production in rule[1]:
        if production.startswith('<'):
            # If the production is a non-terminal, recursively generate a subtree using the corresponding rule
            matching_rules = [r for r in rules if r[0] == production]
            if not matching_rules:
                raise ValueError("Invalid production rule: " + production)
            subrule = None
            for r in matching_rules:
                try:
                    subrule = parse(tokens[:], r)  # Pass a copy of the token list to avoid consuming tokens prematurely
                    break
                except ValueError:
                    pass
            if not subrule:
                raise ValueError("No valid subrule found for production rule: " + production)
            node.add_child(subrule)
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
