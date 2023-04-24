import lexical_Analyzer

tokens = lexical_Analyzer.lexical_analyzer('program.c')
list = []

print("\n\n")


def compound_statement():
    pass


def parma(token, pos):
    parame = ''
    pos += 1
    i = 0
    while token[pos][0] != 'RIGHT_PAREN':

        if token[pos][0] == 'KEYWORD':
            if token[pos + 1][0] == 'IDENTIFIER':
                if token[pos + 2][0] == 'COMMA':
                    parame += token[pos][1] + ' ' + token[pos + 1][1] + ' ' + token[pos + 2][1]
                    pos += 1
                else:
                    parame += token[pos][1] + '  ' + token[pos + 1][1]
                    pos += 1
            else:
                print("Error Expected IDENTIFIER")
        elif token[pos][0] == 'IDENTIFIER':
            if token[pos + 1][0] == 'COMMA':
                parame += token[pos][1] + ' ' + token[pos + 1][1]
            else:
                parame += token[pos][1]
        pos += 1
        i += 1
    return parame, pos


def condition(tokens, position):
    global express_n
    condition_statment = ''
    current_token = position
    current_token, left_operand, = expression(tokens, current_token)
    condition_statment += left_operand
    express_n = ''
    token_type = tokens[current_token][0]
    if token_type == 'EQUAL' or token_type == 'NOT_EQUAL' or token_type == 'LESS_THAN' or token_type == 'GREATER_THAN' or token_type == 'LESS_THAN_EQUAL' or token_type == 'GREATER_THAN_EQUAL':
        conditional_operator = tokens[current_token][1]
        condition_statment += " " + conditional_operator
        current_token, right_operand, = expression(tokens, current_token)
        condition_statment += " " + right_operand
        express_n = ''
    else:
        print("Syntax Error: conditional_operator error ")
    return current_token, condition_statment

def if_statment(token, postion):
    pass

def statment(token, postion): # statement: (declaration | initializing | function_call | assignment | if_statement | while_statement | return_statement)*;
    current_token = postion
    # declaration



express_n = ""


def expression(tokens, position):
    global express_n
    express_n += ''
    current_token = position + 1
    while current_token < len(tokens):
        token_type, token_value = tokens[current_token]
        if token_type == 'IDENTIFIER':
            express_n += token_value + ' '
        elif token_type == 'INTEGER':
            express_n += token_value + ' '
        elif token_type == 'LEFT_PAREN':
            express_n += token_value + ' '
            expression(tokens, current_token)  # Handle nested expressions recursively
            while tokens[current_token][0] != 'RIGHT_PAREN':
                current_token += 1
            express_n += tokens[current_token][1] + ' '

            # Skip to the end of the nested expression
        elif token_type == 'PLUS':
            express_n += token_value + ' '
        elif token_type == 'SEMICOLON' or token_type == 'RIGHT_PAREN' or token_type == 'EQUAL' or token_type == 'NOT_EQUAL' or token_type == 'LESS_THAN' or token_type == 'GREATER_THAN' or token_type == 'LESS_THAN_EQUAL' or token_type == 'GREATER_THAN_EQUAL':
            break
        else:
            print(f"Sytax error -- Expression Error Cause:  {tokens[current_token][1]}")

        current_token += 1
    return current_token, express_n


