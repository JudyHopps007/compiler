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

# Define a visitor class to traverse the parse tree
class CVisitor(NodeVisitor):
    def visit_program(self, node, children):
        return children

    def visit_declaration(self, node, children):
        return ("declaration", children[0], children[1])

    def visit_type(self, node, children):
        return node.text

    def visit_identifier(self, node, children):
        return ("identifier", node.text)

    def visit_statement(self, node, children):
        return ("statement", children[0])

    def visit_expression(self, node, children):
        return ("expression", children)

    def visit_term(self, node, children):
        return ("term", children)

    def visit_factor(self, node, children):
        if len(children) == 1:
            return children[0]
        else:
            return ("expression", children[1])

    def visit_integer(self, node, children):
        return ("integer", int(node.text))

    def visit_float(self, node, children):
        return ("float", float(node.text))

    def visit_char(self, node, children):
        return ("char", node.text.strip("'"))

    def visit_bool(self, node, children):
        return ("bool", node.text)

    def visit_add_op(self, node, children):
        return node.text

    def visit_mul_op(self, node, children):
        return node.text

# Define a function to parse a list of tokens
def parse_tokens(tokens):
    # Combine the tokens into a single string
    input_string = ""
    for token in tokens:
        input_string += token[1] + " "

    # Parse the input string using the grammar
    parse_tree = grammar.parse(input_string)

    # Use the visitor class to traverse the parse tree and generate the output
    visitor = CVisitor()
    output = visitor.visit(parse_tree)

    return output


import lexical_Analyzer
import json
tokens = lexical_Analyzer.lexical_analyzer('program.c')

#output = parse_tokens(tokens)
#print(json.dumps(output, indent=4))