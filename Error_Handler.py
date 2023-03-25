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

    ('<declaration>', ['<function_declaration>*']),
    ('<declaration>', []),


    ('<function_declaration>', ['<type_specifier>', '<identifier>', '<parameter_list>',  '<compound_statement>']),

    #('<function_declaration_closure>', ['<type_specifier>', '<identifier>', '<parameter_list>',  '<compound_statement>']),

    ('<parameter_list>', ['LEFT_PAREN', '<type_specifier>', '<identifier>', 'RIGHT_PAREN']),
    ('<more_parameters>', ['COMMA', '<type_specifier>', '<identifier>', '<more_parameters>']),
    ('<more_parameters>', []),

    ('<type_specifier>', ['KEYWORD']),
    ('<identifier>', ['IDENTIFIER']),
    ('<identifier>', ['main_f']),

    ('<comma>', ['COMMA']),
    ('<compound_statement>', ['LEFT_BRACE', 'RIGHT_BRACE']),


]






# ('<function_declaration>', ['<type_specifier>', '<identifier>', 'LEFT_PAREN', 'RIGHT_PAREN', '<compound_statement>']),

# Define a function that recursively generates a parse tree from the token stream using the production rules
def calculate_similarity(rule1, rule2):
    # Calculate similarity between two production rules by counting the number of common non-terminals in their productions
    common_non_terminals = set(rule1[1]).intersection(set(rule2[1]))
    return len(common_non_terminals)

def parse(tokens, rule, kleene_dict=None):
    node = ParseTreeNode(rule[0])
    print(rule[0])

    # Check for similar production rules and choose the most likely one
    similar_rules = []
    for r in rules:
        if r[0] == rule[0]:
            similarity = calculate_similarity(r, rule)
            similar_rules.append((r, similarity))
    if similar_rules:
        most_similar_rule = max(similar_rules, key=lambda x: x[1])[0]
        rule = most_similar_rule

    for production in rule[1]:
        if production.endswith('*'):
            # If the production is a Kleene closure of a non-terminal
            non_terminal = production[:-1]
            subrules = [r for r in rules if r[0] == non_terminal]
            if not subrules:
                raise ValueError("Invalid production rule: " + non_terminal)
            while True:
                try:
                    child = parse(tokens, subrules[0], kleene_dict)
                    node.add_child(child)
                    print('\t \t Match', subrules[0])
                except ValueError:
                    break
                if not tokens:
                    break  # Added check for end of input
        elif production.startswith('<'):
            # If the production is a non-terminal, recursively generate a subtree using the corresponding rule
            subrules = [r for r in rules if r[0] == production]
            if not subrules:
                raise ValueError("Invalid production rule: " + production)
            match_found = False
            for subrule in subrules:
                try:
                    child = parse(tokens, subrule, kleene_dict)
                    node.add_child(child)
                    match_found = True
                    print('\t \t Match', subrule)
                    break
                except ValueError as e:
                    print('r', e)

            if not match_found:
                raise ValueError("No matching subrule found for production rule: ", production)
        else:
            # If the production is a terminal, consume a token from the token stream and match it against the production
            if not tokens:
                raise ValueError("Unexpected end of input")

            token = tokens.pop(0)
            print('============', token)
            if token[0] != production:
                raise ValueError(f"Expected token type {production}, got {token[0]}: {token[1]}")
            node.add_child(ParseTreeNode(token))

    # Handle Kleene closure specified in the rule
    if kleene_dict and rule[0] in kleene_dict:
        while True:
            try:
                child = parse(tokens, rule, kleene_dict=None)
                node.add_child(child)
                print('\t \t Kleene closure')
            except ValueError:
                break
            if not tokens:
                break  # Added check for end of input

    return node

def similarity_score(rule1, rule2):
    """
    Compute a similarity score between two production rules based on how many common non-terminals they share.
    """
    non_terminals1 = set([p for p in rule1[1] if p.startswith('<')])
    non_terminals2 = set([p for p in rule2[1] if p.startswith('<')])
    common_non_terminals = non_terminals1.intersection(non_terminals2)
    return len(common_non_terminals)



# Define a function that runs the syntax analyzer on the token stream
def syntax_analyze(tokens):
    tree = parse(tokens, rules[0])
    if tokens:
        raise ValueError("Unexpected tokens at end of input")
    return tree


print('\nTOKENS\n\t', tokens)
tree = syntax_analyze(tokens)
print("tree", tree)
