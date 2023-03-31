from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

# Define the grammar
grammar = Grammar(
    """
    program = (declaration / statement)*
    declaration = identifier
    identifier = ~"[a-zA-Z_][a-zA-Z0-9_]*"
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


import lexical_Analyzer

tokens = lexical_Analyzer.lexical_analyzer('program.c')
