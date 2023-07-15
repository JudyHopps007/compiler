import lexical_Analyzer  # importing scanner source file for token list
import time  # for measuring 'parser' run time
import re

tokens = lexical_Analyzer.lexical_analyzer('program.c')  # generating token list using lexical_Analyzer form our program.c that contain the code we want to compile
Error_list = ""  # keep store track of syntax errors generated
express_n = ""  # keep store of expression statements  errors generated
print("\n\n")
parser_tree = []  # used to store syntax tree node information in a tuple form


def parameter_RFC(token, current_token):
    global Error_list
    node = []  # store parameter node information
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


def condition_statement_RFC_old(tokens, position):
    global express_n, Error_list
    node = []  # store condition statement node information
    condition_statment = ''  # store condition statements
    current_token = position
    print('cond', tokens[current_token][0])

    current_token, left_operand, exp_node_l = expression(tokens, current_token)
    condition_statment += left_operand

    node.append(tuple(exp_node_l))
    express_n = ''
    if current_token < len(tokens) and (tokens[current_token][0] == 'EQUAL' or tokens[current_token][0] == 'NOT_EQUAL' or tokens[current_token][0] == 'LESS_THAN' or tokens[current_token][0] == 'GREATER_THAN' or tokens[current_token][0] == 'LESS_THAN_EQUAL' or tokens[current_token][0] == 'GREATER_THAN_EQUAL'):
        conditional_operator = tokens[current_token][1]
        condition_statment += " " + conditional_operator
        current_token, right_operand, exp_node_r = expression(tokens, current_token)
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


