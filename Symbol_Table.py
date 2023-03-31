import lexical_Analyzer

tokens = lexical_Analyzer.lexical_analyzer('program.c')

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
    ('<program>', [ '<declaration>']),
    ('<include-list>', ['INCLUDE_ID', 'INCLUDE_DIRECTIVE']),
    ('<declaration>', ['<function_declaration>*']),
    ('<function_declaration>', ['<type_specifier>', '<identifier>', '<parameter_list>',  '<compound_statement>']),
    ('<parameter_list>', ['LEFT_PAREN',  'RIGHT_PAREN']),
    ('<parameters>', ['<type_specifier>', '<identifier>']),
    ('<more_parameters>', ['COMMA', '<type_specifier>', '<identifier>', '<more_parameters>']),
    ('<more_parameters>', []),
    ('<type_specifier>', ['KEYWORD']),
    ('<identifier>', ['IDENTIFIER']),
    ('<comma>', ['COMMA']),
    ('<compound_statement>', ['LEFT_BRACE', 'RIGHT_BRACE']),


]


# Define a function that recursively generates a parse tree from the token stream using the production rules
class ParseTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __str__(self):
        return f"{self.value} ({', '.join(str(c) for c in self.children)})"

    def __repr__(self):
        return self.__str__()


class ParseTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return str(self.value)


def parse(tokens, rule, rules, kleene_dict=None):
    node = ParseTreeNode(rule[0])
    for production in rule[1]:
        if production.endswith('*'):
            # If the production is a Kleene closure of a non-terminal
            non_terminal = production[:-1]
            subrules = [r for r in rules if r[0] == rule[0]]
            while True:
                try:
                    child = parse(tokens, subrules[0], rules, kleene_dict=rule)
                    node.add_child(child)
                except ValueError:
                    break
                if not tokens:
                    break
        elif production.startswith('<'):
            # If the production is a non-terminal, recursively generate a subtree using the corresponding rule
            subrules = [r for r in rules if r[0] == production]
            if not subrules:
                raise ValueError("Invalid production rule: " + production)
            match_found = False
            for subrule in subrules:
                try:
                    child = parse(tokens, subrule, rules, kleene_dict=kleene_dict)
                    node.add_child(child)
                    match_found = True
                    break
                except ValueError:
                    pass
            if not match_found:
                raise ValueError("No matching subrule found for production rule: ", production)
        else:
            # If the production is a terminal, consume a token from the token stream and match it against the production
            if not tokens:
                raise ValueError("Unexpected end of input")
            token = tokens.pop(0)
            if token[0] != production:
                raise ValueError(f"Expected token type {production}, got {token[0]}: {token[1]}")
            node.add_child(ParseTreeNode(token))
    # Handle Kleene closure specified in the rule
    if kleene_dict and rule[0] in kleene_dict:
        while True:
            try:
                child = parse(tokens, rule, rules, kleene_dict=rule)
                node.add_child(child)
            except ValueError:
                break
            if not tokens:
                break
    return node


def syntax_analyze(tokens, rules):
    tree = parse(tokens, rules[0], rules)
    if tokens:
        raise ValueError("Unexpected tokens at end of input")
    return tree


print('\nTOKENS\n\t', tokens)
tree = syntax_analyze(tokens, rules)
print("tree", tree)
