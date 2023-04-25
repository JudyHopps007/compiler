import lexical_Analyzer # importing scanner source file for token list
import time   # for measuring 'parser' run time


tokens = lexical_Analyzer.lexical_analyzer('program.c')
Error_list = ""  # keep store track of syntax errors generated
express_n = ""  # keep store of expression statments  errors generated
print("\n\n")


def parameter_RFC(token, pos):
    parame = '' # keep store parameters that are found
    pos += 1
    i = 0
    while token[pos][0] != 'RIGHT_PAREN':
        if token[pos][0] == 'KEYWORD':
            if token[pos + 1][0] == 'IDENTIFIER':
                if token[pos + 2][0] == 'COMMA':
                    if token[pos + 3][0] != 'RIGHT_PAREN':
                        parame += token[pos][1] + ' ' + token[pos + 1][1] + ' ' + token[pos + 2][1]
                        pos += 1
                    else:
                        parame += token[pos][1] + ' ' + token[pos + 1][1] + ' ' + token[pos + 2][1]
                        pos += 1
                elif token[pos + 2][0] == 'KEYWORD':
                    parame += token[pos][1] + '  ' + token[pos + 1][1] + "  <missing ','>  "
                    pos += 1
                else:
                    print("syntax: <missing ','> at line", token[pos + 2][2])
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


def condition_statement_RFC(tokens, position):
        global express_n
        condition_statment = '' # store condition statements
        current_token = position
        current_token, left_operand, = expression(tokens, current_token)
        condition_statment += left_operand
        express_n = ''
        if current_token < len(tokens) and (tokens[current_token][0] == 'EQUAL' or tokens[current_token][0] == 'NOT_EQUAL' or tokens[current_token][0] == 'LESS_THAN' or tokens[current_token][0] == 'GREATER_THAN' or tokens[current_token][0] == 'LESS_THAN_EQUAL' or tokens[current_token][0] == 'GREATER_THAN_EQUAL'):
            conditional_operator = tokens[current_token][1]
            condition_statment += " " + conditional_operator
            current_token, right_operand, = expression(tokens, current_token)
            condition_statment += " " + right_operand
            express_n = ''
        if len(condition_statment) == 0:
            print("Syntax Error: Condition statement not provided")
        return current_token, condition_statment


