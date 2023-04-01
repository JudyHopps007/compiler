from antlr4 import *
from CLexer import CLexer
from CParser import CParser
from lexical_Analyzer import lexical_analyzer


tokens = lexical_analyzer("program.c")  # get the list of tokens from the lexical analyzer
lexer = CLexer(InputStream(' '.join([t[1] for t in tokens])))  # create a lexer instance from the token list

# create a CommonTokenStream from the lexer
stream = CommonTokenStream(lexer)
stream.fill()

# print the token list
for token in stream.tokens:
    print('g===-', token)

parser = CParser(stream)  # create a parser instance from the token stream

# call the appropriate method on the parser to parse the input
tree = parser.program()

# print the parse tree
print(tree.toStringTree(recog=parser))
