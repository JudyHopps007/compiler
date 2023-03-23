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
parsing_table = {
    '<start>': {
        'if': [('if_statement',)],
        'while': [('while_statement',)],
        'identifier': [('assignment_statement',)],
        'print': [('print_statement',)],
    },
    'if_statement': {
        'if': [('<', 'expression', '>', 'then', 'statement')],
    },
    'while_statement': {
        'while': [('<', 'expression', '>', 'do', 'statement')],
    },
    'assignment_statement': {
        'identifier': [('identifier', '=', 'expression')],
    },
    'print_statement': {
        'print': [('print', 'expression')],
    },
    'expression': {
        'identifier': [('identifier',)],
        'number': [('number',)],
    },
}



# ('<function_declaration>', ['<type_specifier>', '<identifier>', 'LEFT_PAREN', 'RIGHT_PAREN', '<compound_statement>']),

# Define a function that recursively generates a parse tree from the token stream using the production rules
def parse(tokens, parsing_table):
    stack = ['<start>']
    i = 0
    while stack:
        symbol = stack.pop()
        if symbol.startswith('<'):
            rule = parsing_table[symbol][tokens[i][0]]
            if not rule:
                raise ValueError(f"Unexpected token: {tokens[i][1]}")
            for s in reversed(rule[1]):
                stack.append(s)
        else:
            if symbol != tokens[i][0]:
                raise ValueError(f"Expected token {symbol}, but got {tokens[i][0]}")
            i += 1
    return True

# Define a function that runs the syntax analyzer on the token stream



parse(tokens, parsing_table)
