import lexical_Analyzer  # importing scanner source file for token list
import time  # for measuring 'parser' run time

tokens = lexical_Analyzer.lexical_analyzer('program.c')
Error_list = ""  # keep store track of syntax errors generated
express_n = ""  # keep store of expression statments  errors generated
print("\n\n")
parser_tree = []


def parameter_RFC(token, current_token):
    global Error_list
    node = []
    parame = ''  # keep store parameters that are found
    current_token += 1
    i = 0
    if current_token < len(tokens):
        while token[current_token][0] != 'RIGHT_PAREN':
            if token[current_token][0] == 'KEYWORD':
                if token[current_token + 1][0] == 'IDENTIFIER':
                    parame += token[current_token][1] + ' ' + token[current_token + 1][1] + ' '
                    node.append((("type_specifier", f'{token[current_token][1]}'), ("IDENTIFIER", f"{token[current_token + 1][1]}")))

                    current_token += 1
                    if token[current_token + 1][0] == 'COMMA':
                        if token[current_token + 2][0] != 'RIGHT_PAREN':
                            parame += token[current_token + 1][1] + ' '
                            current_token += 1
                        elif token[current_token + 2][0] == 'RIGHT_PAREN':
                            parame += token[current_token + 1][1] + ' ' + " <remove ','> "
                            current_token += 1

            elif token[current_token][0] == 'IDENTIFIER':
                parame += token[current_token][1] + ' '
                node.append(("IDENTIFIER", f"{token[current_token][1]}"))
                if token[current_token + 1][0] == 'COMMA':
                    if token[current_token + 2][0] != 'RIGHT_PAREN':
                        parame += token[current_token + 1][1] + ' '
                        current_token += 1
                    elif token[current_token + 2][0] == 'RIGHT_PAREN':
                        parame += token[current_token + 1][1] + ' ' + " <remove ','> "
                        current_token += 1
            else:
                print()
                Error_list += f"\nSyntax Error: illegal function parameter definition at line {token[current_token][2]}"
                parame += "<illegal-character>" + ' '

            current_token += 1
            i += 1
    return parame, current_token, node


def condition_statement_RFC(tokens, position):
    global express_n, Error_list
    node = []
    condition_statment = ''  # store condition statements
    current_token = position
    current_token, left_operand, exp_node_l = expression(tokens, current_token)
    condition_statment += left_operand
    node.append(tuple(exp_node_l))
    express_n = ''
    if current_token < len(tokens) and (tokens[current_token][0] == 'EQUAL' or tokens[current_token][0] == 'NOT_EQUAL' or tokens[current_token][0] == 'LESS_THAN' or tokens[current_token][0] == 'GREATER_THAN' or tokens[current_token][0] == 'LESS_THAN_EQUAL' or tokens[current_token][0] == 'GREATER_THAN_EQUAL'):
        conditional_operator = tokens[current_token][1]
        condition_statment += " " + conditional_operator
        current_token, right_operand, exp_node_r= expression(tokens, current_token)
        if len(exp_node_r) != 0:
            node.pop()
            condition_statment += " " + right_operand
            node.append(tuple(exp_node_l))
            node.append(conditional_operator)
            node.append(tuple(exp_node_r))
            express_n = ''
        else:
            Error_list += f"\nSyntax Error: Condition statement incomplete at line {tokens[current_token][2]}"
    if len(condition_statment) == 0:
        Error_list += f"\nSyntax Error: Condition statement not provided at line {tokens[current_token][2]}"
    return current_token, condition_statment, node


