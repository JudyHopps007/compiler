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
    ('<program>', ['<include-list>', '<declaration>']),
    ('<include-list>', ['INCLUDE_DIRECTIVE']),
]



# First, create the predictive parsing table
parsing_table = {}
for non_terminal, productions in rules:
    for lookahead in set(prod[0] for prod in productions if not prod.startswith('<')):
        parsing_table.setdefault(non_terminal, {})[lookahead] = [prod for prod in productions if prod.startswith(lookahead)]

# Then define the predictive parse function
def predictive_parse(tokens):
    stack = ['$', '<program>']
    token_index = 0
    tree = ParseTreeNode('<program>')
    node_stack = [tree]

    while stack:
        symbol = stack[-1]
        token_type = tokens[token_index][0] if token_index < len(tokens) else '$'

        if symbol.startswith('<'):
            # Non-terminal symbol
            if token_type not in parsing_table[symbol]:
                raise ValueError(f"Unexpected token type {token_type}: {tokens[token_index][1]}")
            production = parsing_table[symbol][token_type][0]
            node = ParseTreeNode(production)
            node_stack[-1].add_child(node)
            node_stack.append(node)
            stack.pop()
            for s in reversed(production.split()[::-1]):
                if s != '<epsilon>':
                    stack.append(s)
        elif symbol == token_type:
            # Terminal symbol
            node = ParseTreeNode(tokens[token_index])
            node_stack[-1].add_child(node)
            node_index += 1
            stack.pop()
        else:
            raise ValueError(f"Expected symbol {symbol}, got token type {token_type}: {tokens[token_index][1]}")

    return tree


table = ParseTable(rules)

print(table)

tree = parse(tokens, '<program>', table)
