from antlr4 import *
from CLexer import CLexer
from CParser import CParser
from lexical_Analyzer import lexical_analyzer

tokens = lexical_analyzer("program.c")  # get the list of tokens from the lexical analyzer


def Syntax_Analyzer(token_list):
    lexer = CLexer(InputStream(' '.join([t[1] for t in token_list])))  # create a lexer instance from the token list
    stream = CommonTokenStream(lexer)  # create a CommonTokenStream from the lexer
    stream.fill()


    # print the token list
    for token in stream.tokens:
        print('g===-', token)

    parser = CParser(stream)  # create a parser instance from the token stream
    tree = parser.program() # call the appropriate method on the parser to parse the input
    return tree.toStringTree(recog=parser)  # return the parse tree


tree = Syntax_Analyzer(tokens)
print(tree)