def statments(token, postion):  # statement: (declaration | initializing | function_call | assignment | if_statement | while_statement | return_statement)*;
    global express_n, Error_list
    node = []
    statment_block = ''  # store statements in block
    block_track = 1
    current_token = postion

    while block_track != 0:
        current_token += 1
        if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_BRACE':
            statment_block += '\n\t\t\t\t\t'
            block_track -= 1
        elif current_token < len(tokens) and tokens[current_token][0] == "KEYWORD" and tokens[current_token][1] != 'return':
            type_specifer = tokens[current_token][1]
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "IDENTIFIER":
                name = tokens[current_token + 1][1]
                if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "SEMICOLON":  # handle declaration
                    terminator = tokens[current_token + 2][1]
                    # print(f"Declaration {type} {name} {terminator}")
                    statment_block += f"\n\t\t\t\t\tDECLARATION:   {type_specifer} {name} {terminator}"
                    node.append(("DECLARATION", ("type_specifer", f"{type_specifer}"), ('IDENTIFIER', F"{name}")))
                    current_token += 2

                elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "LEFT_PAREN":  # handle functions
                    f_lp = tokens[current_token + 2][1]
                    function_parameter, pos, param_node = parameter_RFC(tokens, (current_token + 2))
                    current_token = pos
                    if current_token < len(tokens) and tokens[current_token][0] == "RIGHT_PAREN":
                        f_rp = tokens[current_token][1]
                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "LEFT_BRACE":
                            block_track -= 1
                            f_lb = tokens[current_token + 1][1]
                            current_token, function_body, child_node = statments(tokens, current_token + 1)
                            if current_token < len(tokens) and tokens[current_token][0] == "RIGHT_BRACE":
                                block_track += 1
                                f_rb = tokens[current_token][1]
                                statment_block += f"\n\t\t\t\t\tFUNCTION: {type_specifer}  {name} {f_lp} {function_parameter} {f_rp} {f_lb} {function_body} {f_rb}"
                                node.append(('FUNCTION', ("type_specifier", f"{type_specifer}"), ("function_name", f"{name}"), ("function_parameter", f"{function_parameter}"), ("function_body", tuple(child_node))))
                            else:
                                Error_list += "\nSyntax Error: <missing '}',  function block not closed"
                                statment_block += f"\n\t\t\t\t\tFUNCTION: {type_specifer}  {name} {f_lp} {function_parameter} {f_rp} {f_lb} {function_body}  \n\t\t\t\t\t<missing RIGHT_BRACE' >"
                                node.append(('FUNCTION', ("type_specifier", f"{type_specifer}"), ("function_name", f"{name}"), ("function_parameter", tuple(param_node)), ("function_body", tuple(child_node))))
                        else:
                            Error_list += "\nSyntax Error: <missing '}',  function block not closed at line " + tokens[current_token - 1][2]
                            statment_block += f"\n\t\t\t\t\tFUNCTION: {type_specifer}  {name} {f_lp} {function_parameter} <missing LEFT_BRACE>..."
                    else:
                        statment_block += f"\n\t\t\t\t\tFUNCTION: {type_specifer}  {name} {f_lp} {function_parameter} <missing ')'>..."
                        Error_list += "\nSyntax Error: incomplete function statment, <missing ')' '{' ...'}' at line ", tokens[current_token - 1][2]

                elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "ASSIGN":  # initialization
                    type_specifer = tokens[current_token][1]
                    namr = tokens[current_token + 1][1]
                    asg = tokens[current_token + 2][1]
                    current_token, express, exp_node = expression(tokens, current_token + 2)
                    express_n = ''

                    if len(express) != 0:
                        if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                            s_tm = tokens[current_token][1]
                            statment_block += f"\n\t\t\t\t\tINITIALIZATION:  {type_specifer} {namr} {asg} {express} {s_tm}"
                            node.append(('INITIALIZATION', ("type_specifier", f"{type_specifer}"), ("IDENTIFIER", f"{namr}"), ("expression", tuple(exp_node))))
                        else:
                            statment_block += f"\n\t\t\t\t\tINITIALIZATION: {type_specifer} {namr} {asg} {express} <missing ';'>"
                            node.append(('INITIALIZATION', ("type_specifier", f"{type_specifer}"), ("IDENTIFIER", f"{namr}"), ("expression", tuple(exp_node))))
                            Error_list += f"\nSyntax Error: missing statement terminator at line {tokens[current_token - 1][2]} after '{tokens[current_token - 1][1]}'"
                            continue
                    else:
                        Error_list += f"\nSyntax Error: variable Initialization error, no value was assigned at line {tokens[current_token][2]} "
                        if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                            s_tm = tokens[current_token][1]
                            statment_block += f"\n\t\t\t\t\tINITIALIZATION: {type_specifer} {namr} {asg} ~{None}~ {s_tm}"
                        else:
                            statment_block += f"\n\t\t\t\t\tINITIALIZATION: {type_specifer} {namr} {asg} ~{None}~ <missing ';'>"
                            Error_list += f"\nSyntax Error: missing statement terminator at line {tokens[current_token][2]}"
                            continue
                else:
                    # print(f"Declaration: {type}  {name} <missing ';' >")
                    statment_block += f"\n\t\t\t\t\tDECLARATION: {type_specifer}  {name} <missing ';' >"
                    # print(" Syntax Error : unterminated statement ", tokens[current_token + 1][0])
                    Error_list += f"\nSyntax Error : unterminated statement for '{tokens[current_token + 1][1]}' at line {tokens[current_token + 1][2]} "
                    current_token += 1
            else:
                # print(" Syntax Error : expected token IDENTIFIER")
                Error_list += "Syntax Error : expected token 'IDENTIFIER' goten at line  ", tokens[current_token][2]

        elif current_token < len(tokens) and tokens[current_token][0] == 'IF':
            if_node = []
            gm = ""
            else_if = 0
            while True:
                if_key_word = tokens[current_token][1]
                gm += if_key_word + ' '
                if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_PAREN':
                    l_p = tokens[current_token + 1][1]
                    gm += l_p + ' '
                    current_token, if_condition, con_node = condition_statement_RFC(tokens, current_token + 1)
                    gm += if_condition + ' '
                    if else_if == 0:
                        if_node.append(('if_condition', tuple(con_node)))
                    else:
                        if_node.append(('elif_condition', tuple(con_node)))
                    if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_PAREN':
                        r_p = tokens[current_token][1]
                        gm += r_p + ' '
                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_BRACE':
                            block_track += 1
                            l_b = tokens[current_token + 1][1]
                            gm += l_b + ' '
                            current_token, if_statment_body, stat_node = statments(tokens, current_token + 1)
                            if else_if == 0:
                                if_node.append(('if_body', tuple(stat_node)))
                            else:
                                if_node.append(('elif_body', tuple(stat_node)))
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
                                            current_token, else_statment_body, els_node = statments(tokens, current_token + 2)
                                            if_node.append(('else_body', tuple(els_node)))
                                            gm += else_statment_body + ' '
                                            if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_BRACE':
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
                                                Error_list += "\nSyntax Error: incomplete else statment  missing <RIGHT_BRACE> at line ", tokens[current_token - 1][2]
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
                                Error_list += "\nSyntax Error : if-statement expected  RIGHT_BRACE  at line  " + tokens[current_token - 1][2]
                                # (f"IF statement: {gm} < missing 'RIGHT_BRACE'>")
                                statment_block += f"\n\t\t\t\t\tIF STATEMENT: {gm} < missing 'RIGHT_BRACE'>"
                                break
                        else:
                            # print(" Syntax Error : if-statment expected  LEFT_BRACE  < missing '{'> ")
                            Error_list += "\nSyntax Error : if-statement expected  LEFT_BRACE   < missing '{'>  at line  " + tokens[current_token - 1][2]
                            # print(f"IF statement: {gm} ... <statement incomplete> ...")
                            statment_block += f"\n\t\t\t\t\tIF STATEMENT: {gm} ... <statement incomplete> ..."
                            break
                    else:
                        # print(" Syntax Error : if-statment expected  LEFT_PAREN  < missing ')'> ")
                        Error_list += "\nSyntax Error : if-statement expected  LEFT_PAREN   < missing ')'> at line  " + tokens[current_token - 1][2]
                        # print(f"IF statement: {gm} ... <statement incomplete> ...")
                        statment_block += f"\n\t\t\t\t\tIF STATEMENT: {gm} ... <statement incomplete> ..."
                        break
                else:
                    # print(" Syntax Error : if-statment expected  LEFT_PAREN  < missing '{}'> ")
                    Error_list += "\nSyntax Error : if-statment expected  LEFT_PAREN  < missing '{}'>  at line  " + tokens[current_token - 1][2]
                    # print(f"IF statement: {gm} ... <missing LEFT_PAREN> ...")
                    statment_block += f"\n\t\t\t\t\tIF STATEMENT: {gm} ... <missing LEFT_PAREN> ..."
                    break
            node.append(('if_statment', tuple(if_node)))

        elif current_token < len(tokens) and tokens[current_token][0] == 'WHILE':
            while_key = tokens[current_token][0]
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_PAREN':
                wh_lp = tokens[current_token + 1][1]
                current_token, condition_statment, con_node = condition_statement_RFC(tokens, current_token + 1)
                if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_PAREN':
                    wh_rp = tokens[current_token][1]
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_BRACE':
                        block_track += 1
                        wh_lb = tokens[current_token + 1][1]
                        current_token, while_body, child_node = statments(tokens, current_token + 1)
                        if tokens[current_token][0] == 'RIGHT_BRACE':
                            block_track -= 1
                            wh_rb = tokens[current_token][1]
                            wh_condition = condition_statment
                            # print(F"WHILE-STATEMENT: {while_key} {wh_lp} {wh_condition} {wh_rp} {wh_lb}  {while_body} {wh_rb}")
                            statment_block += f"\n\t\t\t\t\tWHILE-STATEMENT: {while_key} {wh_lp} {wh_condition} {wh_rp} {wh_lb} {while_body} {wh_rb}"
                            node.append(('WHILE-STATEMENT', ('condition', tuple(con_node)), ("while_body", tuple(child_node))))
                        else:
                            # print(F"WHILE-STATEMENT: {while_key} {wh_lp} <missing RIGHT_BRACE>")
                            statment_block += f"\n\t\t\t\t\tWHILE-STATEMENT: {while_key} {wh_lp} {condition_statment} {wh_rp} {wh_lb}  {while_body} <missing RIGHT_BRACE>"
                            node.append(('WHILE-STATEMENT', ('condition', f'{condition_statment}'), ("while_body", f"{while_body}")))
                            Error_list += "\nSyntax Error: missing '}' at line ", tokens[current_token - 1][2]
                else:
                    # print(F"WHILE-STATEMENT: {while_key} {wh_lp} <error incomplete-while-statement>")
                    statment_block += f"\n\t\t\t\t\tWHILE-STATEMENT: {while_key} {wh_lp} <error incomplete-while-statement>"
            else:
                # print(F"WHILE-STATEMENT: {while_key}  <error incomplete-while-statement>")
                statment_block += f"\n\t\t\t\t\tWHILE-STATEMENT: {while_key}  <error incomplete-while-statement>"
                Error_list += "\nSyntax error: while statment incomplete at line " + tokens[current_token][2]

        elif current_token < len(tokens) and tokens[current_token][0] == 'IDENTIFIER':
            name = tokens[current_token][1]
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'ASSIGN':
                asg = tokens[current_token + 1][1]
                if (current_token + 2) < len(tokens) and (current_token + 3) < len(tokens) and tokens[current_token + 2][0] == 'IDENTIFIER' and tokens[current_token + 3][0] == 'LEFT_PAREN':  # function_assignment_call
                    f_name = tokens[current_token + 2][1]
                    l_p = tokens[current_token + 3][1]
                    f_parameter, current_token, param_node = parameter_RFC(tokens, (current_token + 3))
                    r_p = tokens[current_token][1]
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'SEMICOLON':
                        s_tm = tokens[current_token + 1][1]
                        # print(f"Function Assignment: {name} {asg} {f_name} {l_p} {f_parameter} {r_p} {s_tm}")
                        statment_block += f"\n\t\t\t\t\tFUNCTION ASSIGNMENT: {name} {asg} {f_name} {l_p} {f_parameter} {r_p} {s_tm}"
                        node.append(('function_assignment', ("IDENTIFIER", f"{name}"), ("f_name", f"{f_name}"), ('param', tuple(param_node))))
                        current_token += 1
                    else:
                        # print(f"Function Assignment: {name} {asg} {f_name} {l_p} {f_parameter} {r_p} <missing ';'>")
                        statment_block += f"\n\t\t\t\t\tFUNCTION ASSIGNMENT: {name} {asg} {f_name} {l_p} {f_parameter} {r_p} <missing ';'>"
                        node.append(('function_assignment', ("IDENTIFIER", f"{name}"), ("f_name", f"{f_name}"), ('param', tuple(param_node))))
                        Error_list += "\nSyntax error: function-call-assignment  missing semicolon at line " + tokens[current_token][2]
                else:
                    current_token, express, exp_node = expression(tokens, current_token + 1)
                    express_n = ''
                    if len(express) != 0:
                        if current_token < len(tokens) and tokens[current_token][0] != "SEMICOLON":
                            # print("Syntax Error: statement terminator missing")
                            Error_list += "\nSyntax Error: statement terminator missing at line " + tokens[current_token - 1][2]
                            # print(f"Variable assignment: {name} {asg} {express}  <missing ';'>")
                            statment_block += f"\n\t\t\t\t\tVARIABLE ASSIGNMENT: {name} {asg} {express}  <missing ';'>"
                            node.append(('variable_assignment', ("IDENTIFIER", f"{name}"), ("expression", tuple(exp_node))))
                        elif current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                            # print(f"Variable assignment: {name} {asg} {express} {tokens[current_token][1]}")
                            statment_block += f"\n\t\t\t\t\tVARIABLE ASSIGNMENT: {name} {asg} {express} {tokens[current_token][1]}"
                            node.append(('variable_assignment', ("IDENTIFIER", f"{name}"), ("expression", tuple(exp_node))))
                        else:
                            statment_block += f"\n\t\t\t\t\tVARIABLE ASSIGNMENT1: {name} {asg} {express}  <missing ';'>"
                            Error_list += "\nSyntax Error: statement terminator missing at line " + tokens[current_token - 1][2]
                            node.append(('variable_assignment', ("IDENTIFIER", f"{name}"), ("expression", tuple(exp_node))))
                    else:
                        # print("Syntax Error: variable assignment error, no value was assigned ")
                        Error_list += "\nSyntax Error: variable assignment error, no value was assigned " + tokens[current_token - 1][2]
                        if tokens[current_token][0] == "SEMICOLON":
                            s_tm = tokens[current_token][1]
                            statment_block += f"\n\t\t\t\t\tVARIABLE ASSIGNMENT: {name} {asg} {None} {s_tm}"

            elif tokens[current_token + 1][0] == 'LEFT_PAREN':
                l_p = tokens[current_token + 1][1]
                function_parameter, pos, param_node = parameter_RFC(tokens, (current_token + 1))
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
                        Error_list += "\nSyntax Error: function call missing statement terminator at line " + tokens[current_token][2]

        elif current_token < len(tokens) and tokens[current_token][1] == 'return':
            current_token, express, exp_node = expression(tokens, current_token)
            express_n = ''
            if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":

                if len(express) != 0:
                    statment_block += f"\n\t\t\t\t\tRETURN-STATEMENT  : return " + express + tokens[current_token][1]
                    node.append(("return_statement", express))
                    continue
                else:
                    statment_block += f"\n\t\t\t\t\tRETURN-STATEMENT  : return  <error 'no value'> " + tokens[current_token][1]
                    Error_list += f"\nSyntax error: no return value was specified at line {tokens[current_token][2]}"
                    break
            elif current_token < len(tokens) and tokens[current_token][0] == "RIGHT_BRACE":
                if len(express) != 0:
                    statment_block += f"\n\t\t\t\t\tRETURN-STATEMENT  : return " + express
                    node.append(("return_statement", express))
                    Error_list += f"\nSyntax error: return statement missing semicolon  at line {tokens[current_token - 1][2]}"
                    break
                else:
                    statment_block += "\n\t\t\t\t\tRETURN-STATEMENT  : return  <error 'no value'> <missing ';'>"
                    Error_list += f"\nSyntax error: no return value was specified at line {tokens[current_token][2]}"
                    Error_list += f"\nSyntax error: return statement missing semicolon  at line {tokens[current_token - 1][2]}"
                    break
            else:
                if len(express) != 0:
                    statment_block += f"\n\t\t\t\t\tRETURN-STATEMENT  : return {express} < missing ';'>"
                    Error_list += f"\nSyntax error: return statement missing semicolon  at line {tokens[current_token - 1][2]}"
                else:
                    print(f"RETURN-STATEMENT  : return  <missing return-value>  <missing ';'>")
                    Error_list += f"\nSyntax error: no return value was specified, and  missing a 'statement' terminator for return statement {tokens[current_token - 1][2]}"
        else:

            if current_token < len(tokens):
                try:
                    Error_list += f"\nSyntax Error : '{tokens[current_token][1]}'  at line  {tokens[current_token][2]}"
                except:
                    Error_list += f"\nSyntax Error : 'statement incomplete at line "

            else:
                break
    return current_token, statment_block, node


