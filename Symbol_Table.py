import lexical_Analyzer

tokens = lexical_Analyzer.lex('program.c')

print('\nTOKENS\n\t', tokens)

rules = [
    ('<program>', ['<include_list>',  '<declaration>']),
    ('<include_list>', ['INCLUDE_DIRECTIVE']),

    ('<declaration>', ['<function_declaration>', '<declaration>']),
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
    stack = ['<program>'] # initial stack with the starting symbol
    i = 0 # index of the current token

    while stack:
        symbol = stack.pop() # get the next symbol from the stack

        if symbol.startswith('<'):
            # symbol is a non-terminal, look up its production rule
            for rule_lhs, rule_rhs in rules:
                if rule_lhs == symbol:
                    stack += reversed(rule_rhs) # push rhs symbols in reverse order to the stack
                    break
        else:
            # symbol is a terminal, compare it with the current token
            token_type, token_value = tokens[i]

            if symbol == token_type:
                i += 1 # advance to the next token
            else:
                print(f"Syntax error: expected {symbol}, but found {token_type} '{token_value}'")
                return False

    if i < len(tokens):
        print(f"Syntax error: unexpected token {tokens[i][0]} '{tokens[i][1]}'")
        return False
    else:
        print("Syntax analysis successful!")
        return True


syntax_analyzer(tokens, rules)