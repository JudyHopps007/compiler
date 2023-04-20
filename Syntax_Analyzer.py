from antlr4 import *  # managing the parser
from Syntax_DIR.C_grammarLexer import C_grammarLexer  # importing the C_grammarLexer file for c grammar
from Syntax_DIR.C_grammarParser import C_grammarParser  # importing the parser file for syntax check
from lexical_Analyzer import lexical_analyzer  # importing the lexical_Analyzer file for token_list feed
import time  # time library to measure run parser run time
import Error_Handler  # importing the Error_Handler file  for syntax Error output feedback

print(" \n \n \n")
tokens_list = lexical_analyzer("program.c")  # get the list of tokens from the lexical analyzer

from collections import deque


def print_parse_tree(parse_tree_string: str, prefix: str = '', is_last: bool = True) -> None:
    tokens = deque(parse_tree_string.split("()"))
    node = tokens.popleft()
    print(f"{prefix}{'└── ' if is_last else '├── '}{node}")

    def print_children(tokens, prefix):
        while tokens:
            node = tokens.popleft()
            if '(' in node:
                print_parse_tree(' '.join(tokens), prefix + ('    ' if len(tokens) == 1 else '│   '), tokens[-1] == node)
                break
            else:
                print(f"{prefix}{'└── ' if not tokens else '├── '}{node}")

    if any('(' in node for node in tokens):
        print_children(tokens, prefix)
    else:
        while tokens:
            print(f"{prefix}└── {tokens.popleft().replace('(', '').replace(')', '')}")


def Syntax_Analyzer(token_list):
    lexer = C_grammarLexer(InputStream(' '.join([t[1] for t in token_list])))  # create a lexer instance from the token list
    stream = CommonTokenStream(lexer)  # create a CommonTokenStream from the lexer

    parser = C_grammarParser(stream)  # create a parser instance from the token stream
    parser.removeErrorListeners()
    tree = parser.program()  # call the appropriate method on the parser to parse the input
    Error_Handler.syntax_error_check()  # checking for syntax error
    return tree.toStringTree(recog=parser)  # return the parse tree


start_run_time_time = time.time()  # Record the Start run time-time of Syntax_analyzer
parser_tree = Syntax_Analyzer(tokens_list)  # calling the parser function and passing token list
End_run_time_time = time.time()  # Record the End run time-time of lexical_analyzer
Program_Run_time = End_run_time_time - start_run_time_time  # Calculate the elapsed time (run time of lexical_analyzer function)
print(f"\nParser Program Runtime  :  {Program_Run_time} seconds")

print('\n================ ============= PARSER TREE ============================== ==================\n')
print(parser_tree)

print('\n================ ============= PARSER TREE STRUCTURE ==================== ==================\n')
print_parse_tree(parser_tree)
