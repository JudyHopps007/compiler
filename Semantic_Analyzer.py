class ParseTreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def add_child(self, child):
        self.children.append(child)


def find_matching_subrule(rules, production):
    subrules = [r for r in rules if r[0] == production]
    if not subrules:
        raise ValueError(f"No matching subrule found for production rule: {production}")
    for subrule in subrules:
        try:
            parse([], subrule)
            return subrule
        except ValueError:
            pass
    raise ValueError(f"No matching subrule found for production rule: {production}")


def parse(tokens, rule, rules):
    if not tokens:
        raise ValueError("Unexpected end of input")
    if not rule:
        raise ValueError("Invalid rule")
    node = ParseTreeNode(rule[0])
    for production in rule[1]:
        if production.startswith('<'):
            # If the production is a non-terminal, recursively generate a subtree using the corresponding rule
            subrule = find_matching_subrule(rules, production)
            child = parse(tokens, subrule, rules)
            node.add_child(child)
        else:
            # If the production is a terminal, consume a token from the token stream and match it against the production
            if not tokens:
                raise ValueError("Unexpected end of input")
            token = tokens.pop(0)
            if token[0] != production:
                raise ValueError(f"Expected token type {production}, got {token[0]}: {token[1]}")
            node.add_child(ParseTreeNode(token))
    return node


rules = [
    ('<program>', ['<include-list>',  '<declaration>']),
    ('<include-list>', ['INCLUDE_DIRECTIVE']),


    ('<declaration>', ['<function_declaration>', "<declaration>"]),
    ('<declaration>', []),

    ('<function_declaration>', ['<type_specifier>', '<identifier>', 'LEFT_PAREN', 'RIGHT_PAREN' '<compound_statement>']),

    ('<type_specifier>', ['KEYWORD']),
    ('<identifier>', ['IDENTIFIER']),
    ('<identifier>', ['main_f']),



    ('<comma>', ['COMMA']),


    ('<compound_statement>', ['LEFT_BRACE', 'RIGHT_BRACE']),
]
import lexical_Analyzer

tokens = lexical_Analyzer.lex('program.c')
p = ('<program>', ['<include-list>',  '<declaration>'])
parse(tokens, p, rules)