def expression(tokens, position):
    global express_n, Error_list
    global express_n, node
    node = []
    temp = []
    express_n += ''
    current_token = position + 1
    while current_token < len(tokens):
        token_type, token_value, line_number = tokens[current_token]
        if token_type == 'IDENTIFIER':
            express_n += token_value + ' '
            temp.append(token_value)
        elif token_type == 'INTEGER':
            express_n += token_value + ' '
            temp.append(token_value)
        elif token_type == 'CHAR':
            express_n += token_value + ' '
            temp.append(token_value)
        elif token_type == 'STRING':
            express_n += token_value + ' '
            temp.append(token_value)
        elif token_type == 'BOOLEAN':
            express_n += token_value + ' '
            temp.append(token_value)
        elif token_type == 'FLOATING_POINT':
            express_n += token_value + ' '
            temp.append(token_value)
        elif token_type == 'LEFT_PAREN':
            express_n += token_value + ' '
            expression(tokens, current_token)  # Handle nested expressions recursively
            while tokens[current_token][0] != 'RIGHT_PAREN':  # Skip to the end of the nested expression
                current_token += 1
            express_n += tokens[current_token][1] + ' '
        elif token_type == 'PLUS' or token_type == "MINUS" or token_type == "MULTIPLY" or token_type == "DIVIDE" or token_type == "MODULUS":
            if (tokens[current_token + 1][0] != 'SEMICOLON') and (tokens[current_token + 1][0] != 'KEYWORD'):
                temp.append(token_value)
                express_n += token_value + ' '
            else:
                Error_list += f"\nSyntax error -- Expression Error Caused by  {tokens[current_token][1]}  : at line  {tokens[current_token][2]}"
        elif token_type == 'SEMICOLON' or token_type == 'RIGHT_PAREN' or token_type == 'EQUAL' or token_type == 'NOT_EQUAL' or token_type == 'LESS_THAN' or token_type == 'GREATER_THAN' or token_type == 'LESS_THAN_EQUAL' or token_type == 'GREATER_THAN_EQUAL':
            break
        else:
            Error_list += f"\nSyntax error -- Expression Error Caused by  {tokens[current_token][1]}  at line  {tokens[current_token][2]}"
            break
        current_token += 1
    return current_token, express_n, temp