def statments(token, postion):  # statement: (declaration | initializing | function_call | assignment | if_statement | while_statement | return_statement)*;
    global express_n, Error_list
    statment_block = '' # store statements in block
    block_track = 1
    current_token = postion
    while block_track != 0:
        current_token += 1
        if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_BRACE':
            statment_block += '\n\t\t\t\t\t'
            block_track -= 1
        elif current_token < len(tokens) and tokens[current_token][0] == "KEYWORD" and tokens[current_token][1] != 'return':
            type = tokens[current_token][1]
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "IDENTIFIER":
                name = tokens[current_token + 1][1]
                if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "SEMICOLON":  # handle declaration
                    terminator = tokens[current_token + 2][1]
                    # print(f"Declaration {type} {name} {terminator}")
                    statment_block += f"\n\t\t\t\t\tDECLARATION:   {type} {name} {terminator}"
                    current_token += 2

                elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "LEFT_PAREN":  # handle functions
                    f_lp = tokens[current_token + 2][1]
                    function_parameter, pos = parameter_RFC(tokens, (current_token + 2))
                    current_token = pos
                    if current_token < len(tokens) and tokens[current_token][0] == "RIGHT_PAREN":
                        block_track += 1
                        f_rp = tokens[current_token][1]
                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "LEFT_BRACE":
                            block_track -= 1
                            f_lb = tokens[current_token + 1][1]
                            current_token, function_body = statments(tokens, current_token + 1)
                            if current_token < len(tokens) and tokens[current_token][0] == "RIGHT_BRACE":
                                block_track += 1
                                f_rb = tokens[current_token][1]
                                # print(f"Function: {type}  {name} {f_lp} {function_parameter} {f_rp} {f_lb} {function_body} {f_rb}")
                                statment_block += f"\n\t\t\t\t\tFUNCTION: {type}  {name} {f_lp} {function_parameter} {f_rp} {f_lb} {function_body} {f_rb}"
                            else:
                                # print("Syntax Error: <missing '}',  function block not closed")
                                Error_list += "\nSyntax Error: <missing '}',  function block not closed"
                                # print(f"Function: {type}  {name} {f_lp} {function_parameter} {f_rp} {f_lb} {function_body}  <missing RIGHT_BRACE' >")
                                statment_block += f"\n\t\t\t\t\tFUNCTION: {type}  {name} {f_lp} {function_parameter} {f_rp} {f_lb} {function_body}  <missing RIGHT_BRACE' >"
                        else:
                            # print("Syntax Error: Functon definition   <missing '{'>")
                            Error_list += "\nSyntax Error: Functon definition   <missing '{'>"
                            # print(f"Function: {type}  {name} {f_lp} {function_parameter} <missing LEFT_BRACE>...")
                            statment_block += f"\n\t\t\t\t\tFUNCTION: {type}  {name} {f_lp} {function_parameter} <missing LEFT_BRACE>..."
                    else:
                        # print("Syntax Error: <missing '('")
                        Error_list += "\nSyntax Error: <missing '('"

                elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "ASSIGN":  # initialization
                    type = tokens[current_token][1]
                    namr = tokens[current_token + 1][1]
                    asg = tokens[current_token + 2][1]
                    current_token, express = expression(tokens, current_token + 2)
                    express_n = ''

                    if len(express) != 0:
                        if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                            s_tm = tokens[current_token][1]
                            # print(f"initialization: {type} {namr} {asg} {express} {s_tm}")
                            statment_block += f"\n\t\t\t\t\tINITIALIZATION: {type} {namr} {asg} {express} {s_tm}"
                        else:
                            # print(f"initialization: {type} {namr} {asg} {express} <missing ';'>")
                            statment_block += f"\n\t\t\t\t\tINITIALIZATION: {type} {namr} {asg} {express} <missing ';'>"
                            # print(f"Syntax Error: missing statement terminator")
                            Error_list += "\nSyntax Error: missing statement terminator"
                            continue
                    else:
                        print("Syntax Error: variable Initialization error, no value was assigned ")
                        if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                            s_tm = tokens[current_token][1]
                            # print(f"initialization: {type} {namr} {asg} ~{None}~ {s_tm}")
                            statment_block += f"\n\t\t\t\t\tINITIALIZATION: {type} {namr} {asg} ~{None}~ {s_tm}"
                        else:
                            # print(f"initialization: {type} {namr} {asg} ~{None}~ <missing ';'>")
                            statment_block += f"\n\t\t\t\t\tINITIALIZATION: {type} {namr} {asg} ~{None}~ <missing ';'>"
                            # print(f"Syntax Error: missing statement terminator")
                            Error_list += "\nSyntax Error: missing statement terminator"
                            continue
                else:
                    # print(f"Declaration: {type}  {name} <missing ';' >")
                    statment_block += f"\n\t\t\t\t\tDECLARATION: {type}  {name} <missing ';' >"
                    # print(" Syntax Error : unterminated statement ", tokens[current_token + 1][0])
                    Error_list += "\nSyntax Error : unterminated statement  " + tokens[current_token + 1][0]
                    current_token += 1
            else:
                # print(" Syntax Error : expected token IDENTIFIER")
                Error_list += "\nSyntax Error : expected token IDENTIFIER"

        elif current_token  < len(tokens) and tokens[current_token][0] == 'IF':
            gm = ""
            else_if = 0
            while True:
                if_key_word = tokens[current_token][1]
                gm += if_key_word + ' '
                if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_PAREN':
                    l_p = tokens[current_token + 1][1]
                    gm += l_p + ' '
                    current_token, if_condition = condition_statement_RFC(tokens, current_token + 1)
                    gm += if_condition + ' '
                    if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_PAREN':
                        r_p = tokens[current_token][1]
                        gm += r_p + ' '
                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_BRACE':
                            block_track += 1
                            l_b = tokens[current_token + 1][1]
                            gm += l_b + ' '
                            current_token, if_statment_body = statments(tokens, current_token + 1)
                            gm += if_statment_body + ' '
                            if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_BRACE':
                                block_track -= 1
                                r_b = tokens[current_token][1]
                                gm += r_b + ' '
                                # current_token += 2
                                if current_token == len(tokens):
                                    # print(f"IF statement : {gm}")
                                    statment_block += f"\n\t\t\t\t\tIF STATEMENT : {gm}"
                                    break
                                elif tokens[current_token + 1][0] != 'ELSE':
                                    # print(f"IF statement : {gm}")
                                    statment_block += f"\n\t\t\t\t\tIF STATEMENT : {gm}"
                                    break
                                else:
                                    if tokens[current_token + 1][0] == 'ELSE' and tokens[current_token + 2][0] != 'IF':
                                        if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'LEFT_BRACE':
                                            block_track += 1
                                            else_key = tokens[current_token + 1][1]
                                            gm += else_key + ' '
                                            e_lb = tokens[current_token + 2][1]
                                            gm += e_lb + ' '
                                            current_token, else_statment_body = statments(tokens, current_token + 2)
                                            gm += else_statment_body + ' '
                                            if tokens[current_token][0] == 'RIGHT_BRACE':
                                                block_track -= 1
                                                e_rb = tokens[current_token][1]
                                                gm += e_rb + ' '
                                                if else_if == 0:
                                                    # print(f"IF-ELSE statement: {gm}")
                                                    statment_block += f"\n\t\t\t\t\tIF-ELSE STATEMENT: {gm}"
                                                else:
                                                    # print(f"IF-ELSE-IF statement: {gm}")
                                                    statment_block += f"\n\t\t\t\t\tIF-ELSE STATEMENT: {gm}"
                                                break
                                            else:
                                                # print(f"IF statement: {gm} < missing 'RIGHT_BRACE'>")
                                                statment_block += f"\n\t\t\t\t\tIF STATEMENT: {gm} < missing 'RIGHT_BRACE'>"
                                                # print("Syntax Error: incomplete else statment  missing <RIGHT_BRACE>")
                                                Error_list += "\nSyntax Error: incomplete else statment  missing <RIGHT_BRACE>"
                                                break
                                        else:
                                            else_key = tokens[current_token + 1][1]
                                            gm += else_key + ' '
                                            # print(f"IF statement: {gm} < missing 'LEFT_BRACE' 'RIGHT_BRACE'>")
                                            statment_block += f"\n\t\t\t\t\tIF STATEMENT: {gm} < missing 'LEFT_BRACE' 'RIGHT_BRACE'>"
                                            # print("Syntax Error: incomplete else statment ")
                                            Error_list += "\nSyntax Error: incomplete else statment "
                                            break
                                    elif tokens[current_token + 1][0] == 'ELSE' and tokens[current_token + 2][0] == 'IF':
                                        else_key = tokens[current_token + 1][1]
                                        gm += else_key + " "
                                        else_if += 1
                                        current_token += 2
                            else:
                                # print(" Syntax Error : if-statment expected  RIGHT_BRACE   ")
                                Error_list += "\nSyntax Error : if-statment expected  RIGHT_BRACE   "
                                # (f"IF statement: {gm} < missing 'RIGHT_BRACE'>")
                                statment_block += f"\n\t\t\t\t\tIF STATEMENT: {gm} < missing 'RIGHT_BRACE'>"
                                break
                        else:
                            # print(" Syntax Error : if-statment expected  LEFT_BRACE  < missing '{'> ")
                            Error_list += "\nSyntax Error : if-statment expected  LEFT_BRACE  < missing '{'> "
                            # print(f"IF statement: {gm} ... <statement incomplete> ...")
                            statment_block += f"\n\t\t\t\t\tIF STATEMENT: {gm} ... <statement incomplete> ..."
                            break
                    else:
                        # print(" Syntax Error : if-statment expected  LEFT_PAREN  < missing ')'> ")
                        Error_list += "\nSyntax Error : if-statment expected  LEFT_PAREN  < missing ')'> "
                        # print(f"IF statement: {gm} ... <statement incomplete> ...")
                        statment_block += f"\n\t\t\t\t\tIF STATEMENT: {gm} ... <statement incomplete> ..."
                        break
                else:
                    # print(" Syntax Error : if-statment expected  LEFT_PAREN  < missing '{}'> ")
                    Error_list += "\nSyntax Error : if-statment expected  LEFT_PAREN  < missing '{}'> "
                    # print(f"IF statement: {gm} ... <missing LEFT_PAREN> ...")
                    statment_block += f"\n\t\t\t\t\tIF STATEMENT: {gm} ... <missing LEFT_PAREN> ..."
                    break

        elif current_token  < len(tokens) and  tokens[current_token][0] == 'WHILE':
            while_key = tokens[current_token][0]
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_PAREN':
                wh_lp = tokens[current_token + 1][1]
                current_token, condition_statment = condition_statement_RFC(tokens, current_token + 1)
                if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_PAREN':
                    wh_rp = tokens[current_token][1]
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_BRACE':
                        block_track += 1
                        wh_lb = tokens[current_token + 1][1]
                        current_token, while_body = statments(tokens, current_token + 1)
                        if tokens[current_token][0] == 'RIGHT_BRACE':
                            block_track -= 1
                            wh_rb = tokens[current_token][1]
                            wh_condition = condition_statment
                            # print(F"WHILE-STATEMENT: {while_key} {wh_lp} {wh_condition} {wh_rp} {wh_lb}  {while_body} {wh_rb}")
                            statment_block += f"\n\t\t\t\t\tWHILE-STATEMENT: {while_key} {wh_lp} {wh_condition} {wh_rp} {wh_lb} {while_body} {wh_rb}"
                        else:
                            # print(F"WHILE-STATEMENT: {while_key} {wh_lp} <missing RIGHT_BRACE>")
                            statment_block += f"\n\t\t\t\t\tWHILE-STATEMENT: {while_key} {wh_lp} <missing RIGHT_BRACE>"
                else:
                    # print(F"WHILE-STATEMENT: {while_key} {wh_lp} <error incomplete-while-statement>")
                    statment_block += f"\n\t\t\t\t\tWHILE-STATEMENT: {while_key} {wh_lp} <error incomplete-while-statement>"
            else:
                # print(F"WHILE-STATEMENT: {while_key}  <error incomplete-while-statement>")
                statment_block += f"\n\t\t\t\t\tWHILE-STATEMENT: {while_key}  <error incomplete-while-statement>"

        elif current_token  < len(tokens) and tokens[current_token][0] == 'IDENTIFIER':
            name = tokens[current_token][1]
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'ASSIGN':
                asg = tokens[current_token + 1][1]
                if (current_token + 2) < len(tokens) and (current_token + 3) < len(tokens) and tokens[current_token + 2][0] == 'IDENTIFIER' and tokens[current_token + 3][0] == 'LEFT_PAREN':  # function_assignment_call
                    f_name = tokens[current_token + 2][1]
                    l_p = tokens[current_token + 3][1]
                    f_parameter, current_token = parameter_RFC(tokens, (current_token + 3))
                    r_p = tokens[current_token][1]
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'SEMICOLON':
                        s_tm = tokens[current_token + 1][1]
                        # print(f"Function Assignment: {name} {asg} {f_name} {l_p} {f_parameter} {r_p} {s_tm}")
                        statment_block += f"\n\t\t\t\t\tFUNCTION ASSIGNMENT: {name} {asg} {f_name} {l_p} {f_parameter} {r_p} {s_tm}"
                        current_token += 1
                    else:
                        # print(f"Function Assignment: {name} {asg} {f_name} {l_p} {f_parameter} {r_p} <missing ';'>")
                        statment_block += f"\n\t\t\t\t\tFUNCTION ASSIGNMENT: {name} {asg} {f_name} {l_p} {f_parameter} {r_p} <missing ';'>"
                else:
                    current_token, express = expression(tokens, current_token + 1)
                    express_n = ''
                    if len(express) != 0:
                        if current_token < len(tokens) and tokens[current_token][0] != "SEMICOLON":
                            # print("Syntax Error: statement terminator missing")
                            Error_list += "\nSyntax Error: statement terminator missing"
                            # print(f"Variable assignment: {name} {asg} {express}  <missing ';'>")
                            statment_block += f"\n\t\t\t\t\tVARIABLE ASSIGNMENT: {name} {asg} {express}  <missing ';'>"
                        else:
                            # print(f"Variable assignment: {name} {asg} {express} {tokens[current_token][1]}")
                            statment_block += f"\n\t\t\t\t\tVARIABLE ASSIGNMENT: {name} {asg} {express} {tokens[current_token][1]}"
                    else:
                        # print("Syntax Error: variable assignment error, no value was assigned ")
                        Error_list += "\nSyntax Error: variable assignment error, no value was assigned "
                        if tokens[current_token][0] == "SEMICOLON":
                            s_tm = tokens[current_token][1]
                            # print(f"Variable assignment: {name} {asg} {None} {s_tm}")
                            statment_block += f"\n\t\t\t\t\tVARIABLE ASSIGNMENT: {name} {asg} {None} {s_tm}"


            elif tokens[current_token + 1][0] == 'LEFT_PAREN':
                l_p = tokens[current_token + 1][1]
                function_parameter, pos = parameter_RFC(tokens, (current_token + 1))
                current_token = pos
                if tokens[current_token][0] == "RIGHT_PAREN":
                    f_rp = tokens[current_token][1]
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "SEMICOLON":
                        tm = tokens[current_token + 1][1]
                        # print(f"Function Call: {name} {l_p} {function_parameter} {f_rp} {tm}")
                        statment_block += f"\n\t\t\t\t\tFUNCTION CALL: {name} {l_p} {function_parameter} {f_rp} {tm}"
                        current_token += 1
                    else:
                        # print(f"Function Call: {name} {l_p} {function_parameter} {f_rp}  < missing ';'>")
                        statment_block += f"\n\t\t\t\t\tFUNCTION CALL: {name} {l_p} {function_parameter} {f_rp}  < missing ';'>"
                        # print('Syntax Error: function call missing statement terminator')
                        Error_list += "\nSyntax Error: function call missing statement terminator"

        elif current_token  < len(tokens) and tokens[current_token][1] == 'return':
            current_token, express = expression(tokens, current_token)
            express_n = ''
            if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                if len(express) != 0:
                    # print("RETURN-STATMENT  : return ", express, tokens[current_token][1])
                    statment_block += f"\n\t\t\t\t\tRETURN-STATEMENT  : return " + express + tokens[current_token][1]
                else:
                    # print("RETURN-STATMENT  : return  <error 'no value'>", tokens[current_token][1])
                    statment_block += f"\n\t\t\t\t\tRETURN-STATEMENT  : return  <error 'no value'> " + tokens[current_token][1]
                    # print("Syntax error: no return value was specified")
                    Error_list += "\nSyntax error: no return value was specified"
            else:
                if len(express_n) != 0:
                    # print(f"RETURN-STATMENT  : return {express} < missing ';'>")
                    statment_block += f"\n\t\t\t\t\tRETURN-STATEMENT  : return {express} < missing ';'>"
                    # print("Syntax error: no return value was specified")
                    Error_list += "\nSyntax error: no return value was specified"
                else:
                    print(f"RETURN-STATEMENT  : return  <missing return-value>  <missing ';'>")
                    # print("Syntax error: no return value was specified, missing statement terminator for return statement")
                    Error_list += "\nSyntax error: no return value was specified, missing statement terminator for return statement"


        else:
            if current_token < len(tokens):
                # print("Syntax Error  : ", tokens[current_token])
                try:
                    Error_list += f"\nSyntax Error : '{tokens[current_token][1]}'  at line  {tokens[current_token][2]}"
                except:
                    Error_list += f"\nSyntax Error : 'statement incomplete at line "
                    print()
            else:
                break

    return current_token, statment_block


