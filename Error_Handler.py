import lexical_Analyzer

tokens = lexical_Analyzer.lexical_analyzer('program.c')

print('\nTOKENS\n\t', tokens)

rules = [
    ('<program>', ['<include_list>',  '<declaration>']),
    ('<include_list>', ['INCLUDE_DIRECTIVE']),

    ('<declaration>', ['<function_declaration>']),
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

def syntax_analyzer(tokens, rules):
    stack = ['<program>']
    i = 0
    line = 1
    column = 1

    # Validate input
    non_terminals = set(rule[0] for rule in rules)
    for token_type, token_value in tokens:
        if token_type not in non_terminals and token_type not in ['IDENTIFIER', 'NUMBER', 'STRING', 'BOOLEAN']:
            raise ValueError(f"Invalid token type '{token_type}' at line {line}, column {column}")
        column += len(token_value)

        if token_value == '\n':
            line += 1
            column = 1

    # Parse tokens
    while stack:
        symbol = stack.pop()

        if symbol.startswith('<'):
            # Non-terminal symbol
            for rule_lhs, rule_rhs in rules:
                if rule_lhs == symbol:
                    stack += reversed(rule_rhs)
                    break
        else:
            # Terminal symbol
            token_type, token_value = tokens[i]
            if symbol == token_type:
                i += 1
            else:
                raise SyntaxError(f"Expected '{symbol}' at line {line}, column {column}, but found '{token_type}' '{token_value}'")

            column += len(token_value)
            if token_value == '\n':
                line += 1
                column = 1

    # Check for extra tokens
    if i < len(tokens):
        raise SyntaxError(f"Unexpected token '{tokens[i][0]}' '{tokens[i][1]}' at line {line}, column {column}")

    # Parsing successful
    return True


syntax_analyzer(tokens, rules)