def parse_program(tokens, postion):
    global express_n, Error_list  # calling global varables to be used
    current_token = postion
    while current_token < len(tokens):
        if tokens[current_token][0] == "INCLUDE_ID":
            if tokens[current_token + 1][0] == 'INCLUDE_DIRECTIVE':
                # handle include list
                include_directive = tokens[current_token][1] + ' ' + tokens[current_token + 1][1]
                current_token += 1
                print(f"INCLUDE_LIST: {include_directive}")
                parser_tree.append(('INCLUDE_LIST', include_directive))
            else:
                Error_list += f"\nSYNTAX ERROR: INCLUDE_DIRECTIVE: '{tokens[current_token + 1][1]}' at line {tokens[current_token + 1][2]}"
                current_token += 1

        elif tokens[current_token][0] == "KEYWORD" and tokens[current_token][1] != 'return':
            type_specifer = tokens[current_token][1]
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "IDENTIFIER":
                name = tokens[current_token + 1][1]
                if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "SEMICOLON":  # handle declaration
                    terminator = tokens[current_token + 2][1]
                    print(f"DECLARATION :  {type_specifer} {name} {terminator}")
                    parser_tree.append(("DECLARATION", ("type_specifer", f"{type_specifer}"), ('IDENTIFIER', F"{name}")))
                    current_token += 2

                elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "LEFT_PAREN":  # handle functions
                    f_lp = tokens[current_token + 2][1]
                    function_parameter, pos, param_node = parameter_RFC(tokens, (current_token + 2))
                    current_token = pos
                    if current_token < len(tokens) and tokens[current_token][0] == "RIGHT_PAREN":
                        f_rp = tokens[current_token][1]
                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "LEFT_BRACE":
                            f_lb = tokens[current_token + 1][1]
                            current_token, function_body, child_node = statments(tokens, current_token + 1)

                            if current_token < len(tokens) and tokens[current_token][0] == "RIGHT_BRACE":
                                f_rb = tokens[current_token][1]
                                print(f"FUNCTION: {type_specifer}  {name} {f_lp} {function_parameter} {f_rp} {f_lb} {function_body} {f_rb}")

                                parser_tree.append(('FUNCTION', ("type_specifier", f"{type_specifer}"), ("function_name", f"{name}"), ("function_parameter", tuple(param_node)), ("function_body", tuple(child_node))))
                            else:
                                Error_list += f"\nSyntax Error: <missing right-brace>,  function block not closed at line {tokens[current_token - 1][2]}"
                                print(f"FUNCTION: {type_specifer}  {name} {f_lp} {function_parameter} {f_rp} {f_lb} {function_body}  <missing RIGHT_BRACE' >")
                                parser_tree.append(('FUNCTION', ("type_specifier", f"{type_specifer}"), ("function_name", f"{name}"), ("function_parameter", tuple(param_node)), ("function_body", tuple(child_node))))
                        else:
                            print(f"FUNCTION: {type_specifer}  {name} {f_lp} {function_parameter} <missing LEFT_BRACE>...")
                            Error_list += f"\nSyntax Error: Functon definition   <missing 'right-brace'> at line  {tokens[current_token][2]}"
                    else:
                        print(f"FUNCTION: {type_specifer}  {name} {f_lp} {function_parameter} <missing ')'>...")
                        Error_list += f"\nSyntax Error: incomplete function statement, <missing ')' 'left-brace' ...'right-brace' > at line  {tokens[current_token - 1][2]}"

                elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "ASSIGN":  # initialization
                    type_specifer = tokens[current_token][1]
                    namr = tokens[current_token + 1][1]
                    asg = tokens[current_token + 2][1]
                    current_token, express, exp_node = expression(tokens, current_token + 2)
                    express_n = ''
                    if len(express) != 0:
                        if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                            s_tm = tokens[current_token][1]
                            print(f"INITIALIZATION: {type_specifer} {namr} {asg} {express} {s_tm}")
                            parser_tree.append(('INITIALIZATION', ("type_specifier", f"{type_specifer}"), ("IDENTIFIER", f"{namr}"), ("expression", tuple(exp_node))))
                        else:
                            print(f"INITIALIZATION: {type_specifer} {namr} {asg} {express} <missing ';'>")
                            parser_tree.append(('INITIALIZATION', ("type_specifier", f"{type_specifer}"), ("IDENTIFIER", f"{namr}"), ("expression", f"{express}")))
                            parser_tree.append(('INITIALIZATION', ("type_specifier", f"{type_specifer}"), ("IDENTIFIER", f"{namr}"), ("expression", tuple(exp_node))))
                            continue
                    else:
                        print(f"Syntax Error: variable Initialization error, no value was assigned at line {tokens[current_token][2]} ")
                        if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                            s_tm = tokens[current_token][1]
                            print(f"INITIALIZATION: {type_specifer} {namr} {asg} ~{None}~ {s_tm}")
                        else:
                            print(f"INITIALIZATION: {type_specifer} {namr} {asg} ~{None}~ <missing ';'>")
                            Error_list += f"\nSyntax Error: missing statement terminator at line {tokens[current_token][2]}"
                            continue
                else:
                    print(f"DECLARATION: {type_specifer}  {name} <missing ';' >")
                    parser_tree.append(("DECLARATION", ("type_specifer", f"{type_specifer}"), ('IDENTIFIER', F"{name}")))
                    Error_list += f"\nSyntax Error : unterminated statement for '{tokens[current_token + 1][1]}' at line {tokens[current_token + 1][2]} "
                    current_token += 1
            else:
                Error_list += f"\nSyntax Error : expected token 'IDENTIFIER' goten at line  {tokens[current_token][2]}"

        elif tokens[current_token][0] == 'IF':
            gm = ""
            if_node = []
            else_if = 0
            while True:
                if_key_word = tokens[current_token][1]
                gm += if_key_word + ' '
                if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_PAREN':
                    l_p = tokens[current_token + 1][1]
                    gm += l_p + ' '
                    current_token, if_condition, con_node = condition_statement_RFC(tokens, current_token + 1)
                    gm += if_condition + ' '
                    if else_if == 0:
                        if_node.append(('if_condition', tuple(con_node)))
                    else:
                        if_node.append(('elif_condition', tuple(con_node)))
                    if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_PAREN':
                        r_p = tokens[current_token][1]
                        gm += r_p + ' '
                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_BRACE':
                            l_b = tokens[current_token + 1][1]
                            gm += l_b + ' '
                            current_token, if_statment_body, stat_node = statments(tokens, current_token + 1)
                            if else_if == 0:
                               if_node.append(('if_body', tuple(stat_node)))
                            else:
                                if_node.append(('elif_body', tuple(stat_node)))
                            gm += if_statment_body + ' '
                            if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_BRACE':
                                r_b = tokens[current_token][1]
                                gm += r_b + ' '
                                # current_token += 2
                                if current_token == len(tokens):
                                    print(f"IF STATEMENT {gm}")
                                    break
                                elif (current_token + 1) >= len(tokens):
                                    print(f"IF STATEMENT: {gm}")
                                    break
                                elif tokens[current_token + 1][0] != 'ELSE':
                                    print(f"IF STATEMENT: {gm}")
                                    break
                                else:
                                    if (current_token + 2) < len(tokens) and tokens[current_token + 1][0] == 'ELSE' and tokens[current_token + 2][0] != 'IF':
                                        else_key = tokens[current_token + 1][1]
                                        gm += else_key + ' '
                                        if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'LEFT_BRACE':
                                            e_lb = tokens[current_token + 2][1]
                                            gm += e_lb + ' '
                                            current_token, else_statment_body, els_node = statments(tokens, current_token + 2)
                                            if_node.append(('else_body', tuple(els_node)))
                                            gm += else_statment_body + ' '
                                            if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_BRACE':
                                                e_rb = tokens[current_token][1]
                                                gm += e_rb + ' '
                                                if else_if == 0:
                                                    print(f"IF-ELSE STATEMENT: {gm}")

                                                else:
                                                    print(f"IF-ELSE-IF STATEMENT: {gm}")
                                                break
                                            else:
                                                print(f"IF-STATEMENT: {gm} <missing 'RIGHT_BRACE'>")
                                                Error_list += f"\nSyntax Error: incomplete else statement  missing <RIGHT_BRACE> at line  {tokens[current_token - 1][2]}"
                                                break
                                        else:
                                            print(f"IF statement: {gm} < missing 'LEFT_BRACE' 'RIGHT_BRACE'>")
                                            Error_list += f"\nSyntax Error: incomplete else statement at line {tokens[current_token - 1][2]}"
                                            break

                                    elif (current_token + 2) < len(tokens) and tokens[current_token + 1][0] == 'ELSE' and tokens[current_token + 2][0] == 'IF':
                                        else_key = tokens[current_token + 1][1]
                                        gm += else_key + " "
                                        else_if += 1
                                        current_token += 2
                            else:
                                Error_list += f"\nSyntax Error : if-statement expected  RIGHT_BRACE  at line   {tokens[current_token - 1][2]}"
                                print(f"IF STATEMENT: {gm} < missing 'RIGHT_BRACE'>")
                                parser_tree.append(('if_statement', ('condition', tuple(con_node)), ("if_body", tuple(stat_node))))
                                break
                        else:
                            Error_list += f"\nSyntax Error : if-statement expected  LEFT_BRACE   at line  {tokens[current_token - 1][2]}"
                            print(f"IF STATEMENT: {gm} ... <statement incomplete> ...")
                            break
                    else:
                        Error_list += f"\nSyntax Error : if-statement expected  LEFT_PAREN   < missing ')'> at line {tokens[current_token - 1][2]}"
                        print(f"IF STATEMENT: {gm} ... <statement incomplete> ...")
                        break
                else:
                    Error_list += f"\n Syntax Error : illigal if-statement format at line  {tokens[current_token][2]}"
                    print(f"IF STATEMENT: {gm} ... <missing LEFT_PAREN> ...")
                    break
            parser_tree.append(('if_statment', tuple(if_node)))

        elif tokens[current_token][0] == 'WHILE':
            while_key = tokens[current_token][0]
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_PAREN':
                wh_lp = tokens[current_token + 1][1]
                current_token, condition_statment, con_node = condition_statement_RFC(tokens, current_token + 1)
                if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_PAREN':
                    wh_rp = tokens[current_token][1]
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_BRACE':
                        wh_lb = tokens[current_token + 1][1]
                        current_token, while_body, child_node = statments(tokens, current_token + 1)
                        if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_BRACE':
                            wh_rb = tokens[current_token][1]
                            print(F"WHILE-STATEMENT: {while_key} {wh_lp} {condition_statment} {wh_rp} {wh_lb}  {while_body} {wh_rb}")
                            parser_tree.append(('WHILE-STATEMENT', ('condition', tuple(con_node)), ("while_body", tuple(child_node))))
                        else:
                            print(F"WHILE-STATEMENT: {while_key} {wh_lp} {condition_statment} {wh_rp} {wh_lb}  {while_body} <missing RIGHT_BRACE>")
                            parser_tree.append(('WHILE-STATEMENT', ('condition', f'{condition_statment}'), ("while_body", f"{while_body}")))
                            Error_list += f"\nSyntax Error: missing right-brace at line {tokens[current_token - 1][2]}"
                else:
                    print(F"WHILE-STATEMENT: {while_key} {wh_lp} <error incomplete-while-statement> <missing ')'...>")
                    Error_list += f"\nSyntax error: while statement <error incomplete-while-statement> <missing ')'...>  at line {tokens[current_token - 1][2]}"
            else:
                print(F"WHILE-STATEMENT: {while_key}  <error incomplete-while-statement>")
                Error_list += f"\nSyntax error: while statement incomplete at line  {tokens[current_token][2]}"

        elif tokens[current_token][0] == 'IDENTIFIER':
            name = tokens[current_token][1]
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'ASSIGN':
                asg = tokens[current_token + 1][1]
                if (current_token + 2) < len(tokens) and (current_token + 3) < len(tokens) and tokens[current_token + 2][0] == 'IDENTIFIER' and tokens[current_token + 3][0] == 'LEFT_PAREN':  # function_assignment_call
                    f_name = tokens[current_token + 2][1]
                    l_p = tokens[current_token + 3][1]
                    f_parameter, current_token, param_node = parameter_RFC(tokens, (current_token + 3))
                    r_p = tokens[current_token][1]

                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'SEMICOLON':
                        s_tm = tokens[current_token + 1][1]
                        print(f"FUNCTION ASSIGNMENT: {name} {asg} {f_name} {l_p} {f_parameter} {r_p} {s_tm}")
                        parser_tree.append(('function_assignment', ("IDENTIFIER", f"{name}"), ("f_name", f"{f_name}"), ('param', tuple(param_node))))
                        current_token += 1
                    else:
                        print(f"FUNCTION ASSIGNMENT: {name} {asg} {f_name} {l_p} {f_parameter} {r_p} <missing ';'>")
                        parser_tree.append(('function_assignment', ("IDENTIFIER", f"{name}"), ("f_name", f"{f_name}"), ('param', tuple(param_node))))
                        print("Syntax error: function-call-assignment  missing semicolon at line ", tokens[current_token][2])
                else:
                    current_token, express, exp_node = expression(tokens, current_token + 1)
                    express_n = ''
                    if len(express) != 0:
                        if current_token < len(tokens) and tokens[current_token][0] != "SEMICOLON":
                            Error_list += f"\nSyntax Error: statement terminator missing at line {tokens[current_token - 1][2]}"
                            print(f"VARIABLE ASSIGNMENT2: {name} {asg} {express}  <missing ';'>")
                            parser_tree.append(('variable_assignment', ("IDENTIFIER", f"{name}"), ("expression", tuple(exp_node))))
                        elif current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                            print(f"VARIABLE ASSIGNMENT: {name} {asg} {express} {tokens[current_token][1]}")
                            parser_tree.append(('variable_assignment', ("IDENTIFIER", f"{name}"), ("expression", tuple(exp_node))))
                        else:
                            Error_list += f"\nSyntax Error: statement terminator missing at line {tokens[current_token - 1][2]}"
                            print(f"VARIABLE ASSIGNMENT1: {name} {asg} {express}  <missing ';'>")
                            parser_tree.append(('variable_assignment', ("IDENTIFIER", f"{name}"), ("expression", tuple(exp_node))))
                    else:
                        Error_list += f"\nSyntax Error: variable assignment error, no value was assigned {tokens[current_token - 1][2]}"
                        if tokens[current_token][0] == "SEMICOLON":
                            s_tm = tokens[current_token][1]
                            print(f"VARIABLE ASSIGNMENT: {name} {asg} {None} {s_tm}")

            elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_PAREN':
                l_p = tokens[current_token + 1][1]
                function_parameter, pos, param_node = parameter_RFC(tokens, (current_token + 1))
                current_token = pos
                if tokens[current_token][0] == "RIGHT_PAREN":
                    f_rp = tokens[current_token][1]
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "SEMICOLON":
                        tm = tokens[current_token + 1][1]
                        print(f"FUNCTION CALL: {name} {l_p} {function_parameter} {f_rp} {tm}")
                        current_token += 1
                    else:
                        print(f"FUNCTION CALL : {name} {l_p} {function_parameter} {f_rp}  < missing ';'>")
                        Error_list += f"\nSyntax Error: function call missing statement terminator at line {tokens[current_token][2]}"

        elif tokens[current_token][1] == 'return':
            current_token, express, exp_node = expression(tokens, current_token)
            express_n = ''
            if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                if len(express) != 0:
                    print("RETURN-STATEMENT  : return ", express, tokens[current_token][1])
                    parser_tree.append(("return_statement", express))
                else:
                    Error_list += f"\nSyntax error: no return value was specified at line {tokens[current_token][2]}"
            else:
                if len(express) != 0:
                    print(f"RETURN-STATEMENT  : return {express} <missing ';'>")
                    Error_list += f"\nSyntax error: return statement missing semicolon  at line {tokens[current_token - 1][2]}"
                    parser_tree.append(("return_statement", express))
                else:
                    print(f"RETURN-STATEMENT  : return  <missing return-value>  <missing ';'>")
                    Error_list += f"\nSyntax error: no return value was specified, and  missing a 'statement' terminator for return statement {tokens[current_token - 1][2]}"
        else:
            Error_list += f"\nSyntax Error : '{tokens[current_token][1]}'  at line  {tokens[current_token][2]}"
        current_token += 1


