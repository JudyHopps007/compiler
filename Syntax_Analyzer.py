from typing import List, Tuple

# Define a function to parse a single production rule
def parse_rule(rule: str) -> Tuple[str, List[str]]:
    lhs, rhs = rule.split(" -> ")
    rhs = rhs.split(" | ")
    rhs = [r.split() for r in rhs]
    return lhs, rhs

# Define a function to read production rules from a text file
def read_rules(filename: str) -> List[Tuple[str, List[str]]]:
    with open(filename) as f:
        rules = [parse_rule(line.strip()) for line in f if line.strip()]
    return rules

# Define a function to find all rules that have a given nonterminal symbol on the left-hand side
def find_rules_by_lhs(rules: List[Tuple[str, List[str]]], nonterminal: str) -> List[Tuple[str, List[str]]]:
    return [r for r in rules if r[0] == nonterminal]

# Define a function to find all nonterminal symbols that appear in a given production rule
def find_nonterminals_in_rule(rule: Tuple[str, List[str]]) -> List[str]:
    return [s for s in rule[1] if s.isupper()]

# Define a function to find all nonterminal symbols that appear in a list of production rules
def find_nonterminals_in_rules(rules: List[Tuple[str, List[str]]]) -> List[str]:
    nonterminals = set()
    for rule in rules:
        nonterminals.update(find_nonterminals_in_rule(rule))
    return list(nonterminals)

# Define a function to parse a C program using the given production rules
def parse_c_program(program: str, rules: List[Tuple[str, List[str]]]) -> bool:
    def parse_symbol(symbol: str, rest_program: str) -> bool:
        if symbol.islower():  # Terminal symbol
            if rest_program.startswith(symbol):
                return True, rest_program[len(symbol):]
            else:
                return False, rest_program
        else:  # Nonterminal symbol
            symbol_rules = find_rules_by_lhs(rules, symbol)
            for rule in symbol_rules:
                success, new_program = parse_sequence(rule[1], rest_program)
                if success:
                    return True, new_program
            return False, rest_program

    def parse_sequence(sequence: List[str], rest_program: str) -> Tuple[bool, str]:
        if not sequence:  # Empty sequence
            return True, rest_program
        else:
            success, new_program = parse_symbol(sequence[0], rest_program)
            if success:
                return parse_sequence(sequence[1:], new_program)
            else:
                return False, rest_program

    # Start parsing with the 'program' nonterminal symbol
    success, remaining_program = parse_symbol('program', program)
    return success and not remaining_program.strip()

# Read the production rules from a text file
rules = read_rules('grammar.txt')

# Parse a C program using the given production rules
program = """
int main() {
    printf("Hello, world!");
    return 0;
}
"""
if parse_c_program(program, rules):
    print("Parsing succeeded.")
else:
    print("Parsing failed.")
