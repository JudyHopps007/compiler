import lexical_Analyzer

tokens = lexical_Analyzer.lex('program.c')


class ParseTreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def add_child(self, child):
        self.children.append(child)


def parse(tokens, parsing_table):
    stack = ['$', parsing_table['<start>'][0]]
    root = ParseTreeNode('<start>')
    curr_node = root

    while stack:
        top = stack[-1]
        token = tokens[0][0] if tokens else '$'
        if top in parsing_table and token in parsing_table[top]:
            stack.pop()
            for prod in reversed(parsing_table[top][token]):
                curr_node.add_child(ParseTreeNode(prod))
                if prod.startswith('<'):
                    new_node = ParseTreeNode(prod)
                    curr_node = new_node
                    stack.append(prod)
        elif top == token:
            stack.pop()
            if token != '$':
                curr_node.add_child(ParseTreeNode(tokens.pop(0)))
                curr_node = curr_node.parent
        else:
            raise ValueError(f"Unexpected token: {token}")

    return root



# Define the production rules for the language
# This is a simplified set of rules for illustration purposes only
parsing_table = {
    '<start>': {
        'int': ['<expr>'],
        'float': ['<expr>'],
        '(': ['<expr>'],
        'id': ['<expr>'],
    },
    '<expr>': {
        'int': ['<term>', '<expr_>'],
        'float': ['<term>', '<expr_>'],
        '(': ['<term>', '<expr_>'],
        'id': ['<term>', '<expr_>'],
    },
    '<expr_>': {
        '+': ['+', '<term>', '<expr_>'],
        ')': [],
        '$': [],
    },
    '<term>': {
        'int': ['<factor>', '<term_>'],
        'float': ['<factor>', '<term_>'],
        '(': ['<factor>', '<term_>'],
        'id': ['<factor>', '<term_>'],
    },
    '<term_>': {
        '*': ['*', '<factor>', '<term_>'],
        '+': [],
        ')': [],
        '$': [],
    },
    '<factor>': {
        'int': ['int'],
        'float': ['float'],
        '(': ['(', '<expr>', ')'],
        'id': ['id'],
    },
}



parse(tokens, parsing_table)
