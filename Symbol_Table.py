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

def praser(tokens, rules):
    pass
print(rules[0])
print(len(rules[1]))



def parse(tokens, rule):
    print(rule[0])
    for production in rule[1]:
        if production.endswith('*'):
            pass
        elif production.startswith('<'):
           pass
        else:
            pass

parse(tokens, rules)