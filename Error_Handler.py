import lexical_Analyzer

tokens = lexical_Analyzer.lexical_analyzer('program.c')

import re  # generate regular expression
import time  # measure the run time
import json
from pyparsing import *


# Define regular expression patterns for different types of tokens(assigning tokens to lexemes)
patterns_rg = [
    (r'#include', 'INCLUDE_ID'),
    (r'<[A-Za-z]+.h>', 'INCLUDE_DIRECTIVE'),
    (r'\b(int|void|char|bool|float|long|return)\b', 'KEYWORD'),
    (r'\b(if)\b', 'if'),
    (r'\b(else)\b', 'else'),
    (r'\b(while)\b', 'while'),
    (r'\b(true|false)\b', 'BOOLEAN'),
    (r'[0-9]+[.][0-9]+', 'floating_point'),
    (r'\b[0-9]+\b', 'integer'),
    (r"'.'", 'char'),
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

# Define grammar for the C programming language
identifier = Regex(r'[a-zA-Z_][a-zA-Z0-9_]*')
number = Regex(r'[0-9]+(\.[0-9]+)?')
string = Regex(r'\".*\"')
boolean = oneOf("true false")
type_name = oneOf("int char void bool float long")

expression = Forward()

# Define the various operations allowed in expressions
unary_op = oneOf("! -")
mult_op = oneOf("* / %")
add_op = oneOf("+ -")
rel_op = oneOf("< > <= >= == !=")
log_op = oneOf("&& ||")

primary_expression = (identifier | number | string | boolean | Group("(" + expression + ")"))

# Define expressions
postfix_expression = primary_expression + ZeroOrMore((Group("[" + expression + "]")) | (Group("." + identifier)) | (Group("->" + identifier)) | (Group("(" + Optional(delimitedList(expression)) + ")")))
unary_expression = Optional(unary_op) + postfix_expression
multiplicative_expression = unary_expression + ZeroOrMore((mult_op + unary_expression))
additive_expression = multiplicative_expression + ZeroOrMore((add_op + multiplicative_expression))
relational_expression = additive_expression + ZeroOrMore((rel_op + additive_expression))
equality_expression = relational_expression + ZeroOrMore((oneOf("
