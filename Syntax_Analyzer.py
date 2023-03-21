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
    ('<program>', ['<include-list>',  '<declaration>']),
    ('<include-list>', ['INCLUDE_DIRECTIVE']),
    ('<declaration>', ['<function_declaration>', "<declaration>"]),
    ('<declaration>', []),
    ('<function_declaration>', ['<type_specifier>', '<identifier>', 'LEFT_PAREN', '<parameter_list>', 'RIGHT_PAREN', '<compound_statement>']),
    ('<type_specifier>', ['KEYWORD']),
    ('<identifier>', ['IDENTIFIER']),
    ('<parameter_list>', ['<statement>']),
    ('<parameter_list>', ['<<parameter_list>>', 'COMMA', '<statement>']),
    ('<parameter_list>', []),
    ('<statement>', ['<type_specifier>', 'IDENTIFIER']),
    ('<statement>', ['IDENTIFIER']),

    ('<compound_statement>', ['LEFT_BRACE', 'RIGHT_BRACE']),
]


# Define a function that recursively generates a parse tree from the token stream using the production rules
def parse(tokens, rule):
    node = ParseTreeNode(rule[0])
    print(rule[0])
    for production in rule[1]:
        if production.startswith('<'):
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
                try:
                    print(f"\nExpected token type {production}, got {tokens[0]}: {tokens[1]}")
                    raise ValueError("No matching subrule found for production rule: ", production)
                except:
                    raise ValueError("No matching subrule found for production rule: ", production)
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


print(tokens)
tree = syntax_analyze(tokens)
print("tree", tree.value)
