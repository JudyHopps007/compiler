import lexical_Analyzer

tokens = lexical_Analyzer.lex('program.c')

print('\nTOKENS\n\t', tokens)

rules = [
    ('<program>', ['<include_list>',  '<declaration>']),
    ('<include_list>', ['INCLUDE_DIRECTIVE']),

    ('<declaration>', ['<function_declaration>*', '<include_list>']),
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
    stack = ['$']
    input_list = [token[0] for token in tokens] + ['$']
    input_index = 0
    current_production = ('<program>', [])

    while True:
        top_of_stack = stack[-1]
        if top_of_stack in ('$', '<declaration>', '<function_declaration>', '<parameter_list>', '<more_parameters>', '<type_specifier>', '<identifier>', '<comma>', '<compound_statement>'):
            stack.pop()
            current_production[1].append(top_of_stack)
            for rule in rules:
                if rule[0] == top_of_stack and current_production[1] == rule[1]:
                    current_production = rule
                    break
        elif top_of_stack == input_list[input_index]:
            stack.pop()
            input_index += 1
        else:
            # There is a syntax error
            return False

        if current_production[1] == []:
            if current_production[0] == '<program>':
                # The input is syntactically correct
                return True
            else:
                stack.append(current_production[0])
                current_production = ('', [])
        else:
            for symbol in reversed(current_production[1]):
                stack.append(symbol)
