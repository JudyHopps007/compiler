import re

# Define the grammar rules using regular expressions
program_regex = re.compile(r'^<statement>(<statement>)?$')
statement_regex = re.compile(r'^<assignment>|<print>|<if>|<while>$')
assignment_regex = re.compile(r'^<identifier>=<expression>;$')
expression_regex = re.compile(r'^<term>(<addop><expression>)?$')
term_regex = re.compile(r'^<factor>(<mulop><term>)?$')
factor_regex = re.compile(r'^<identifier>|<number>|\(<expression>\)$')
addop_regex = re.compile(r'^\+|\-$')
mulop_regex = re.compile(r'^\*|\/$')
print_regex = re.compile(r'^printf\("<string>"\);$')
string_regex = re.compile(r'^"[^"\\]*(\\.[^"\\]*)*"$')
if_regex = re.compile(r'^if\(<condition>\)<statement>(else<statement>)?$')
condition_regex = re.compile(r'^<expression><relop><expression>$')
relop_regex = re.compile(r'^==|!=|<|<=|>|>=$')
while_regex = re.compile(r'^while\(<condition>\)<statement>$')

# Define a function to parse a sentence
def parse(sentence):
    if program_regex.match(sentence):
        statements = sentence.split()
        for statement in statements:
            if statement_regex.match(statement):
                if assignment_regex.match(statement):
                    identifier, expression = statement.split('=')
                    identifier = identifier.strip()
                    expression = expression.strip()
                    if identifier_regex.match(identifier) and expression_regex.match(expression):
                        continue
                elif print_regex.match(statement):
                    string = string_regex.search(statement).group(0)
                    if string:
                        continue
                elif if_regex.match(statement):
                    condition, if_statement, else_statement = if_regex.search(statement).groups()
                    if condition_regex.match(condition) and statement_regex.match(if_statement) and statement_regex.match(else_statement):
                        continue
                    elif condition_regex.match(condition) and statement_regex.match(if_statement):
                        continue
                elif while_regex.match(statement):
                    condition, while_statement = while_regex.search(statement).groups()
                    if condition_regex.match(condition) and statement_regex.match(while_statement):
                        continue
            raise SyntaxError(f'Invalid statement: {statement}')
    else:
        #raise SyntaxError(f'Invalid program: {sentence}')
        pass
    return True

# Example usage
program = '''
x = 2 + 3;
printf("Hello, world!");
if (x > 5) x = x - 5; else x = x + 5;
while (x < 10) x = x + 1;
'''
parse(program)
