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




class ParseTable:
    def __init__(self, rules):
        self.table = {}
        for nonterminal, productions in rules:
            for lookahead in self.get_first_set(productions):
                if lookahead not in self.table:
                    self.table[lookahead] = {}
                self.table[lookahead][nonterminal] = productions

    def get_first_set(self, symbols):
        first_set = set()
        for symbol in symbols:
            if symbol.startswith('<'):
                first_set.update(self.get_first_set(self.table.get(symbol, {})))
                if ('EPSILON' not in first_set):
                    break
            else:
                first_set.add(symbol)
                break
        else:
            first_set.add('EPSILON')
        return first_set


def parse(tokens, start_symbol, parse_table):
    stack = [start_symbol]
    tree_stack = [ParseTreeNode(start_symbol)]
    lookahead = tokens[0][0] if tokens else None

    while stack:
        symbol = stack.pop()
        tree = tree_stack.pop()

        if symbol.startswith('<'):
            production = parse_table.table[lookahead].get(symbol, None)
            if production is None:
                raise ValueError(f"Unexpected token: {lookahead}")
            for rhs_symbol in reversed(production):
                stack.append(rhs_symbol)
                if rhs_symbol.startswith('<'):
                    tree.add_child(ParseTreeNode(rhs_symbol))
                    tree_stack.append(tree.children[-1])
                else:
                    if not tokens:
                        raise ValueError("Unexpected end of input")
                    token = tokens.pop(0)
                    if token[0] != rhs_symbol:
                        raise ValueError(f"Expected token type {rhs_symbol}, got {token[0]}: {token[1]}")
                    tree.add_child(ParseTreeNode(token))
                    lookahead = tokens[0][0] if tokens else None

        else:
            if not tokens:
                raise ValueError("Unexpected end of input")
            token = tokens.pop(0)
            if token[0] != symbol:
                raise ValueError(f"Expected token type {symbol}, got {token[0]}: {token[1]}")
            tree.add_child(ParseTreeNode(token))
            lookahead = tokens[0][0] if tokens else None

    return tree



table = ParseTable(rules)

print(table)

tree = parse(tokens, '<program>', table)
