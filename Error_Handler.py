import lexical_Analyzer

tokens = lexical_Analyzer.lexical_analyzer('program.c')

import pyparsing as pp

# Define PyParsing grammar for C programming language
# We'll use some of the tokens defined in the patterns_rg list
# Here we define only a basic grammar for demonstration purposes

expression = pp.Forward()

integer = pp.Regex(r'[0-9]+').setParseAction(lambda t: int(t[0]))
floating_point = pp.Regex(r'[0-9]+\.[0-9]+').setParseAction(lambda t: float(t[0]))
boolean = pp.Regex(r'(true|false)').setParseAction(lambda t: True if t[0] == 'true' else False)
identifier = pp.Regex(r'[a-zA-Z_][a-zA-Z0-9_]*')

factor = pp.Group(integer | floating_point | boolean | identifier | '(' + expression + ')')
term = pp.infixNotation(factor, [
    (pp.oneOf('* / %'), 2, pp.opAssoc.LEFT),
])
expression << pp.infixNotation(term, [
    (pp.oneOf('+ -'), 2, pp.opAssoc.LEFT),
])

# Define a PyParsing grammar for a C program
# This will use the tokens defined in the patterns_rg list
program = pp.Forward()

include_statement = pp.Group('#include' + '<' + identifier + '.h>' + ';')
statement = pp.Group(expression + ';')
statements = pp.Group(pp.OneOrMore(statement))
if_statement = pp.Group('if' + '(' + expression + ')' + '{' + statements + '}' + pp.Optional('else' + '{' + statements + '}'))
while_loop = pp.Group('while' + '(' + expression + ')' + '{' + statements + '}')
function = pp.Group(pp.Optional('int' | 'void' | 'char' | 'bool' | 'float' | 'long') + identifier + '(' + pp.Optional(pp.delimitedList(identifier)) + ')' + '{' + statements + '}')

program << pp.Group(include_statement | if_statement | while_loop | function)

# Define a function that checks a list of tokens for syntax errors using PyParsing
def parse_tokens(tokens):
    try:
        program.parseString(tokens)
        print('No syntax errors found')
    except pp.ParseException as e:
        print(f'Syntax error: {e}')


parse_tokens(tokens)