# Define the grammar
rules = [
    ('<expr>', ['<term>', '+', '<term>']),
    ('<expr>', ['<term>']),
    ('<term>', ['<factor>', '*', '<factor>']),
    ('<term>', ['<factor>']),
    ('<factor>', ['NUMBER']),
    ('<factor>', ['(', '<expr>', ')']),
]

# Parse a simple expression: 2 * (3 + 4)
tokens = [('NUMBER', '2'), ('*', ''), ('(', ''), ('NUMBER', '3'), ('+', ''), ('NUMBER', '4'), (')', '')]

# Define the parse tree node class
class ParseTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

# Define the parse function
def parse(tokens, rule):
    node = ParseTreeNode(rule[0])
    for production in rule[1]:
        if production.endswith('*'):
            # If the production ends with '*', apply the Kleene closure
            subrule = [production[:-1]]
            while True:
                try:
                    child = parse(tokens, subrule)
                    node.add_child(child)
                except ValueError:
                    break
        elif production.startswith('<'):
            # If the production is a non-terminal, recursively generate a subtree using the corresponding rule
            subrules = [r for r in rules if r[0] == production]
            if not subrules:
                raise ValueError("Invalid production rule: " + production)
            match_found = False
            for subrule in subrules:
                try:
                    child = parse(tokens, subrule)
                    node.add_child(child)
                    match_found = True
                    break
                except ValueError:
                    pass
            if not match_found:
                raise ValueError("No matching subrule found for production rule: " + production)
        else:
            # If the production is a terminal, consume a token from the token stream and match it against the production
            if not tokens:
                raise ValueError("Unexpected end of input")
            token = tokens.pop(0)
            if token[0] != production:
                raise ValueError(f"Expected token type {production}, got {token[0]}: {token[1]}")
            node.add_child(ParseTreeNode(token))
    return node

# Parse the input tokens using the <expr> rule
tree = parse(tokens, ('<expr>',))

# Print the parse tree
def print_tree(node, indent=0):
    print('  ' * indent + str(node.value))
    for child in node.children:
        print_tree(child, indent + 1)
print_tree(tree)