def expression(tokens, position):
    global express_n
    express_n += ''
    current_token = position + 1
    while current_token < len(tokens):
        token_type, token_value, line_number = tokens[current_token]
        if token_type == 'IDENTIFIER' and tokens[current_token+1] != 'IDENTIFIER':
            print(tokens[current_token], tokens[current_token+1])
            express_n += token_value + ' '
        elif token_type == 'INTEGER':
            express_n += token_value + ' '
        elif token_type == 'CHAR':
            express_n += token_value + ' '
        elif token_type == 'STRING':
            express_n += token_value + ' '
        elif token_type == 'BOOLEAN':
            express_n += token_value + ' '
        elif token_type == 'FLOATING_POINT':
            express_n += token_value + ' '
        elif token_type == 'LEFT_PAREN':
            express_n += token_value + ' '
            expression(tokens, current_token)  # Handle nested expressions recursively
            while tokens[current_token][0] != 'RIGHT_PAREN':  # Skip to the end of the nested expression
                current_token += 1
            express_n += tokens[current_token][1] + ' '
        elif token_type == 'PLUS' or token_type == "MINUS" or token_type == "MULTIPLY" or token_type == "DIVIDE" or token_type == "MODULUS":
            express_n += token_value + ' '
        elif token_type == 'SEMICOLON' or token_type == 'RIGHT_PAREN' or token_type == 'EQUAL' or token_type == 'NOT_EQUAL' or token_type == 'LESS_THAN' or token_type == 'GREATER_THAN' or token_type == 'LESS_THAN_EQUAL' or token_type == 'GREATER_THAN_EQUAL':
            break
        else:
            print(f"Syntax error -- Expression Error Cause:  {tokens[current_token][1]}")
            break
        current_token += 1
    return current_token, express_n


