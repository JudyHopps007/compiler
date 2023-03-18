import re

pattern = r'\b(integer|SEMICOLON)\b'
regex = re.compile(pattern)

tokens = ['integer', 'SEMICOLON', 'identifier', 'int', '10']
for token in tokens:
    if regex.match(token):
        print(f"{token} matches the pattern")
    else:
        print(f"{token} does not match the pattern")
