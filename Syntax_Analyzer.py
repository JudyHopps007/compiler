
class ParseTreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def add_child(self, child):
        self.children.append(child)
# Define the production rules for the language using the | symbol to represent alternatives
# Define the production rules for the language
# Use a list of possible right-hand side productions for each left-hand side non-terminal symbol
# '|' is used as an 'or' operator between alternative productions
rules = {
    '<program>': [['<statement>']],
    '<statement>': [['<if_statement>'], ['<while_statement>'], ['<expression_statement>']],
    '<if_statement>': [['if', '(', '<expression>', ')', '<statement>']],
    '<while_statement>': [['while', '(', '<expression>', ')', '<statement>']],
    '<expression_statement>': [['<expression>', ';']],
    '<expression>': [['<identifier>', '=', '<expression>'], ['<simple_expression>']],
    '<simple_expression>': [['<term>', '<additive_operator>', '<term>']],
    '<term>': [['<factor>', '<multiplicative_operator>', '<factor>']],
    '<factor>': [['<identifier>'], ['<number>']],
    '<identifier>': [['IDENTIFIER']],
    '<number>': [['NUMBER']],
    '<additive_operator>': [['+'], ['-']],
    '<multiplicative_operator>': [['*'], ['/']]
}

# Define a function that recursively generates a parse tree from the token stream using the production rules
def parse(tokens, rule):
    node = ParseTreeNode(rule)

    # Get the list of possible right-hand side productions for the given rule
    rhs_list = rules[rule]

    for rhs in rhs_list:
        i = 0
        subtree = ParseTreeNode(rule)
        for symbol in rhs:
            if symbol.startswith('<'):
                # If the symbol is a non-terminal, recursively generate a subtree using the corresponding rule
                subrule = symbol
                child = parse(tokens, subrule)
                subtree.add_child(child)
            else:
                # If the symbol is a terminal, consume a token from the token stream and match it against the symbol
                if not tokens:
                    break
                token = tokens[0]
                if token[0] == symbol:
                    subtree.add_child(ParseTreeNode(token))
                    tokens.pop(0)
                    i += 1
                else:
                    break
        # If the entire right-hand side of the production matches the token stream, return the subtree
        if i == len(rhs):
            node.add_child(subtree)
            break

    return node


# Define a function that runs the syntax analyzer on the token stream
def syntax_analyze(tokens):
    tree = parse(tokens, '<program>')
    if tokens:
        raise ValueError("Unexpected tokens at end of input")
    return tree

# Example usage

import lexical_Analyzer
tokens = lexical_Analyzer.lex('program.c')
print(tokens)
tree = syntax_analyze(tokens)
print(tree.value)