def parse_program(tokens, postion):
    global express_n
    current_token = postion
    while current_token < len(tokens):
        if tokens[current_token][0] == "INCLUDE_ID":
            if tokens[current_token + 1][0] == 'INCLUDE_DIRECTIVE':
                # handle include list
                include_directive = tokens[current_token][1] + ' ' + tokens[current_token + 1][1]
                current_token += 1
                print(f"INCLUDE-LIST: {include_directive}")
            else:
                print(f"SYNTAX ERROR: INCLUDE_DIRECTIVE: '{tokens[current_token + 1][1]}' at line {tokens[current_token + 1][2]}")
                current_token += 1

        elif tokens[current_token][0] == "KEYWORD" and tokens[current_token][1] != 'return':
            type = tokens[current_token][1]
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "IDENTIFIER":
                name = tokens[current_token + 1][1]
                if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "SEMICOLON":  # handle declaration
                    terminator = tokens[current_token + 2][1]
                    print(f"DECLARATION {type} {name} {terminator}")
                    current_token += 2

                elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "LEFT_PAREN":  # handle functions
                    f_lp = tokens[current_token + 2][1]
                    function_parameter, pos = parameter_RFC(tokens, (current_token + 2))
                    current_token = pos
                    if current_token < len(tokens) and tokens[current_token][0] == "RIGHT_PAREN":
                        f_rp = tokens[current_token][1]
                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "LEFT_BRACE":
                            f_lb = tokens[current_token + 1][1]
                            current_token, function_body = statments(tokens, current_token + 1)
                            # call function body
                            if current_token < len(tokens) and tokens[current_token][0] == "RIGHT_BRACE":
                                f_rb = tokens[current_token][1]
                                print(f"FUNCTION: {type}  {name} {f_lp} {function_parameter} {f_rp} {f_lb} {function_body} {f_rb}")
                            else:
                                print("Syntax Error: <missing '}',  function block not closed at line ", tokens[current_token-1][2])
                                print(f"FUNCTION: {type}  {name} {f_lp} {function_parameter} {f_rp} {f_lb} {function_body}  <missing RIGHT_BRACE' >")
                        else:
                            print("Syntax Error: Functon definition   <missing '{'> at line ", tokens[current_token][2])
                            print(f"FUNCTION: {type}  {name} {f_lp} {function_parameter} <missing LEFT_BRACE>...")
                    else:
                        print("Syntax Error: <missing '('")

                elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "ASSIGN":  # initialization
                    type = tokens[current_token][1]
                    namr = tokens[current_token + 1][1]
                    asg = tokens[current_token + 2][1]
                    current_token, express = expression(tokens, current_token + 2)
                    express_n = ''

                    if len(express) != 0:
                        if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                            s_tm = tokens[current_token][1]
                            print(f"INITIALIZATION: {type} {namr} {asg} {express} {s_tm}")
                        else:
                            print(f"INITIALIZATION: {type} {namr} {asg} {express} <missing ';'>")
                            print(f"Syntax Error: missing statement terminator at line {tokens[current_token-1][2]} after '{tokens[current_token-1][1]}'" )
                            continue
                    else:
                        print(f"Syntax Error: variable Initialization error, no value was assigned at line {tokens[current_token][2]} ")
                        if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                            s_tm = tokens[current_token][1]
                            print(f"INITIALIZATION: {type} {namr} {asg} ~{None}~ {s_tm}")
                        else:
                            print(f"INITIALIZATION: {type} {namr} {asg} ~{None}~ <missing ';'>")
                            print(f"Syntax Error: missing statement terminator at line {tokens[current_token][2]}")
                            continue
                else:
                    print(f"DECLARATION: {type}  {name} <missing ';' >")
                    print(f"Syntax Error : unterminated statement for '{tokens[current_token + 1][1]}' at line {tokens[current_token + 1][2]} ")
                    current_token += 1
            else:
                print("Syntax Error : expected token 'IDENTIFIER' goten at line  ",  tokens[current_token][2])

        elif tokens[current_token][0] == 'IF':
            gm = ""
            else_if = 0
            while True:
                if_key_word = tokens[current_token][1]
                gm += if_key_word + ' '
                if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_PAREN':
                    l_p = tokens[current_token + 1][1]
                    gm += l_p + ' '
                    current_token, if_condition = condition_statement_RFC(tokens, current_token + 1)
                    gm += if_condition + ' '
                    if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_PAREN':
                        r_p = tokens[current_token][1]
                        gm += r_p + ' '
                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_BRACE':
                            l_b = tokens[current_token + 1][1]
                            gm += l_b + ' '
                            current_token, if_statment_body = statments(tokens, current_token + 1)

                            gm += if_statment_body + ' '
                            if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_BRACE':
                                r_b = tokens[current_token][1]
                                gm += r_b + ' '
                                # current_token += 2
                                if current_token == len(tokens):
                                    print(f"IF STATEMENT {gm}")
                                    break
                                elif (current_token + 1) >= len(tokens) :
                                    print(f"IF STATEMENT: {gm}")
                                    break
                                elif tokens[current_token + 1][0] != 'ELSE':
                                    print(f"IF STATEMENT: {gm}")
                                    break
                                else:
                                    if tokens[current_token + 1][0] == 'ELSE' and tokens[current_token + 2][0] != 'IF':
                                        if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'LEFT_BRACE':
                                            else_key = tokens[current_token + 1][1]
                                            gm += else_key + ' '
                                            e_lb = tokens[current_token + 2][1]
                                            gm += e_lb + ' '
                                            current_token, else_statment_body = statments(tokens, current_token + 2)
                                            gm += else_statment_body + ' '
                                            if tokens[current_token][0] == 'RIGHT_BRACE':
                                                e_rb = tokens[current_token][1]
                                                gm += e_rb + ' '
                                                if else_if == 0:
                                                    print(f"IF-ELSE STATEMENT: {gm}")

                                                else:
                                                    print(f"IF-ELSE-IF STATEMENT: {gm}")

                                                break
                                            else:
                                                print(f"IF-STATEMENT: {gm} < missing 'RIGHT_BRACE'>")
                                                print("Syntax Error: incomplete else statment  missing <RIGHT_BRACE>")
                                                break
                                        else:
                                            else_key = tokens[current_token + 1][1]
                                            gm += else_key + ' '
                                            print(f"IF statement: {gm} < missing 'LEFT_BRACE' 'RIGHT_BRACE'>")
                                            print("Syntax Error: incomplete else statment ")
                                            break

                                    elif tokens[current_token + 1][0] == 'ELSE' and tokens[current_token + 2][0] == 'IF':
                                        else_key = tokens[current_token + 1][1]
                                        gm += else_key + " "
                                        else_if += 1
                                        current_token += 2
                            else:
                                print(" Syntax Error : if-statement expected  RIGHT_BRACE  at line  ", tokens[current_token-1][2] )
                                print(f"IF STATEMENT: {gm} < missing 'RIGHT_BRACE'>")
                                break
                        else:
                            print(" Syntax Error : if-statement expected  LEFT_BRACE  < missing '{'>  at line  ", tokens[current_token-1][2])
                            print(f"IF STATEMENT: {gm} ... <statement incomplete> ...")
                            break
                    else:
                        print(" Syntax Error : if-statement expected  LEFT_PAREN  < missing ')'> at line  ", tokens[current_token-1][2])
                        print(f"IF STATEMENT: {gm} ... <statement incomplete> ...")
                        break
                else:

                    print(" Syntax Error : if-statment expected  LEFT_PAREN  < missing '{}'>  at line  ", tokens[current_token-1][2])
                    print(f"IF STATEMENT: {gm} ... <missing LEFT_PAREN> ...")
                    break

        elif tokens[current_token][0] == 'WHILE':
            while_key = tokens[current_token][0]
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_PAREN':
                wh_lp = tokens[current_token + 1][1]
                current_token, condition_statment = condition_statement_RFC(tokens, current_token + 1)
                if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_PAREN':
                    wh_rp = tokens[current_token][1]
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_BRACE':
                        wh_lb = tokens[current_token + 1][1]
                        current_token, while_body = statments(tokens, current_token + 1)
                        if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_BRACE':
                            wh_rb = tokens[current_token][1]
                            print(F"WHILE-STATEMENT: {while_key} {wh_lp} {condition_statment} {wh_rp} {wh_lb}  {while_body} {wh_rb}")
                        else:
                            print(F"WHILE-STATEMENT: {while_key} {wh_lp} {condition_statment} {wh_rp} {wh_lb}  {while_body} <missing RIGHT_BRACE>")
                else:
                    print(F"WHILE-STATEMENT: {while_key} {wh_lp} <error incomplete-while-statement> <missing ')'...>  at line ", tokens[current_token-1][2])
            else:
                print(F"WHILE-STATEMENT: {while_key}  <error incomplete-while-statement> at line ", tokens[current_token][2] )

        elif tokens[current_token][0] == 'IDENTIFIER':
            name = tokens[current_token][1]
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'ASSIGN':
                asg = tokens[current_token + 1][1]
                if (current_token + 2) < len(tokens) and (current_token + 3) < len(tokens) and tokens[current_token + 2][0] == 'IDENTIFIER' and tokens[current_token + 3][0] == 'LEFT_PAREN':  # function_assignment_call
                    f_name = tokens[current_token + 2][1]
                    l_p = tokens[current_token + 3][1]
                    f_parameter, current_token = parameter_RFC(tokens, (current_token + 3))
                    r_p = tokens[current_token][1]

                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'SEMICOLON':
                        s_tm = tokens[current_token + 1][1]
                        print(f"FUNCTION ASSIGNMENT: {name} {asg} {f_name} {l_p} {f_parameter} {r_p} {s_tm}")
                        current_token += 1
                    else:
                        print(f"FUNCTION ASSIGNMENT: {name} {asg} {f_name} {l_p} {f_parameter} {r_p} <missing ';'>")
                else:
                    current_token, express = expression(tokens, current_token + 1)
                    express_n = ''
                    if len(express) != 0:
                        if current_token < len(tokens) and tokens[current_token][0] != "SEMICOLON":
                            print("Syntax Error: statement terminator missing")
                            print(f"VARIABLE ASSIGNMENT2: {name} {asg} {express}  <missing ';'>")
                        elif current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                            print(f"VARIABLE ASSIGNMENT: {name} {asg} {express} {tokens[current_token][1]}")
                        else:
                            print(f"VARIABLE ASSIGNMENT1: {name} {asg} {express}  <missing ';'>")
                    else:
                        print("Syntax Error: variable assignment error, no value was assigned ", {tokens[current_token-1][2]} )
                        if tokens[current_token][0] == "SEMICOLON":
                            s_tm = tokens[current_token][1]
                            print(f"VARIABLE ASSIGNMENT: {name} {asg} {None} {s_tm}")

            elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_PAREN':
                l_p = tokens[current_token + 1][1]
                function_parameter, pos = parameter_RFC(tokens, (current_token + 1))
                current_token = pos
                if tokens[current_token][0] == "RIGHT_PAREN":
                    f_rp = tokens[current_token][1]
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "SEMICOLON":
                        tm = tokens[current_token + 1][1]
                        print(f"FUNCTION CALL: {name} {l_p} {function_parameter} {f_rp} {tm}")
                        current_token += 1
                    else:
                        print(f"FUNCTION CALL ed: {name} {l_p} {function_parameter} {f_rp}  < missing ';'>")
                        print('Syntax Error: function call missing statement terminator')

        elif tokens[current_token][1] == 'return':
            current_token, express = expression(tokens, current_token)
            express_n = ''
            if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                if len(express) != 0:
                    print("RETURN-STATEMENT  : return ", express, tokens[current_token][1])
                else:
                    print("RETURN-STATEMENT  : return  <error 'no value'>", tokens[current_token][1])
                    print("Syntax error: no return value was specified")
            else:
                if len(express_n) != 0:
                    print(f"RETURN-STATEMENT  : return {express} < missing ';'>")
                    print("Syntax error: no return value was specified")
                else:
                    print(f"RETURN-STATEMENT  : return  <missing return-value>  <missing ';'>")
                    print("Syntax error: no return value was specified, missing statement terminator for return statement")
        else:
            print(f"Syntax Error : '{tokens[current_token][1]}'  at line  {tokens[current_token][2]}", )
        current_token += 1


start_run_time_time = time.time()  # Record the Start run time-time of Syntax_analyzer
print("\n\n======================================== parser output == ====================================== \n\n")
parse_program(tokens, 0)   # calling the parser function and passing token list
End_run_time_time = time.time()  # Record the End run time-time of lexical_analyzer
Program_Run_time = End_run_time_time - start_run_time_time  # Calculate the elapsed time (run time of lexical_analyzer function)
print("\n\n================================================================================ \n\n")
print(f"\nParser Program Runtime  :  {Program_Run_time} seconds")

start_run_time_time = time.time()  # Record the Start run time-time of lexical_analyzer


print(Error_list)