start_run_time_time = time.time()  # Record the Start run time-time of Syntax_analyzer
print("\n\n======================================== PARSER OUTPUT ======================================== \n\n")
parse_program(tokens, 0)  # calling the parser function and passing token list
End_run_time_time = time.time()  # Record the End run time-time of lexical_analyzer
Program_Run_time = End_run_time_time - start_run_time_time  # Calculate the elapsed time (run time of parser function)
print(f"\nParser Program Runtime  :  {Program_Run_time} seconds")


print("\n===============================  ERROR ================ \n")
print(Error_list)
print("\n===============================  PERSER LIST ================ \n")
print(parser_tree)
print("\n===============================  Intimidate_Code_Generator ================ \n")


def serach(my_dict, target_value):
    for key, value in my_dict.items():
        if value[1] == target_value:
            return key
    return target_value

temp = []
disct = {}
count = 1
label_track = 1
def Intemidiet_Code_Generator(list_of_tuples):
    global temp, disct, count, label_track

    for node_name, *children in list_of_tuples:
        if node_name == "DECLARATION":
            hold1 = None
            hold2 = None
            for child in children:
                if child[0] == 'type_specifer':
                    hold1 = child[1]
                if child[0] == 'IDENTIFIER':
                    hold2 = child[1]
            t_v = f't{count}'
            disct[t_v] = (hold1, hold2, None)
            count += 1


        elif node_name == "variable_assignment":
            hold1 = None
            hold2 = None
            value = []
            store = ''
            t_v = None
            for child in children:
                    if child[0] == "IDENTIFIER":
                        hold1 = child[1]
                        t_v = serach(disct, hold1)
                    elif child[0] == "expression":
                        for t in child[1]:
                            t = serach(disct, t)
                            value.append(t)
                        temp = disct[t_v]
                        disct[t_v] = (temp[0], temp[1], ' '.join(str(x) for x in value))
                        count += 1
                        store += f"{t_v} = " + ' '.join(str(x) for x in value)
            print(store)

        elif node_name == "INITIALIZATION":
            store = ""
            hold1 = None
            hold2 = None
            for child in children:
                if child[0] == "type_specifier":
                    hold1 = child[1]
                elif child[0] == "IDENTIFIER":
                    hold2 = child[1]
                else:
                    value = []
                    for t in child[1]:
                        t = serach(disct, t)
                        value.append(t)
                    t_v = f't{count}'
                    disct[t_v] = (hold1, hold2, ' '.join(str(x) for x in value))
                    count += 1
                    store += f"{t_v} = " + ' '.join(str(x) for x in value)

            print(store)





        elif node_name == "FUNCTION":
            i = 0
            for child in children:
                if child[0] == 'function_name':
                    print("func begin", child[1])
                elif child[0] == 'function_parameter':
                    for child in child[1]:
                        for child in child:
                            if isinstance(child, tuple):
                                if child[0] != "type_specifier":
                                    print(f"T{i}  = addr({child[1]})")
                                    disct[f'T{i}'] = child[1]
                                    i += 1
                            elif child != "IDENTIFIER":
                                print(f"T{i}  = addr({child})")
                                disct[f'T{i}'] = child[1]
                                i += 1

                elif child[0] == 'function_body':
                    for child in child[1]:
                        temp.append(child)
                        Intemidiet_Code_Generator(temp)
                        temp = []
                        if child[0] == 'return_statement':
                            print(f"return {child[1]}")
                            print("func end")

        elif node_name == "WHILE-STATEMENT":
            vae = ""
            for child in children:
                if child[0] == 'condition':
                    for x in child[1]:
                        if isinstance(x, tuple):
                            for i in x:
                                t = serach(disct, i)
                                vae += t
                        else:
                            if x == '==':
                                 x = '!='
                            elif x == '!=':
                                 x = '=='
                            elif x == '<':
                                 x = '>='
                            elif x == '>':
                                 x = '<='
                            vae += x

                elif child[0] == 'while_body':
                    l = label_track
                    r = label_track+1
                    print(f"L{l}: if ({vae}) goto L{r}")
                    for sub_child in child[1]:
                        label_track += 1
                        temp.append(sub_child)
                        Intemidiet_Code_Generator(temp)
                        temp = []
                        print(f"L{r} : ")


                if child[0] == 'return_statement':
                     print(f"goto L1")
                     print(f"L2:  return {child[1]}")

        elif node_name == "if_statment":
            end = int((len(children[0]) - 1)/2 +2)
            end = end+label_track-1
            for child in children[0]:
                if child[0] == 'if_condition':
                        vae = ""
                        for x in child[1]:
                            if isinstance(x, tuple):
                                for i in x:
                                    t = serach(disct, i)
                                    vae += t
                            else:
                                if x == '==':
                                    x = '!='
                                elif x == '!=':
                                    x = '=='
                                elif x == '<':
                                    x = '>='
                                elif x == '>':
                                    x = '<='
                                vae += x
                        l = label_track
                        r = label_track + 1
                        print(f"L{l} : if ( {vae} ) goto L{r}")
                        label_track += 1

                elif child[0] == 'if_body':
                    for sub_child in child[1]:
                        temp.append(sub_child)
                        Intemidiet_Code_Generator(temp)
                        temp = []
                        print(f"goto  L{end}")

                elif child[0] == 'elif_condition':
                    vae = ""
                    for x in child[1]:
                        if isinstance(x, tuple):
                            for i in x:
                                t = serach(disct, i)
                                vae += t
                        else:
                            if x == '==':
                                x = '!='
                            elif x == '!=':
                                x = '=='
                            elif x == '<':
                                x = '>='
                            elif x == '>':
                                x = '<='
                            vae += x
                    l = label_track
                    r = label_track + 1
                    print(f"L{l} : if ( {vae} ) goto L{r}")
                    label_track += 1

                elif child[0] == 'elif_body':
                    for sub_child in child[1]:
                        temp.append(sub_child)
                        Intemidiet_Code_Generator(temp)
                        temp = []
                        print(f"goto  L{end}")

                elif child[0] == 'else_body':
                    for sub_child in child[1]:
                        l = label_track
                        label_track += 1
                        print(f'L{l} :')
                        temp.append(sub_child)
                        Intemidiet_Code_Generator(temp)
                        temp = []
                        print(f"L{end} :")
            label_track+=1

        elif node_name == "function_assignment":
            t = []
            function_name = None
            variable_name = None
            for child in children:
                if child[0] == 'IDENTIFIER':
                    variable_name = child[1]
                if child[0] == 'f_name':
                    function_name = child[1]

                if child[0] == 'param':
                    for parm in child[1]:
                        t.append(parm[1])


            print(f"call {function_name}, {', '.join(str(x) for x in t)}")






Intemidiet_Code_Generator(parser_tree)