def parse_program(tokens):
    current_token = 0
    print(tokens[current_token])
    while current_token < len(tokens):

        if tokens[current_token][0] == "INCLUDE_ID":
            if tokens[current_token + 1][0] == 'INCLUDE_DIRECTIVE':
                # handle include list
                include_directive = tokens[current_token][1] + ' ' + tokens[current_token + 1][1]
                current_token += 1
                print(f"include list: {include_directive}")
            else:
                print(f"SYNTAX ERROR: INCLUDE_DIRECTIVE: {tokens[current_token + 1][1]}")
                current_token += 1

        elif tokens[current_token][0] == "KEYWORD" and tokens[current_token][1] != 'return':

            if tokens[current_token + 1][0] == "IDENTIFIER":

                if tokens[current_token + 2][0] == "SEMICOLON":  # handle declaration
                    type = tokens[current_token][1]
                    name = tokens[current_token + 1][1]
                    terminator = tokens[current_token + 2][1]
                    print(f"Declaration {type} {name} {terminator}")
                    current_token += 2

                elif tokens[current_token + 2][0] == "LEFT_PAREN":  # handle functions
                    function_type = tokens[current_token][1]
                    function_name = tokens[current_token + 1][1]
                    f_lp = tokens[current_token + 2][1]
                    function_parameter, pos = parma(tokens, (current_token + 2))
                    current_token = pos
                    if tokens[current_token][0] == "RIGHT_PAREN":
                        if tokens[current_token + 1][0] == "LEFT_BRACE":
                            compound_statement()
                            # call function body
                            if tokens[current_token + 2][0] == "RIGHT_BRACE":
                                f_rp = tokens[current_token][1]
                                f_lb = tokens[current_token + 1][1]
                                statment = None
                                f_rb = tokens[current_token + 2][1]
                                print(f"Function: {function_type}  {function_name} {f_lp} {function_parameter} {f_rp} {f_lb} {statment}{f_rb}")
                                current_token += 2
                            else:
                                print("Function not closed ")

        elif tokens[current_token][0] == 'IF':
            if_key_word = tokens[current_token][1]
            if tokens[current_token + 1][0] == 'LEFT_PAREN':
                l_p = tokens[current_token + 1][1]
                current_token, condition_statment = condition(tokens, current_token + 1)
                if tokens[current_token][0] == 'RIGHT_PAREN':
                    r_p = tokens[current_token][1]
                    if tokens[current_token + 1][0] == 'LEFT_BRACE':
                        l_b = tokens[current_token + 1][1]
                        # statment()
                        if tokens[current_token + 2][0] == 'RIGHT_BRACE':
                            if_condition = condition_statment
                            if_statment = None
                            r_b = tokens[current_token + 2][1]
                            current_token += 2
                            try:
                                if tokens[current_token + 1][0] != 'ELSE':
                                    print(f"IF statemt: {if_key_word} {l_p} {if_condition} {r_p} {l_b} {if_statment} {r_b}")
                                else:
                                    if tokens[current_token + 2][0] == 'LEFT_BRACE':
                                        # statment()
                                        if tokens[current_token + 3][0] == 'RIGHT_BRACE':
                                            else_key = tokens[current_token + 1][1]
                                            e_lb = tokens[current_token + 2][1]
                                            else_statment = None
                                            e_rb = tokens[current_token + 3][1]
                                            print(f"IF-ELSE statemt: {if_key_word} {l_p} {if_condition} {r_p} {l_b} {if_statment} {r_b} {else_key} {e_lb} {else_statment} {e_rb}")
                                            current_token += 3
                            except:
                                print(f"IF statemt: {if_key_word} {l_p} {if_condition} {r_p} {l_b} {if_statment} {r_b}")


        elif tokens[current_token][0] == 'WHILE':
            while_key = tokens[current_token][0]
            if tokens[current_token + 1][0] == 'LEFT_PAREN':
                wh_lp = tokens[current_token + 1][1]
                current_token, condition_statment = condition(tokens, current_token + 1)
                if tokens[current_token][0] == 'RIGHT_PAREN':
                    wh_rp = tokens[current_token][1]
                    if tokens[current_token + 1][0] == 'LEFT_BRACE':
                        wh_lb = tokens[current_token + 1][1]
                        # statment()
                        if tokens[current_token + 2][0] == 'RIGHT_BRACE':
                            wh_rb = tokens[current_token + 2][1]
                            wh_condition = condition_statment
                            wh_statment = None

                            print(F"WHILE-STATEMENT: {while_key} {wh_lp} {wh_condition} {wh_rp} {wh_lb} {wh_statment} {wh_rb}")
                            current_token += 2

        elif tokens[current_token][1] == 'return':
            current_token, express = expression(tokens, current_token)
            print("RETURN-STATMENT  : return ", express)
            global express_n
            express_n = ''

        current_token += 1


parser = parse_program(tokens)
