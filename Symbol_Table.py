import lexical_Analyzer

tokens = lexical_Analyzer.lexical_analyzer('program.c')

import re
from lark import Lark, Transformer

patterns_rg = [
    (r'#include', 'INCLUDE_ID'),
    (r'<[A-Za-z]+.h>', 'INCLUDE_DIRECTIVE'),
    (r'\b(int|void|char|bool|float|long|return)\b', 'KEYWORD'),
    (r'\b(if)\b', 'if'),
    (r'\b(else)\b', 'else'),
    (r'\b(while)\b', 'while'),
    (r'\b(true|false)\b', 'BOOLEAN'),
    (r'[0-9]+[.][0-9]+', 'floating_point'),
    (r'\b[0-9]+\b', 'INTEGER'),
    (r"'.'", 'CHAR'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'MULTIPLY'),
    (r'(\/\/[^\n\r]*[\n\r])|\/\*[\s\S]*?\*\/', 'COMMENT'),
    (r'/(?![\/\*])[\n\s]*', 'DIVIDE'),
    (r'%', 'MODULUS'),
    (r'=', 'ASSIGN'),
    (r'==', 'EQUAL'),
    (r'!=', 'NOT_EQUAL'),
    (r'<', 'LESS_THAN'),
    (r'>', 'GREATER_THAN'),
    (r'<=', 'LESS_THAN_EQUAL'),
    (r'>=', 'GREATER_THAN_EQUAL'),
    (r'\(', 'LEFT_PAREN'),
    (r'\)', 'RIGHT_PAREN'),
    (r'\{', 'LEFT_BRACE'),
    (r'\}', 'RIGHT_BRACE'),
    (r';', 'SEMICOLON'),
    (r',', 'COMMA'),
    (r'\|\|', 'OR'),
    (r'\&\&', 'AND'),
    (r'\!', 'NOT'),
]

regex_patterns = '|'.join('(?P<{}>{})'.format(token_type, pattern) for pattern, token_type in patterns_rg)


grammar = """
    start: program

    program: (statement ";")*

    statement: "if" expression "{" program "}" ("else" "{" program "}")?
             | "while" expression "{" program "}"
             | "return" expression?
             | IDENTIFIER "=" expression
             | IDENTIFIER "(" parameters? ")"
             | declaration

    declaration: type IDENTIFIER ("=" expression)?

    parameters: expression ("," expression)*

    expression: expression "||" and_expression    -> or
              | and_expression

    and_expression: and_expression "&&" comparison -> and
                  | comparison

    comparison: comparison "==" addition   -> eq
              | comparison "!=" addition   -> neq
              | comparison "<" addition    -> lt
              | comparison ">" addition    -> gt
              | comparison "<=" addition   -> lte
              | comparison ">=" addition   -> gte
              | addition

    addition: addition "+" term     -> add
            | addition "-" term     -> sub
            | term

    term: term "*" factor         -> mul
        | term "/" factor         -> div
        | term "%" factor         -> mod
        | factor

    factor: "(" expression ")"
          | "-" factor            -> neg
          | "+" factor            -> pos
          | "!" factor            -> not
          | IDENTIFIER
          | NUMBER
          | STRING

    type: "int" | "void" | "char" | "bool" | "float" | "long"

    %import common.WS
    %import patterns_rg.IDENTIFIER
    %import patterns_rg.INTEGER
    %import patterns_rg.FLOAT
    %import patterns_rg.STRING
    %import patterns_rg.CHAR
    %import patterns_rg.BOOLEAN
    %import patterns_rg.PLUS
    %import patterns_rg.MINUS
    %import patterns_rg.MULTIPLY
    %import patterns_rg.DIVIDE
    %import patterns_rg.MODULUS
    %import patterns_rg.ASSIGN
    %import patterns_rg.EQUAL
    %import patterns_rg.NOT_EQUAL
    %import patterns_rg.LESS_THAN
    %import patterns_rg.GREATER_THAN
    %import patterns_rg.LESS_THAN_EQUAL
    %import patterns_rg.GREATER_THAN_EQUAL
    %import patterns_rg.LEFT_PAREN
    %import patterns_rg.RIGHT_PAREN
    %import patterns_rg.LEFT_BRACE
    %import patterns_rg.RIGHT_BRACE
    %import patterns_rg.SEMICOLON
    %import patterns_rg.COMMA
    %import patterns_rg.OR
    %import patterns_rg.AND
    %import patterns_rg.NOT
    %import patterns_rg.COMMENT

    %ignore COMMENT
    %ignore WS
"""