def condition_statement_RFC(tokens, position):
    node = []  # store condition statement node information
    condition_statment = ''  # store condition statements
    back_track = 1
    current_token = position
    print('0000000', tokens[current_token][0])
    while back_track != 0:
        current_token += 1
        if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_PAREN':
            back_track -= 1
        elif current_token < len(tokens) and (tokens[current_token][0] == 'IDENTIFIER' or tokens[current_token][0] == 'INTEGER' or tokens[current_token][0] == 'FLOATING_POINT' or tokens[current_token][0] == 'CHAR' or tokens[current_token][0] == 'STRING'):
            while True:
                
                if (current_token + 1 < len(tokens)) and (tokens[current_token + 1][0] == 'EQUAL' or tokens[current_token + 1][0] == 'NOT_EQUAL' or tokens[current_token + 1][0] == 'LESS_THAN' or tokens[current_token + 1][0] == 'GREATER_THAN' or tokens[current_token + 1][0] == 'LESS_THAN_EQUAL' or tokens[current_token + 1][0] == 'GREATER_THAN_EQUAL'):
                    if (current_token + 2 < len(tokens)) and (tokens[current_token + 2][0] == 'IDENTIFIER' or tokens[current_token + 2][0] == 'INTEGER' or tokens[current_token + 2][0] == 'FLOATING_POINT' or tokens[current_token + 2][0] == 'CHAR' or tokens[current_token + 2][0] == 'STRING'):
                        if (current_token + 3 < len(tokens)) and tokens[current_token + 3][0] == 'RIGHT_PAREN':
                            node.append((('operand', tokens[current_token][1]), ('Relational_operator', tokens[current_token + 1][1]), ('operand', tokens[current_token + 2][1])))
                            current_token += 2
                            break
                        else:
                            node.append(('operand', tokens[current_token][1]))
                            node.append(('Relational_operator', tokens[current_token + 1][1]))
                            node.append(('operand', tokens[current_token + 2][1]))
                            current_token += 2

                elif (current_token + 1 < len(tokens)) and (tokens[current_token + 1][0] == 'AND' or tokens[current_token + 1][0] == 'OR'):
                    if (current_token + 2 < len(tokens)) and (tokens[current_token + 2][0] == 'IDENTIFIER' or tokens[current_token + 2][0] == 'INTEGER' or tokens[current_token + 2][0] == 'FLOATING_POINT' or tokens[current_token + 2][0] == 'CHAR' or tokens[current_token + 2][0] == 'STRING'):
                        if (current_token + 3 < len(tokens)) and tokens[current_token + 3][0] == 'RIGHT_PAREN':
                            node.append((('operand', tokens[current_token][1]), ('logical_operator', tokens[current_token + 1][1]), ('operand', tokens[current_token + 2][1])))
                            current_token += 2
                            break
                        else:
                            node.append(('operand', tokens[current_token][1]))
                            node.append(('logical_operator', tokens[current_token + 1][1]))
                            node.append(('operand', tokens[current_token + 2][1]))
                            current_token += 2
                    elif (current_token + 2 < len(tokens)) and (tokens[current_token + 2][0] == 'NOT':



                elif (current_token + 1 < len(tokens)) and tokens[current_token + 1][0] == 'RIGHT_PAREN':
                    node.append(tokens[current_token][1])
                    break

                else:
                    print('Error ')
                    break

    return current_token, condition_statment, node


def statments_old(token, postion):  # statement: (declaration | initializing | function_call | assignment | if_statement | while_statement | return_statement)*;
    global express_n, Error_list
    node = []  # store  statement node information
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
                Error_list += f"Syntax Error : expected token 'IDENTIFIER' goten at line {tokens[current_token][2]}"

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
                            Error_list += f"\nSyntax Error : if-statement expected  LEFT_BRACE    at line  {tokens[current_token - 1][2]} "
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


def statments(tokens, postion):  # statement: (declaration | initializing | function_call | assignment | if_statement | while_statement | return_statement)*;
    global express_n, Error_list
    node = []  # store  statement node information
    statment_block = ''  # store statements in block
    block_track = 1
    current_token = postion

    while block_track != 0:
        current_token += 1
        if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_BRACE':
            block_track -= 1

        # constant syntax
        elif current_token < len(tokens) and tokens[current_token][0] == "CONSTANT_KEY":
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "KEYWORD" and tokens[current_token + 1][1] != 'return' and tokens[current_token + 1][1] != 'void' and tokens[current_token + 1][1] != 'bool':
                if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "IDENTIFIER":
                    if (current_token + 3) < len(tokens) and tokens[current_token + 3][0] == "ASSIGN":
                        if (current_token + 4) < len(tokens) and (tokens[current_token + 4][0] == "IDENTIFIER" or tokens[current_token + 4][0] == "FLOATING_POINT" or tokens[current_token + 4][0] == "CHAR" or tokens[current_token + 4][0] == "STRING"):
                            constant_data_type = tokens[current_token + 1][1]
                            constant_name = tokens[current_token + 2][1]
                            constant_value = tokens[current_token + 4][1]
                            current_token += 4
                            print(f"CONSTANT: {constant_data_type} {constant_name} {constant_value}")
                            node.append(('CONSTANT', ("constant_data_type", constant_data_type), ("constant_name", constant_name), ("constant_value", constant_value)))
                            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'SEMICOLON':
                                current_token += 1
                            else:
                                Error_list += f"\nSyntax Error: constant definition not terminated. missing semicolon at line  {tokens[current_token][2]}"
                        else:
                            current_token += 3
                            Error_list += f"\nSyntax Error: constant definition error. no value assigned to the constant variable at line  {tokens[current_token][2]}"
                    else:
                        current_token += 2
                        Error_list += f"\nSyntax Error: constant definition error. missing =  at line  {tokens[current_token][2]}"
                else:
                    current_token += 1
                    Error_list += f"\nSyntax Error: constant definition incomplete. missing constant variable name  at line  {tokens[current_token][2]}"
            else:
                Error_list += f"\nSyntax Error: constant definition error. missing constant data type at line  {tokens[current_token][2]}"

        elif current_token < len(tokens) and tokens[current_token][0] == "KEYWORD" and tokens[current_token][1] != 'return':
            type_specifer = tokens[current_token][1]
            while True:
                if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "IDENTIFIER":
                    varable_name = tokens[current_token + 1][1]
                    current_token += 1
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "SEMICOLON":  # handle declaration
                        print(f"DECLARATION :  {type_specifer} {varable_name}")
                        node.append(("DECLARATION", ("type_specifier", f"{type_specifer}"), ('IDENTIFIER', varable_name)))
                        current_token += 1
                        break
                    elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "COMMA":
                        print(f"DECLARATION :  {type_specifer} {varable_name}")
                        node.append(("DECLARATION", ("type_specifier", f"{type_specifer}"), ('IDENTIFIER', varable_name)))
                        current_token += 1
                        continue


                    elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "LEFT_PAREN":  # handle functions
                        f_lp = tokens[current_token + 1][1]
                        function_parameter_str, token_position, function_parameter_node = parameter_RFC(tokens, (current_token + 1))
                        current_token = token_position
                        if current_token < len(tokens) and tokens[current_token][0] == "RIGHT_PAREN":
                            f_rp = tokens[current_token][1]
                            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "LEFT_BRACE":
                                block_track += 1
                                f_lb = tokens[current_token + 1][1]
                                current_token, function_body, child_node = statments(tokens, current_token + 1)

                                if current_token < len(tokens) and tokens[current_token][0] == "RIGHT_BRACE":
                                    block_track -= 1
                                    f_rb = tokens[current_token][1]
                                    print(f"FUNCTION: {type_specifer}  {varable_name} {f_lp} {function_parameter_str} {f_rp} {f_lb} {function_body} {f_rb}")
                                    node.append(('FUNCTION', ("type_specifier", type_specifer), ("function_name", varable_name), ("function_parameter", tuple(function_parameter_node)), ("function_body", tuple(child_node))))
                                    break
                                else:
                                    print(f"FUNCTION: {type_specifer}  {varable_name} {f_lp} {function_parameter_str} {f_rp} {f_lb} {function_body}")
                                    Error_list += f"\nSyntax Error: <missing right-brace>,  function block not closed properly at line {tokens[current_token - 1][2]}"
                                    node.append(('FUNCTION', ("type_specifier", type_specifer), ("function_name", varable_name), ("function_parameter", tuple(function_parameter_node)), ("function_body", tuple(child_node))))
                                    break
                            else:
                                print(f"FUNCTION: {type_specifer}  {varable_name} {f_lp} {function_parameter_str} <missing LEFT_BRACE>...")
                                Error_list += f"\nSyntax Error: Incomplete Functon definition.  missing left-brace  at line  {tokens[current_token][2]}"
                                break
                        else:
                            print(f"FUNCTION: {type_specifer}  {varable_name} {f_lp} {function_parameter_str} <missing ')'>...")
                            Error_list += f"\nSyntax Error: incomplete function statement, missing ')' 'right-paren' at line  {tokens[current_token - 1][2]}"
                            break

                    elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "ASSIGN":  # Variable declaration and  initialization
                        asg = tokens[current_token + 1][1]
                        current_token, express, exp_node = expression(tokens, current_token + 1)
                        express_n = ''
                        if len(express) != 0:
                            if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                                s_tm = tokens[current_token][1]
                                print(f"VAR_DECLARATION_INITIALIZATION-: {type_specifer} {varable_name} {asg} {express} {s_tm}")
                                node.append(('VAR_DECLARATION_INITIALIZATION', ("type_specifier", f"{type_specifer}"), ("IDENTIFIER", f"{varable_name}"), ("expression", tuple(exp_node))))
                                break
                            else:
                                print(f"VAR_DECLARATION_INITIALIZATION: {type_specifer} {varable_name} {asg} {express} <missing ';'>")
                                node.append(('VAR_DECLARATION_INITIALIZATION', ("type_specifier", type_specifer), ("IDENTIFIER", varable_name), ("expression", tuple(exp_node))))
                                Error_list += f"\nSyntax Error : unterminated statement  at line {tokens[current_token - 1][2]} "
                                break
                        else:
                            Error_list += f"\nSyntax Error: variable Initialization error, no value was assigned to variable at line {tokens[current_token][2]}"
                            if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                                s_tm = tokens[current_token][1]
                                print(f"VAR_DECLARATION_INITIALIZATION: {type_specifer} {varable_name} {asg} ~{None}~ {s_tm}")
                                break
                            else:
                                print(f"VAR_DECLARATION_INITIALIZATION: {type_specifer} {varable_name} {asg} ~{None}~ <missing ';'>")
                                Error_list += f"\nSyntax Error: missing statement terminator at line {tokens[current_token][2]}"
                                break

                elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "POINTER_TO_VAR":  # pointer declaration
                    varable_name = tokens[current_token + 1][1]
                    current_token += 1
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "SEMICOLON":
                        print(f"POINTER_DECLARATION :  {type_specifer} {varable_name}")
                        node.append(("POINTER_DECLARATION", ("type_specifier", type_specifer), ('POINTER_TO_VAR', varable_name)))
                        current_token += 1
                        break
                    elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "COMMA":
                        print(f"POINTER_DECLARATION :  {type_specifer} {varable_name}")
                        node.append(("POINTER_DECLARATION", ("type_specifier", type_specifer), ('POINTER_TO_VAR', varable_name)))
                        current_token += 1
                        continue
                    else:
                        Error_list += f"\nSyntax Error : unterminated pointer statement  at line {tokens[current_token][2]}"
                        break

                elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "ARRAY":  # Array syntax 1
                    array = tokens[current_token + 1][1]
                    if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "SEMICOLON":
                        print(f"ARRAY_DECLARATION: {type_specifer} {array} ")
                        node.append(('ARRAY_DECLARATION', ("type_specifier", f"{type_specifer}"), ("array_name", array)))
                        current_token += 2
                    elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "ASSIGN":
                        if (current_token + 3) < len(tokens) and tokens[current_token + 3][0] == "ARRAY_VALUE":
                            array_value = tokens[current_token + 3][1]
                            print(f"ARRAY_DECLARATION_INITIALIZATION: {type_specifer} {array}  =  {array_value}")
                            node.append(('ARRAY_DECLARATION_INITIALIZATION', ("type_specifier", f"{type_specifer}"), ("array_name", array), ("array_value", array_value)))
                            current_token += 3
                            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "SEMICOLON":
                                current_token += 1
                                break
                            else:
                                Error_list += f"\nSyntax Error : unterminated statement  at line {tokens[current_token][2]} "
                                break
                        else:
                            current_token += 2
                            Error_list += f"\nSyntax Error : no value assigned to array  at line {tokens[current_token][2]} "
                            break
                    else:
                        current_token += 1
                        Error_list += f"\nSyntax Error : incomplete array declaration  at line {tokens[current_token][2]} "
                        break
                else:
                    Error_list += f"\nSyntax Error : incomplete statement  at line {tokens[current_token][2]}"
                    break

        elif current_token < len(tokens) and tokens[current_token][0] == 'ARRAY':  # Array syntax 2
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "ASSIGN":
                if (current_token + 2) < len(tokens) and (tokens[current_token + 2][0] == "IDENTIFIER" or tokens[current_token + 2][0] == "INTEGER" or tokens[current_token + 2][0] == "STRING" or tokens[current_token + 2][0] == "FLOATING_POINT" or tokens[current_token + 2][0] == "CHAR"):
                    array_name = tokens[current_token][1]
                    array_value = tokens[current_token + 2][1]
                    match = re.search(r'\[\s*([a-zA-Z_][a-zA-Z0-9_])+\s*\]', array_name)
                    if match:
                        print(f"ARRAY_INITIALIZATION:  {array_name}  =  {array_value}")
                        node.append(('ARRAY_INITIALIZATION', ("array_name", array_name), ("array_value", array_value)))
                        current_token += 2
                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "SEMICOLON":
                            current_token += 1
                        else:
                            Error_list += f"\nSyntax Error : Statement not terminated proper. missing a semicolon at line  {tokens[current_token][2]}"
                    else:
                        current_token += 2
                        Error_list += f"\nSyntax Error : Array initialization error. array index not specified at line  {tokens[current_token][2]}"
                else:
                    current_token += 1
                    Error_list += f"\nSyntax Error : Array element value error. wrong value is being assigned to the array at line  {tokens[current_token][2]}"

        elif current_token < len(tokens) and tokens[current_token][0] == 'IF':
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
                                            block_track += 1
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
                                node.append(('if_statement', ('condition', tuple(con_node)), ("if_body", tuple(stat_node))))
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
                        if current_token < len(tokens) and tokens[current_token][0] == 'RIGHT_BRACE':
                            block_track -= 1
                            wh_rb = tokens[current_token][1]
                            print(F"WHILE-STATEMENT: {while_key} {wh_lp} {condition_statment} {wh_rp} {wh_lb}  {while_body} {wh_rb}")
                            node.append(('WHILE-STATEMENT', ('condition', tuple(con_node)), ("while_body", tuple(child_node))))
                        else:
                            print(F"WHILE-STATEMENT: {while_key} {wh_lp} {condition_statment} {wh_rp} {wh_lb}  {while_body} <missing RIGHT_BRACE>")
                            node.append(('WHILE-STATEMENT', ('condition', f'{condition_statment}'), ("while_body", f"{while_body}")))
                            Error_list += f"\nSyntax Error: missing right-brace at line {tokens[current_token - 1][2]}"
                else:
                    print(F"WHILE-STATEMENT: {while_key} {wh_lp} <error incomplete-while-statement> <missing ')'...>")
                    Error_list += f"\nSyntax error: while statement <error incomplete-while-statement> <missing ')'...>  at line {tokens[current_token - 1][2]}"
            else:
                print(F"WHILE-STATEMENT: {while_key}  <error incomplete-while-statement>")
                Error_list += f"\nSyntax error: while statement incomplete at line  {tokens[current_token][2]}"

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
                        print(f"FUNCTION ASSIGNMENT: {name} {asg} {f_name} {l_p} {f_parameter} {r_p} {s_tm}")
                        node.append(('function_assignment', ("IDENTIFIER", name), ("f_name", f_name), ('param', tuple(param_node))))
                        current_token += 1
                    else:
                        print(f"FUNCTION ASSIGNMENT: {name} {asg} {f_name} {l_p} {f_parameter} {r_p} <missing ';'>")
                        node.append(('function_assignment', ("IDENTIFIER", name), ("f_name", f_name), ('param', tuple(param_node))))
                        print("Syntax error: function-call-assignment statement.  missing statement terminator at line at line ", tokens[current_token][2])

                elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'MEMORY_REFERENCE':  # pointer assignment statement
                    print(f"POINTER_ASSIGNMENT:  {name} {asg} {tokens[current_token + 2][1]}")
                    node.append(('POINTER_ASSIGNMENT', ("pointer_name", name), ("pointer_value", tokens[current_token + 2][1])))
                    current_token += 2
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'SEMICOLON':
                        current_token += 1
                    else:
                        Error_list += f"\nSyntax Error: statement terminator missing at line {tokens[current_token][2]}"

                else:  # variable assignment statement
                    current_token, express, exp_node = expression(tokens, current_token + 1)
                    express_n = ''
                    if len(express) != 0:
                        if current_token < len(tokens) and tokens[current_token][0] != "SEMICOLON":
                            Error_list += f"\nSyntax Error: statement terminator missing at line {tokens[current_token - 1][2]}"
                            print(f"VARIABLE_ASSIGNMENT: {name} {asg} {express}")
                            node.append(('VARIABLE_ASSIGNMENT', ("IDENTIFIER", f"{name}"), ("expression", tuple(exp_node))))
                        elif current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                            print(f"VARIABLE_ASSIGNMENT: {name} {asg} {express} {tokens[current_token][1]}")
                            node.append(('VARIABLE_ASSIGNMENT', ("IDENTIFIER", f"{name}"), ("expression", tuple(exp_node))))
                        else:
                            Error_list += f"\nSyntax Error: statement terminator missing at line {tokens[current_token - 1][2]}"
                            print(f"VARIABLE_ASSIGNMENT: {name} {asg} {express}  <missing ';'>")
                            node.append(('VARIABLE_ASSIGNMENT', ("IDENTIFIER", f"{name}"), ("expression", tuple(exp_node))))
                    else:
                        Error_list += f"\nSyntax Error: variable assignment error, no value was assigned {tokens[current_token - 1][2]}"
                        if tokens[current_token][0] == "SEMICOLON":
                            s_tm = tokens[current_token][1]
                            print(f"VARIABLE_ASSIGNMENT: {name} {asg} {None} {s_tm}")

            elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_PAREN':  # function call
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
            else:
                Error_list += f"\nSyntax Error: incomplete statement at line {tokens[current_token][2]}"


        elif current_token < len(tokens) and tokens[current_token][0] == 'STRUCT_KEY':  # Structure
            struct_members_node = []
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'IDENTIFIER':
                structure_name = tokens[current_token + 1][1]
                if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'LEFT_BRACE':
                    block_track += 1
                    current_token += 2
                    while True:
                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'KEYWORD':
                            if (current_token + 2) < len(tokens) and (tokens[current_token + 2][0] == 'IDENTIFIER' or tokens[current_token + 2][0] == 'ARRAY'):
                                struct_members_node.append(('struct_member', ('member_data_type', tokens[current_token + 1][1]), ('member_name', tokens[current_token + 2][1])))
                                current_token += 2
                                if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'SEMICOLON':
                                    current_token += 1
                                else:
                                    Error_list += f"\nSyntax error: unterminated structure member statement  at line {tokens[current_token][2]}"
                            else:
                                Error_list += f"\nSyntax error: incorrect structure member definition. structure member is defined incorrectly at line {tokens[current_token][2]}"
                                break

                        elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'STRUCT_KEY':  # nested struct
                            if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'IDENTIFIER':
                                if (current_token + 3) < len(tokens) and tokens[current_token + 3][0] == 'IDENTIFIER':
                                    struct_members_node.append(('nested_struct_member', ('struct_name', tokens[current_token + 2][1]), ('member_name', tokens[current_token + 3][1])))
                                    current_token += 3
                                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'SEMICOLON':
                                        current_token += 1
                                    else:
                                        Error_list += f"\nSyntax error: unterminated nested structure member statement at line {tokens[current_token][2]}"
                                else:
                                    current_token += 2
                                    Error_list += f"\nSyntax error:  nested structure member defined incorrectly at line {tokens[current_token][2]}"
                            else:
                                current_token += 1
                                Error_list += f"\nSyntax error: incomplete nested structure member definition at line {tokens[current_token][2]}"


                        elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'RIGHT_BRACE':
                            block_track -= 1
                            if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'SEMICOLON':
                                node.append(("STRUCTURE_DEFINITION", ('structure_name', structure_name), ('structure_members', tuple(struct_members_node))))
                                current_token += 2
                                break

                            elif (current_token + 2) < len(tokens) and (tokens[current_token + 2][0] == 'IDENTIFIER' or tokens[current_token + 2][0] == 'ARRAY'):
                                node.append(("STRUCTURE_DEFINITION", ('structure_name', structure_name), ('structure_members', tuple(struct_members_node))))
                                current_token += 2
                                while True:
                                    if current_token < len(tokens) and (tokens[current_token][0] == 'IDENTIFIER' or tokens[current_token][0] == 'ARRAY'):
                                        structure_variable = tokens[current_token][1]
                                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "SEMICOLON":
                                            node.append(("STRUCTURE_VARIABLE", ('structure_name', structure_name), ('structure_variable', structure_variable)))
                                            current_token += 1
                                            break

                                        elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "COMMA":
                                            node.append(("STRUCTURE_VARIABLE", ('structure_name', structure_name), ('structure_variable', structure_variable)))
                                            current_token += 1
                                        else:
                                            Error_list += f"\nSyntax error: incorrect statement  at line {tokens[current_token][2]}"
                                            current_token += 1
                                            break
                                        current_token += 1
                                    else:
                                        Error_list += f"\nSyntax error: incomplete statement at line {tokens[current_token][2]}"
                                        break

                                break
                            else:
                                current_token += 1
                                Error_list += f"\nSyntax error: unterminated structure  statement. missing semicolon  at line {tokens[current_token][2]}"
                                break
                        else:
                            Error_list += f"\nSyntax error: unidentified error at line {tokens[current_token][2]}"

                            break

                elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'IDENTIFIER':  # struct Variables
                    node.append(("STRUCTURE_VARIABLE", ('structure_name', structure_name), ('structure_variable', tokens[current_token + 2][1])))
                    current_token += 2
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'SEMICOLON':
                        current_token += 1
                    else:
                        Error_list += f"\nSyntax error: unterminated statement. missing semicolon  at line {tokens[current_token][2]}"

        elif current_token < len(tokens) and tokens[current_token][0] == 'ENUMERATION_KEY':  # Enumerated Type Declaration
            constants_node = []
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'IDENTIFIER':
                enumeration_name = tokens[current_token + 1][1]
                if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'LEFT_BRACE':
                    block_track += 1
                    current_token += 2
                    while True:
                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'IDENTIFIER':
                            if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'ASSIGN':
                                if (current_token + 3) < len(tokens) and tokens[current_token + 3][0] == 'INTEGER':
                                    constants_node.append(('enumeration_member', ('constant_name', tokens[current_token + 1][1]), ('constant_value', tokens[current_token + 3][1])))
                                    current_token += 3
                                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'COMMA':
                                        current_token += 1
                                    else:
                                        Error_list += f"\nSyntax error: missing comma  at line {tokens[current_token][2]}"
                                else:
                                    Error_list += f"\nSyntax error: incorrect structure member definition. structure member is defined incorrectly at line {tokens[current_token][2]}"
                                    break
                        elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'RIGHT_BRACE':
                            block_track -= 1
                            if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'SEMICOLON':
                                node.append(("ENUMERATION_DEFINITION", ('enumeration_name', enumeration_name), 'enumeration_constants', tuple(constants_node)))
                                current_token += 2
                                break

                            elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'IDENTIFIER':
                                node.append(("ENUMERATION_DEFINITION", ('enumeration_name', enumeration_name), 'enumeration_constants', tuple(constants_node)))
                                current_token += 2
                                while True:
                                    if current_token < len(tokens) and (tokens[current_token][0] == 'IDENTIFIER'):
                                        structure_variable = tokens[current_token][1]
                                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "SEMICOLON":
                                            node.append(("ENUMERATION_VARIABLE", ('enumeration_name', enumeration_name), ('enumeration_variable', structure_variable)))
                                            current_token += 1
                                            break

                                        elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "COMMA":
                                            node.append(("ENUMERATION_VARIABLE", ('enumeration_name', enumeration_name), ('enumeration_variable', structure_variable)))
                                            current_token += 1
                                        else:
                                            Error_list += f"\nSyntax error: incorrect statement  at line {tokens[current_token][2]}"
                                            current_token += 1
                                            break
                                        current_token += 1
                                    else:
                                        Error_list += f"\nSyntax error: incomplete statement at line {tokens[current_token][2]}"
                                        break
                                break
                elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'IDENTIFIER':
                    node.append(("ENUMERATION_VARIABLE", ('enumeration_name', enumeration_name), ('enumeration_variable', tokens[current_token + 2][1])))
                    if (current_token + 3) < len(tokens) and tokens[current_token + 3][0] == 'SEMICOLON':
                        current_token += 3
                    else:
                        Error_list += f"\nSyntax error: unterminated  statement at line {tokens[current_token][2]}"
                        current_token += 2
                else:
                    Error_list += f"\nSyntax error: incorrect enumeration declaration statement at line {tokens[current_token][2]}"
                    current_token += 1
            else:
                Error_list += f"\nSyntax error: at statement at line {tokens[current_token][2]}"

        elif current_token < len(tokens) and tokens[current_token][1] == 'return':
            current_token, express, exp_node = expression(tokens, current_token)
            express_n = ''
            if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                if len(express) != 0:
                    print("RETURN-STATEMENT  : return ", express, tokens[current_token][1])
                    node.append(("return_statement", express))
                else:
                    Error_list += f"\nSyntax error: no return value was specified at line {tokens[current_token][2]}"
            else:
                if len(express) != 0:
                    print(f"RETURN-STATEMENT  : return {express} <missing ';'>")
                    Error_list += f"\nSyntax error: return statement missing semicolon  at line {tokens[current_token - 1][2]}"
                    node.append(("return_statement", express))
                else:
                    print(f"RETURN-STATEMENT  : return  <missing return-value>  <missing ';'>")
                    Error_list += f"\nSyntax error: no return value was specified, and  missing a 'statement' terminator for return statement {tokens[current_token - 1][2]}"
        else:
            print('1')
            Error_list += f"\nSyntax Error : '{tokens[current_token][1]}'  at line  {tokens[current_token][2]}"
            if current_token < len(tokens):
                pass
            else:
                break

    return current_token, statment_block, node


def precedence():
    pass


def expression(tokens, position):
    global express_n, Error_list
    global express_n
    temp = []  # store  expression node information
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
            current_token, express_n, temp = expression(tokens, current_token)  # Handle nested expressions recursively
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
            # Error_list += f"\nSyntax error -- Expression Error Caused by  {tokens[current_token][1]}  at line  {tokens[current_token][2]}"
            current_token -= 1
            break
        current_token += 1
        express_n = express_n.rstrip()

    # print("return ", temp)
    return current_token, express_n, temp


def parse_program(tokens, postion):
    global express_n, Error_list, parser_tree  # calling global varables to be used
    current_token = postion

    while current_token < len(tokens):
        # print('begin ==', tokens[current_token][1])
        if tokens[current_token][0] == "INCLUDE_ID":
            if tokens[current_token + 1][0] == 'INCLUDE_DIRECTIVE':
                # handle include list
                include_directive = tokens[current_token][1] + ' ' + tokens[current_token + 1][1]
                current_token += 1
                print(f"HEADER_FILE: {include_directive}")
                parser_tree.append(('HEADER_FILE', include_directive))
            elif tokens[current_token + 1][0] == 'STRING':
                match = re.search(r'\"\s*\w+.h\s*\"', tokens[current_token + 1][1])
                if match:
                    # handle include list
                    include_directive = tokens[current_token][1] + ' ' + tokens[current_token + 1][1]
                    current_token += 1
                    print(f"HEADER_FILE: {include_directive}")
                    parser_tree.append(('HEADER_FILE', include_directive))
                else:
                    Error_list += f"\nSYNTAX ERROR: at include directive  {tokens[current_token + 1][1]} at line {tokens[current_token + 1][2]}"
                    current_token += 1
            else:
                Error_list += f"\nSYNTAX ERROR: at include directive: {tokens[current_token + 1][1]} at line {tokens[current_token + 1][2]}"
                current_token += 1

        # macro syntax
        elif tokens[current_token][0] == "MACRO":
            if tokens[current_token + 1][0] == 'IDENTIFIER':
                macro_name = tokens[current_token + 1][1]
                if tokens[current_token + 2][0] == 'IDENTIFIER' or tokens[current_token + 2][0] == 'INTEGER':
                    macro_value = tokens[current_token + 2][1]
                    macro = macro_name + ' ' + macro_value
                    print(f"MACRO: {macro}")
                    parser_tree.append(('MACRO', ("macro_name", macro_name), ("macro_value", macro_value)))
                    current_token += 2
                if tokens[current_token + 2][0] == 'LEFT_PAREN':

                    macro_parameter_str, token_position, macro_parameter_node = parameter_RFC(tokens, (current_token + 2))
                    current_token = token_position

                    if tokens[current_token + 1][0] == 'LEFT_PAREN':
                        current_token += 1
                        macro_body = ''
                        while tokens[current_token][0] != 'RIGHT_PAREN':
                            macro_body += tokens[current_token][1]
                            current_token += 1

                        macro_body += tokens[current_token][1]
                        macro = f"{macro_name} {macro_parameter_node}  {macro_body}"
                        print(f"MACRO: {macro}")
                        parser_tree.append(('MACRO', ("macro_name", f"{macro_name}"), ("macro_parameter", tuple(macro_parameter_node)), ("macro_body", macro_body)))

        # constant syntax
        elif tokens[current_token][0] == "CONSTANT_KEY":
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "KEYWORD" and tokens[current_token + 1][1] != 'return' and tokens[current_token + 1][1] != 'void' and tokens[current_token + 1][1] != 'bool':
                if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "IDENTIFIER":
                    if (current_token + 3) < len(tokens) and tokens[current_token + 3][0] == "ASSIGN":
                        if (current_token + 4) < len(tokens) and (tokens[current_token + 4][0] == "IDENTIFIER" or tokens[current_token + 4][0] == "FLOATING_POINT" or tokens[current_token + 4][0] == "CHAR" or tokens[current_token + 4][0] == "STRING"):
                            constant_data_type = tokens[current_token + 1][1]
                            constant_name = tokens[current_token + 2][1]
                            constant_value = tokens[current_token + 4][1]
                            current_token += 4
                            print(f"CONSTANT: {constant_data_type} {constant_name} {constant_value}")
                            parser_tree.append(('CONSTANT', ("constant_data_type", constant_data_type), ("constant_name", constant_name), ("constant_value", constant_value)))
                            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'SEMICOLON':
                                current_token += 1
                            else:
                                Error_list += f"\nSyntax Error: constant definition not terminated. missing semicolon at line  {tokens[current_token][2]}"
                        else:
                            current_token += 3
                            Error_list += f"\nSyntax Error: constant definition error. no value assigned to the constant variable at line  {tokens[current_token][2]}"
                    else:
                        current_token += 2
                        Error_list += f"\nSyntax Error: constant definition error. missing =  at line  {tokens[current_token][2]}"
                else:
                    current_token += 1
                    Error_list += f"\nSyntax Error: constant definition incomplete. missing constant variable name  at line  {tokens[current_token][2]}"
            else:
                Error_list += f"\nSyntax Error: constant definition error. missing constant data type at line  {tokens[current_token][2]}"


        elif tokens[current_token][0] == "KEYWORD" and tokens[current_token][1] != 'return':
            type_specifer = tokens[current_token][1]

            while True:
                if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "IDENTIFIER":
                    varable_name = tokens[current_token + 1][1]
                    current_token += 1
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "SEMICOLON":  # handle declaration
                        print(f"DECLARATION :  {type_specifer} {varable_name}")
                        parser_tree.append(("DECLARATION", ("type_specifier", f"{type_specifer}"), ('IDENTIFIER', varable_name)))
                        current_token += 1
                        break
                    elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "COMMA":
                        print(f"DECLARATION :  {type_specifer} {varable_name}")
                        parser_tree.append(("DECLARATION", ("type_specifier", f"{type_specifer}"), ('IDENTIFIER', varable_name)))
                        current_token += 1
                        continue



                    elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "LEFT_PAREN":  # handle functions
                        f_lp = tokens[current_token + 1][1]
                        function_parameter_str, token_position, function_parameter_node = parameter_RFC(tokens, (current_token + 1))
                        current_token = token_position
                        if current_token < len(tokens) and tokens[current_token][0] == "RIGHT_PAREN":
                            f_rp = tokens[current_token][1]
                            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "LEFT_BRACE":
                                f_lb = tokens[current_token + 1][1]
                                current_token, function_body, child_node = statments(tokens, current_token + 1)

                                if current_token < len(tokens) and tokens[current_token][0] == "RIGHT_BRACE":
                                    f_rb = tokens[current_token][1]
                                    print(f"FUNCTION: {type_specifer}  {varable_name} {f_lp} {function_parameter_str} {f_rp} {f_lb} {function_body} {f_rb}")
                                    parser_tree.append(('FUNCTION', ("type_specifier", type_specifer), ("function_name", varable_name), ("function_parameter", tuple(function_parameter_node)), ("function_body", tuple(child_node))))
                                    break
                                else:
                                    print(f"FUNCTION: {type_specifer}  {varable_name} {f_lp} {function_parameter_str} {f_rp} {f_lb} {function_body}")
                                    Error_list += f"\nSyntax Error: <missing right-brace>,  function block not closed properly at line {tokens[current_token - 1][2]}"
                                    parser_tree.append(('FUNCTION', ("type_specifier", type_specifer), ("function_name", varable_name), ("function_parameter", tuple(function_parameter_node)), ("function_body", tuple(child_node))))
                                    break
                            else:
                                print(f"FUNCTION: {type_specifer}  {varable_name} {f_lp} {function_parameter_str} <missing LEFT_BRACE>...")
                                Error_list += f"\nSyntax Error: Incomplete Functon definition.  missing left-brace  at line  {tokens[current_token][2]}"
                                break
                        else:
                            print(f"FUNCTION: {type_specifer}  {varable_name} {f_lp} {function_parameter_str} <missing ')'>...")
                            Error_list += f"\nSyntax Error: incomplete function statement, missing ')' 'right-paren' at line  {tokens[current_token - 1][2]}"
                            break

                    elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "ASSIGN":  # Variable declaration and  initialization
                        asg = tokens[current_token + 1][1]
                        current_token, express, exp_node = expression(tokens, current_token + 1)
                        express_n = ''
                        if len(express) != 0:
                            if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                                s_tm = tokens[current_token][1]
                                print(f"VAR_DECLARATION_INITIALIZATION-: {type_specifer} {varable_name} {asg} {express} {s_tm}")
                                parser_tree.append(('VAR_DECLARATION_INITIALIZATION', ("type_specifier", f"{type_specifer}"), ("IDENTIFIER", f"{varable_name}"), ("expression", tuple(exp_node))))
                                break
                            else:
                                print(f"VAR_DECLARATION_INITIALIZATION: {type_specifer} {varable_name} {asg} {express} <missing ';'>")
                                parser_tree.append(('VAR_DECLARATION_INITIALIZATION', ("type_specifier", type_specifer), ("IDENTIFIER", varable_name), ("expression", tuple(exp_node))))
                                Error_list += f"\nSyntax Error : unterminated statement  at line {tokens[current_token - 1][2]} "
                                break
                        else:
                            Error_list += f"\nSyntax Error: variable Initialization error, no value was assigned to variable at line {tokens[current_token][2]}"
                            if current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                                s_tm = tokens[current_token][1]
                                print(f"VAR_DECLARATION_INITIALIZATION: {type_specifer} {varable_name} {asg} ~{None}~ {s_tm}")
                                break
                            else:
                                print(f"VAR_DECLARATION_INITIALIZATION: {type_specifer} {varable_name} {asg} ~{None}~ <missing ';'>")
                                Error_list += f"\nSyntax Error: missing statement terminator at line {tokens[current_token][2]}"
                                break




                elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "POINTER_TO_VAR":  # pointer declaration
                    varable_name = tokens[current_token + 1][1]
                    current_token += 1
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "SEMICOLON":
                        print(f"POINTER_DECLARATION :  {type_specifer} {varable_name}")
                        parser_tree.append(("POINTER_DECLARATION", ("type_specifier", type_specifer), ('POINTER_TO_VAR', varable_name)))
                        current_token += 1
                        break
                    elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "COMMA":
                        print(f"POINTER_DECLARATION :  {type_specifer} {varable_name}")
                        parser_tree.append(("POINTER_DECLARATION", ("type_specifier", type_specifer), ('POINTER_TO_VAR', varable_name)))
                        current_token += 1
                        continue
                    else:
                        Error_list += f"\nSyntax Error : unterminated pointer statement  at line {tokens[current_token][2]}"
                        break



                elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "ARRAY":  # Array syntax 1
                    array = tokens[current_token + 1][1]
                    if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "SEMICOLON":
                        print(f"ARRAY_DECLARATION: {type_specifer} {array} ")
                        parser_tree.append(('ARRAY_DECLARATION', ("type_specifier", f"{type_specifer}"), ("array_name", array)))
                        current_token += 2
                    elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == "ASSIGN":
                        if (current_token + 3) < len(tokens) and tokens[current_token + 3][0] == "ARRAY_VALUE":
                            array_value = tokens[current_token + 3][1]
                            print(f"ARRAY_DECLARATION_INITIALIZATION: {type_specifer} {array}  =  {array_value}")
                            parser_tree.append(('ARRAY_DECLARATION_INITIALIZATION', ("type_specifier", f"{type_specifer}"), ("array_name", array), ("array_value", array_value)))
                            current_token += 3
                            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "SEMICOLON":
                                current_token += 1
                                break
                            else:
                                Error_list += f"\nSyntax Error : unterminated statement  at line {tokens[current_token][2]} "
                                break
                        else:
                            current_token += 2
                            Error_list += f"\nSyntax Error : no value assigned to array  at line {tokens[current_token][2]} "
                            break
                    else:
                        current_token += 1
                        Error_list += f"\nSyntax Error : incomplete array declaration  at line {tokens[current_token][2]} "
                        break
                else:
                    Error_list += f"\nSyntax Error : incomplete statement  at line {tokens[current_token][2]}"
                    break






        elif tokens[current_token][0] == 'ARRAY':  # Array syntax 2
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "ASSIGN":
                if (current_token + 2) < len(tokens) and (tokens[current_token + 2][0] == "IDENTIFIER" or tokens[current_token + 2][0] == "INTEGER" or tokens[current_token + 2][0] == "STRING" or tokens[current_token + 2][0] == "FLOATING_POINT" or tokens[current_token + 2][0] == "CHAR"):
                    array_name = tokens[current_token][1]
                    array_value = tokens[current_token + 2][1]
                    match = re.search(r'\[\s*([a-zA-Z_][a-zA-Z0-9_])+\s*\]', array_name)
                    if match:
                        print(f"ARRAY_INITIALIZATION:  {array_name}  =  {array_value}")
                        parser_tree.append(('ARRAY_INITIALIZATION', ("array_name", array_name), ("array_value", array_value)))
                        current_token += 2
                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "SEMICOLON":
                            current_token += 1
                        else:
                            Error_list += f"\nSyntax Error : Statement not terminated proper. missing a semicolon at line  {tokens[current_token][2]}"
                    else:
                        current_token += 2
                        Error_list += f"\nSyntax Error : Array initialization error. array index not specified at line  {tokens[current_token][2]}"
                else:
                    current_token += 1
                    Error_list += f"\nSyntax Error : Array element value error. wrong value is being assigned to the array at line  {tokens[current_token][2]}"




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
                        parser_tree.append(('function_assignment', ("IDENTIFIER", name), ("f_name", f_name), ('param', tuple(param_node))))
                        current_token += 1
                    else:
                        print(f"FUNCTION ASSIGNMENT: {name} {asg} {f_name} {l_p} {f_parameter} {r_p} <missing ';'>")
                        parser_tree.append(('function_assignment', ("IDENTIFIER", name), ("f_name", f_name), ('param', tuple(param_node))))
                        print("Syntax error: function-call-assignment statement.  missing statement terminator at line at line ", tokens[current_token][2])


                elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'MEMORY_REFERENCE':  # pointer assignment statement
                    print(f"POINTER_ASSIGNMENT:  {name} {asg} {tokens[current_token + 2][1]}")
                    parser_tree.append(('POINTER_ASSIGNMENT', ("pointer_name", name), ("pointer_value", tokens[current_token + 2][1])))
                    current_token += 2
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'SEMICOLON':
                        current_token += 1
                    else:
                        Error_list += f"\nSyntax Error: statement terminator missing at line {tokens[current_token][2]}"

                else:  # variable assignment statement
                    current_token, express, exp_node = expression(tokens, current_token + 1)
                    express_n = ''
                    if len(express) != 0:
                        if current_token < len(tokens) and tokens[current_token][0] != "SEMICOLON":
                            Error_list += f"\nSyntax Error: statement terminator missing at line {tokens[current_token - 1][2]}"
                            print(f"VARIABLE_ASSIGNMENT: {name} {asg} {express}")
                            parser_tree.append(('VARIABLE_ASSIGNMENT', ("IDENTIFIER", f"{name}"), ("expression", tuple(exp_node))))
                        elif current_token < len(tokens) and tokens[current_token][0] == "SEMICOLON":
                            print(f"VARIABLE_ASSIGNMENT: {name} {asg} {express} {tokens[current_token][1]}")
                            parser_tree.append(('VARIABLE_ASSIGNMENT', ("IDENTIFIER", f"{name}"), ("expression", tuple(exp_node))))
                        else:
                            Error_list += f"\nSyntax Error: statement terminator missing at line {tokens[current_token - 1][2]}"
                            print(f"VARIABLE_ASSIGNMENT: {name} {asg} {express}  <missing ';'>")
                            parser_tree.append(('VARIABLE_ASSIGNMENT', ("IDENTIFIER", f"{name}"), ("expression", tuple(exp_node))))
                    else:
                        Error_list += f"\nSyntax Error: variable assignment error, no value was assigned {tokens[current_token - 1][2]}"
                        if tokens[current_token][0] == "SEMICOLON":
                            s_tm = tokens[current_token][1]
                            print(f"VARIABLE_ASSIGNMENT: {name} {asg} {None} {s_tm}")

            elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'LEFT_PAREN':  # function call
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
            else:
                Error_list += f"\nSyntax Error: incomplete statement at line {tokens[current_token][2]}"



        elif tokens[current_token][0] == 'STRUCT_KEY':  # Structure
            struct_members_node = []
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'IDENTIFIER':
                structure_name = tokens[current_token + 1][1]
                if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'LEFT_BRACE':
                    current_token += 2
                    while True:
                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'KEYWORD':
                            if (current_token + 2) < len(tokens) and (tokens[current_token + 2][0] == 'IDENTIFIER' or tokens[current_token + 2][0] == 'ARRAY'):
                                struct_members_node.append(('struct_member', ('member_data_type', tokens[current_token + 1][1]), ('member_name', tokens[current_token + 2][1])))
                                current_token += 2
                                if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'SEMICOLON':
                                    current_token += 1
                                else:
                                    Error_list += f"\nSyntax error: unterminated structure member statement  at line {tokens[current_token][2]}"
                            else:
                                Error_list += f"\nSyntax error: incorrect structure member definition. structure member is defined incorrectly at line {tokens[current_token][2]}"
                                break

                        elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'STRUCT_KEY':  # nested struct
                            if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'IDENTIFIER':
                                if (current_token + 3) < len(tokens) and tokens[current_token + 3][0] == 'IDENTIFIER':
                                    struct_members_node.append(('nested_struct_member', ('struct_name', tokens[current_token + 2][1]), ('member_name', tokens[current_token + 3][1])))
                                    current_token += 3
                                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'SEMICOLON':
                                        current_token += 1
                                    else:
                                        Error_list += f"\nSyntax error: unterminated nested structure member statement at line {tokens[current_token][2]}"
                                else:
                                    current_token += 2
                                    Error_list += f"\nSyntax error:  nested structure member defined incorrectly at line {tokens[current_token][2]}"
                            else:
                                current_token += 1
                                Error_list += f"\nSyntax error: incomplete nested structure member definition at line {tokens[current_token][2]}"


                        elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'RIGHT_BRACE':
                            if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'SEMICOLON':
                                parser_tree.append(("STRUCTURE_DEFINITION", ('structure_name', structure_name), ('structure_members', tuple(struct_members_node))))
                                current_token += 2
                                break

                            elif (current_token + 2) < len(tokens) and (tokens[current_token + 2][0] == 'IDENTIFIER' or tokens[current_token + 2][0] == 'ARRAY'):
                                parser_tree.append(("STRUCTURE_DEFINITION", ('structure_name', structure_name), ('structure_members', tuple(struct_members_node))))
                                current_token += 2
                                while True:
                                    if current_token < len(tokens) and (tokens[current_token][0] == 'IDENTIFIER' or tokens[current_token][0] == 'ARRAY'):
                                        structure_variable = tokens[current_token][1]
                                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "SEMICOLON":
                                            parser_tree.append(("STRUCTURE_VARIABLE", ('structure_name', structure_name), ('structure_variable', structure_variable)))
                                            current_token += 1
                                            break

                                        elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "COMMA":
                                            parser_tree.append(("STRUCTURE_VARIABLE", ('structure_name', structure_name), ('structure_variable', structure_variable)))
                                            current_token += 1
                                        else:
                                            Error_list += f"\nSyntax error: incorrect statement  at line {tokens[current_token][2]}"
                                            current_token += 1
                                            break
                                        current_token += 1
                                    else:
                                        Error_list += f"\nSyntax error: incomplete statement at line {tokens[current_token][2]}"
                                        break

                                break
                            else:
                                current_token += 1
                                Error_list += f"\nSyntax error: unterminated structure  statement. missing semicolon  at line {tokens[current_token][2]}"
                                break
                        else:
                            Error_list += f"\nSyntax error: unidentified error at line {tokens[current_token][2]}"

                            break

                elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'IDENTIFIER':  # struct Variables
                    parser_tree.append(("STRUCTURE_VARIABLE", ('structure_name', structure_name), ('structure_variable', tokens[current_token + 2][1])))
                    current_token += 2
                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'SEMICOLON':
                        current_token += 1
                    else:
                        Error_list += f"\nSyntax error: unterminated statement. missing semicolon  at line {tokens[current_token][2]}"

        elif tokens[current_token][0] == 'ENUMERATION_KEY':  # Enumerated Type Declaration
            constants_node = []
            if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'IDENTIFIER':
                enumeration_name = tokens[current_token + 1][1]
                if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'LEFT_BRACE':
                    current_token += 2
                    while True:
                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'IDENTIFIER':
                            if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'ASSIGN':
                                if (current_token + 3) < len(tokens) and tokens[current_token + 3][0] == 'INTEGER':
                                    constants_node.append(('enumeration_member', ('constant_name', tokens[current_token + 1][1]), ('constant_value', tokens[current_token + 3][1])))
                                    current_token += 3
                                    if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'COMMA':
                                        current_token += 1
                                    else:
                                        Error_list += f"\nSyntax error: missing comma  at line {tokens[current_token][2]}"
                                else:
                                    Error_list += f"\nSyntax error: incorrect structure member definition. structure member is defined incorrectly at line {tokens[current_token][2]}"
                                    break
                        elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == 'RIGHT_BRACE':
                            if (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'SEMICOLON':
                                parser_tree.append(("ENUMERATION_DEFINITION", ('enumeration_name', enumeration_name), 'enumeration_constants', tuple(constants_node)))
                                current_token += 2
                                break

                            elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'IDENTIFIER':
                                parser_tree.append(("ENUMERATION_DEFINITION", ('enumeration_name', enumeration_name), 'enumeration_constants', tuple(constants_node)))
                                current_token += 2
                                while True:
                                    if current_token < len(tokens) and (tokens[current_token][0] == 'IDENTIFIER'):
                                        structure_variable = tokens[current_token][1]
                                        if (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "SEMICOLON":
                                            parser_tree.append(("ENUMERATION_VARIABLE", ('enumeration_name', enumeration_name), ('enumeration_variable', structure_variable)))
                                            current_token += 1
                                            break

                                        elif (current_token + 1) < len(tokens) and tokens[current_token + 1][0] == "COMMA":
                                            parser_tree.append(("ENUMERATION_VARIABLE", ('enumeration_name', enumeration_name), ('enumeration_variable', structure_variable)))
                                            current_token += 1
                                        else:
                                            Error_list += f"\nSyntax error: incorrect statement  at line {tokens[current_token][2]}"
                                            current_token += 1
                                            break
                                        current_token += 1
                                    else:
                                        Error_list += f"\nSyntax error: incomplete statement at line {tokens[current_token][2]}"
                                        break
                                break
                elif (current_token + 2) < len(tokens) and tokens[current_token + 2][0] == 'IDENTIFIER':
                    parser_tree.append(("ENUMERATION_VARIABLE", ('enumeration_name', enumeration_name), ('enumeration_variable', tokens[current_token + 2][1])))
                    if (current_token + 3) < len(tokens) and tokens[current_token + 3][0] == 'SEMICOLON':
                        current_token += 3
                    else:
                        Error_list += f"\nSyntax error: unterminated  statement at line {tokens[current_token][2]}"
                        current_token += 2
                else:
                    Error_list += f"\nSyntax error: incorrect enumeration declaration statement at line {tokens[current_token][2]}"
                    current_token += 1
            else:
                Error_list += f"\nSyntax error: at statement at line {tokens[current_token][2]}"





















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


print("\n\n=============================================== PARSER TREE OUTPUT =============================================================================== \n\n")
start_run_time_time = time.time()  # Record the Start run time-time of Syntax_analyzer
parse_program(tokens, 0)  # calling the parser function and passing token list
End_run_time_time = time.time()  # Record the End run time-time of Syntax_analyzer
Program_Run_time = End_run_time_time - start_run_time_time  # Calculate the elapsed time (run time of parser function)
print(f"\nParser Program Runtime  :  {Program_Run_time} seconds")

print(Error_list)  # print out syntax error caught by the parser

print("\n=================================================  PARSER LIST  ========================================================================================= \n")
print(parser_tree)  # print out the parser tree in list for that will be passed to the intermediate code generotor error caught by the parser
