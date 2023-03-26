import lexical_Analyzer

tokens = lexical_Analyzer.lex('program.c')

print('\nTOKENS\n\t', tokens)

rules = [
    ('<program>', ['<include_list>',  '<declaration>']),
    ('<include_list>', ['INCLUDE_DIRECTIVE']),

    ('<declaration>', ['<function_declaration>', '<include_list>']),
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
    while stack:
        top = stack.pop()
        if top.startswith('<'):
            # Non-terminal symbol
            rule = None
            for r in rules:
                if r[0] == top:
                    rule = r
                    break
            if rule is None:
                raise ValueError(f"No rule found for non-terminal symbol {top}")
            for symbol in reversed(rule[1]):
                stack.append(symbol)
        elif top == tokens[i][0]:
            # Terminal symbol matches token
            i += 1
        else:
            raise ValueError(f"Unexpected token {tokens[i]} for expected symbol {top}")
    if i != len(tokens):
        raise ValueError(f"Unexpected token {tokens[i]} at end of input")

syntax_analyzer(tokens, rules)