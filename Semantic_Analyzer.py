import re

# Define a regular expression pattern for C comments
comment_pattern = r'//.*$|/\*.*?\*/'

# Read the C program from a file
with open('program.c', 'r') as f:
    program = f.read()

# Remove comments from the program
program_without_comments = re.sub(comment_pattern, '', program, flags=re.DOTALL | re.MULTILINE)

# Print the program without comments
print(program_without_comments)