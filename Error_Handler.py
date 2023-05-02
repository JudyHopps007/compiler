from Syntax_DIR.C_grammarLexer import C_grammarLexer  # import lexer for token feed
from Syntax_DIR.C_grammarParser import C_grammarParser  # import parser file  for syntax function feed
from antlr4 import * # importing antlr library for addition methods


def Syntax_Analyzer(token_list):
    input_file = FileStream("program.c")
    lexer = C_grammarLexer(input_file)
    stream = CommonTokenStream(lexer)  # create a CommonTokenStream from the lexer

    parser = C_grammarParser(stream)  # create a parser instance from the token stream
    parser.removeErrorListeners()
    tree = parser.program()  # call the appropriate method on the parser to parse the input
    return tree.toStringTree(recog=parser)  # return the parse tree