import subprocess

# open a command prompt and execute a command
cmd = 'antlr4 -Dlanguage=Python3 C_grammar.g4'  # change this to the command you want to execute
print('Running .... \n ')
subprocess.run(cmd, shell=True)
print('\n.... completed .... ')

