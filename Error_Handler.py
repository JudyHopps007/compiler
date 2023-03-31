import lexical_Analyzer

tokens = lexical_Analyzer.lexical_analyzer('program.c')
from pyparsing import Word, alphas, nums, Literal, Group, ZeroOrMore, Forward, Suppress

# Define the grammar rules
identifier = Word(alphas + '_', alphas + nums + '_')
integer = Word(nums)
floating_point = Word(nums) + Literal('.') + Word(nums)
boolean = Literal('true') | Literal('false')
string = Literal('"') + ZeroOrMore(Word(alphas + nums)) + Literal('"')
char = Literal("'") + Word(alphas + nums) + Literal("'")
operator = Literal('+') | Literal('-') | Literal('*') | Literal('/') | Literal('%') | \
    Literal('==') | Literal('!=') | Literal('<') | Literal('>') | Literal('<=') | Literal('>=') | \
    Literal('=') | Literal('&&') | Literal('||') | Literal('!')
keyword = Literal('if') | Literal('else') | Literal('while') | Literal('return') | \
    Literal('int') | Literal('void') | Literal('char') | Literal('bool') | Literal('float') | Literal('long')

expression = Forward()
expression_list = Group(expression + ZeroOrMore(Suppress(',') + expression))
argument_list = Group(expression_list)
function_call = identifier + Suppress('(') + argument_list + Suppress(')')
factor = (integer | floating_point | boolean | string | char | function_call | identifier |
          Group(Suppress('(') + expression + Suppress(')')))
unary_expression = Group(operator + factor)
multiplicative_expression = Group(factor + ZeroOrMore((Literal('*') | Literal('/') | Literal('%')) + factor))
additive_expression = Group(multiplicative_expression + ZeroOrMore((Literal('+') | Literal('-')) + multiplicative_expression))
relational_expression = Group(additive_expression + ZeroOrMore((Literal('<') | Literal('>') | Literal('<=') | Literal('>=')) + additive_expression))
equality_expression = Group(relational_expression + ZeroOrMore((Literal('==') | Literal('!=')) + relational_expression))
logical_and_expression = Group(equality_expression + ZeroOrMore(Literal('&&') + equality_expression))
logical_or_expression = Group(logical_and_expression + ZeroOrMore(Literal('||') + logical_and_expression))
expression << logical_or_expression

assignment_expression = Group(identifier + Suppress('=') + expression)
expression_statement = Group(expression + Suppress(';'))
compound_statement = Group(Suppress('{') + ZeroOrMore(expression_statement) + Suppress('}'))
selection_statement = Group(Literal('if') + Suppress('(') + expression + Suppress(')') + compound_statement +
                             ZeroOrMore(Literal('else') + compound_statement))
iteration_statement = Group(Literal('while') + Suppress('(') + expression + Suppress(')') + compound_statement)
return_statement = Group(Literal('return') + expression + Suppress(';'))
statement = Forward()
statement << (expression_statement | compound_statement | selection_statement | iteration_statement | return_statement)
declaration = Group(keyword + identifier + Suppress(';'))
function_declaration = Group(keyword + identifier + Suppress('(') + argument_list + Suppress(')') + compound_statement)

program = ZeroOrMore(function_declaration | declaration | statement)

# Define a function to parse the list of tokens
def parse_tokens(tokens):
    try:
        program.parse(tokens)
        print('Parsing successful')
    except Exception as e:
        print('Parsing failed:', e)

parse_tokens(tokens)