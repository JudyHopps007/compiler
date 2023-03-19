class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, symbol_type):
        if name in self.symbols:
            raise ValueError(f"Symbol '{name}' already exists in symbol table")
        self.symbols[name] = {'type': symbol_type}

    def get_symbol(self, name):
        symbol = self.symbols.get(name)
        if not symbol:
            raise ValueError(f"Symbol '{name}' not found in symbol table")
        return symbol

    def update_symbol(self, name, symbol_type):
        symbol = self.get_symbol(name)
        symbol['type'] = symbol_type

    def remove_symbol(self, name):
        if name not in self.symbols:
            raise ValueError(f"Symbol '{name}' not found in symbol table")
        del self.symbols[name]

    def print_table(self):
        for name, attributes in self.symbols.items():
            print(f"{name}: {attributes['type']}")

# Example usage
table = SymbolTable()
table.add_symbol('x', 'int')
table.add_symbol('y', 'float')
table.add_symbol('z', 'string')
table.print_table()
