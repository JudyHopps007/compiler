from Syntax_DIR.C_grammarLexer import C_grammarLexer
from Syntax_DIR.C_grammarParser import C_grammarParser
from antlr4 import *

class MyErrorListener(ParseTreeListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"SYNTAX ERROR: Error at line {line} column {column}: {msg}")


def syntax_error_check():
    input_file = FileStream("program.c")
    lexer = C_grammarLexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = C_grammarParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())
    parser.program()  # call the appropriate method on the parser to parse the input
