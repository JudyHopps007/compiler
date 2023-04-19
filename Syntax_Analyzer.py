from antlr4 import *
from Syntax_DIR.C_grammarLexer import C_grammarLexer
from Syntax_DIR.C_grammarParser import  C_grammarParser
from lexical_Analyzer import lexical_analyzer

print(" \n \n \n")
tokens = lexical_analyzer("program.c")  # get the list of tokens from the lexical analyzer

for t in tokens:
    print(t[1])

def Syntax_Analyzer(token_list):
    lexer = C_grammarLexer(InputStream(' '.join([t[1] for t in token_list])))  # create a lexer instance from the token list
    stream = CommonTokenStream(lexer)  # create a CommonTokenStream from the lexer
    stream.fill()

    #input_file = FileStream('program.c')
    #lexer = C_grammarLexer(input_file)
    #stream = CommonTokenStream(lexer)

    # print the token list
    for token in stream.tokens:
        print('g===-', token)

    parser = C_grammarParser(stream)  # create a parser instance from the token stream
    tree = parser.program() # call the appropriate method on the parser to parse the input
    return tree.toStringTree(recog=parser)  # return the parse tree


tree = Syntax_Analyzer(tokens)

print('\n================ Parser Tree ===================\n')
print(tree)