from pycparser import c_parser, c_ast

# Sample C program to parse
c_program = """

int main() {
    int x = 10;
    printf("x = %d", x);
    return 0;
}
"""

# Create a C parser object
parser = c_parser.CParser()

# Parse the C program into an AST (abstract syntax tree)
ast = parser.parse(c_program)

# Traverse the AST to extract symbol table information
class SymbolVisitor(c_ast.NodeVisitor):
    def __init__(self):
        self.symbols = {}

    def visit_Decl(self, node):
        # Extract symbol name and type
        symbol_name = node.name
        symbol_type = type(node.type).__name__

        # Add symbol to symbol table
        self.symbols[symbol_name] = symbol_type

# Create a symbol table visitor object and visit the AST
symbol_visitor = SymbolVisitor()
symbol_visitor.visit(ast)

# Print the symbol table
print(symbol_visitor.symbols)