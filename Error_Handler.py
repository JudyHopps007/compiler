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
    ('<declaration>', ['<function_declaration>']),
    ('<function_declaration>', ['<type_specifier>', '<identifier>', 'LEFT_PAREN', '<parameter_list>', 'RIGHT_PAREN', '<compound_statement>']),
    ('<type_specifier>', ['KEYWORD']),
    ('<identifier>', ['IDENTIFIER']),
    ('<parameter_list>', ['<statement>', 'COMMA', '<statement>']),
    ('<statement>', ['<type_specifier>', 'IDENTIFIER']),
    ('<compound_statement>', ['LEFT_BRACE', '<type_specifier>', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'PLUS', 'IDENTIFIER', 'SEMICOLON', 'KEYWORD', 'IDENTIFIER', 'SEMICOLON', 'RIGHT_BRACE']),
]

def edit_distance(s1, s2):
    """Compute the edit distance between two strings."""
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

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
            min_edit_distance = float('inf')
            for subrule in subrules:
                try:
                    child = parse(tokens, subrule)
                    node.add_child(child)
                    match_found = True
                    break
                except ValueError:
                    # If no matching subrule is found, check for a slightly matching subrule
                    distance = edit_distance(subrule[0], production)
                    if distance < min_edit_distance:
                        min_edit_distance = distance
                        best_subrule = subrule
            if not match_found:
                raise ValueError(f"No matching subrule found for production rule: {production}. "
                                 f"Did you mean: {best_subrule[0]}?")
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
