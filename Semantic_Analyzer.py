import lexical_Analyzer

#tokens = lexical_Analyzer.lex('program.c')

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
    ('<program>', ['<include-list>', '<declaration>']),
    ('<include-list>', ['INCLUDE_DIRECTIVE']),
]


def parse(tokens, table):
    stack = ['<program>']
    root = ParseTreeNode('<program>')
    current_node = root
    lookahead = tokens[0] if tokens else None

    while stack:
        current_symbol = stack[-1]
        if current_symbol.startswith('<'):
            # If the current symbol is a non-terminal, get the corresponding production from the table
            production = table[current_symbol].get(lookahead)
            if production is None:
                raise ValueError(f"No production found for {current_symbol} and lookahead {lookahead}")
            current_node.add_child(ParseTreeNode(production))
            stack.pop()
            for symbol in reversed(production[1]):
                stack.append(symbol)
            current_node = current_node.children[-1]
        else:
            # If the current symbol is a terminal, match it with the lookahead token
            if not tokens:
                raise ValueError("Unexpected end of input")
            token = tokens.pop(0)
            if current_symbol != token[0]:
                raise ValueError(f"Expected {current_symbol}, got {token[0]}: {token[1]}")
            current_node.add_child(ParseTreeNode(token))
            stack.pop()
        lookahead = tokens[0] if tokens else None

    return root

tokens = [
    ('INCLUDE_DIRECTIVE', '#include'),
    ('IDENTIFIER', 'stdio.h'),
    ('SEMICOLON', ';'),
    ('INT', 'int'),
    ('IDENTIFIER', 'main'),
    ('LPAREN', '('),
    ('RPAREN', ')'),
    ('LBRACE', '{'), ('RETURN', 'return'),
    ('NUMBER', '0'),
    ('SEMICOLON', ';'),
    ('RBRACE', '}')
]
table = {
    '<program>': {'INCLUDE_DIRECTIVE': ('<include-list>', '<declaration>')},
    '<include-list>': {'INCLUDE_DIRECTIVE': ('INCLUDE_DIRECTIVE',)}
}

root = parse(tokens, table)
