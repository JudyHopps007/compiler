token =   [('PREPROCESSOR_DIRECTIVE', '#include <stdio.h>'), ('KEYWORD', 'int'), ('IDENTIFIER', 'main'), ('LEFT_PAREN', '('), ('RIGHT_PAREN', ')'), ('LEFT_BRACE', '{'), ('KEYWORD', 'int'), ('IDENTIFIER', 'a'), ('ASSIGN', '='), ('INTEGER', '10'), ('SEMICOLON', ';'), ('KEYWORD', 'int'), ('IDENTIFIER', 'b'), ('ASSIGN', '='), ('INTEGER', '20'), ('SEMICOLON', ';'), ('KEYWORD', 'int'), ('IDENTIFIER', 'c'), ('ASSIGN', '='), ('IDENTIFIER', 'a'), ('PLUS', '+'), ('IDENTIFIER', 'b'), ('SEMICOLON', ';'), ('IDENTIFIER', 'printf'), ('LEFT_PAREN', '('), ('STRING', '"The sum of a and b is %d\\n"'), ('COMMA', ','), ('IDENTIFIER', 'c'), ('RIGHT_PAREN', ')'), ('SEMICOLON', ';'), ('KEYWORD', 'return'), ('INTEGER', '0'), ('SEMICOLON', ';'), ('RIGHT_BRACE', '}')]

production_rules = {
        'program': [('declaration', 'program'), ('declaration',)],
        'declaration': [('INCLUDE_ID',), ('INCLUDE_DIRECTIVE',), ('KEYWORD', 'IDENTIFIER', '(', 'parameters', ')', '{', 'statements', '}',)],
        'parameters': [('void',), ('parameter_list',)],
        'parameter_list': [('parameter',), ('parameter_list', ',', 'parameter')],
        'parameter': [('KEYWORD', 'IDENTIFIER')],
        'statements': [('statement',), ('statement', 'statements')],
        'statement': [('expression_statement',), ('if_statement',), ('while_statement',)],
        'expression_statement': [('assignment_expression', ';'), ('expression', ';')],
        'assignment_expression': [('IDENTIFIER', '=', 'assignment_expression'), ('logical_or_expression',)],
        'expression': [('logical_or_expression',)],
        'logical_or_expression': [('logical_and_expression',), ('logical_or_expression', '||', 'logical_and_expression')],
        'logical_and_expression': [('equality_expression',), ('logical_and_expression', '&&', 'equality_expression')],
        'equality_expression': [('relational_expression',), ('equality_expression', '==', 'relational_expression'), ('equality_expression', '!=', 'relational_expression')],
        'relational_expression': [('additive_expression',), ('relational_expression', '<', 'additive_expression'), ('relational_expression', '>', 'additive_expression'), ('relational_expression', '<=', 'additive_expression'), ('relational_expression', '>=', 'additive_expression')],
        'additive_expression': [('multiplicative_expression',), ('additive_expression', '+', 'multiplicative_expression'), ('additive_expression', '-', 'multiplicative_expression')],
        'multiplicative_expression': [('unary_expression',), ('multiplicative_expression', '*', 'unary_expression'), ('multiplicative_expression', '/', 'unary_expression'), ('multiplicative_expression', '%', 'unary_expression')],
        'unary_expression': [('postfix_expression',), ('-', 'unary_expression'), ('!', 'unary_expression')],
        'postfix_expression': [('primary_expression',), ('postfix_expression', '(', 'argument_expression_list', ')')],
        'primary_expression': [('IDENTIFIER',), ('INTEGER',), ('FLOATING_POINT',), ('CHAR',), ('STRING',), ('(', 'expression', ')')],
        'argument_expression_list': [('assignment_expression',), ('argument_expression_list', ',', 'assignment_expression')],
        'if_statement': [('IF', '(', 'expression', ')', '{', 'statements', '}', 'else_clause')],
        'else_clause': [('ELSE', '{', 'statements', '}'), ()],
        'while_statement': [('WHILE', '(', 'expression', ')', '{', 'statements', '}')],
    }



def parse(tokens, production_rules):
        # Initialize the parse stack.
        stack = ['$']

        # Initialize the parse tree.
        tree = []

        # Iterate over the tokens.
        for token in tokens:
            # Pop the top of the stack.
            sym = stack.pop()

            # If the top of the stack is a nonterminal,
            # try to match it against the current token.
            if sym in production_rules:
                for rule in production_rules[sym]:
                    if token == rule[0]:
                        stack.append(rule[1])
                        tree.append(rule[0])
                        break
                else:
                    # If the token does not match any of the production rules for the top of the stack,
                    # the parse fails.
                    print('Parse error at token', token)
                    return None
            else:
                # If the top of the stack is a terminal,
                # push it onto the parse tree.
                tree.append(sym)

        # If the parse stack is empty, the parse succeeds.
        if not stack:
            return tree
        else:
            # If the parse stack is not empty, the parse fails.
            print('Parse error, parse stack is not empty')
            return None

parse(token, production_rules)