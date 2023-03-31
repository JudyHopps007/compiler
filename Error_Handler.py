from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

# Define the grammar
grammar = Grammar(
    """
    program = (declaration / statement)*
    declaration = type identifier ";"
    type = "int" / "float" / "char" / "bool"
    identifier = ~"[a-zA-Z_][a-zA-Z0-9_]*"
    statement = expression ";"
    expression = term (add_op term)*
    term = factor (mul_op factor)*
    factor = identifier / integer / float / char / bool / "(" expression ")"
    integer = ~"[0-9]+"
    float = ~"[0-9]+.[0-9]+"
    char = ~"'[a-zA-Z0-9_?]*[\s]*'"
    bool = "true" / "false"
    add_op = "+" / "-"
    mul_op = "*" / "/" / "%"
    """
)

# Define a function to parse a list of tokens
def parse_tokens(tokens):
    # Combine the tokens into a single string
    input_string = ""
    for token in tokens:
        input_string += token[1] + " "

    # Parse the input string using the grammar
    parse_tree = grammar.parse(input_string)

    # Use the visitor class to traverse the parse tree and generate the output


    return output


import lexical_Analyzer
import json
tokens = lexical_Analyzer.lexical_analyzer('program.c')

#output = parse_tokens(tokens)
#print(json.dumps(output, indent=4))