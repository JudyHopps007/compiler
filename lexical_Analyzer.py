import re  # for generate regular expression
import time  # for measuring 'scanner' run time
import json  # for symbol table {access and storage}

print('\n')
# ====================================== LEXICAL ANALYZER PHASE =====================================================


# Define regular expression patterns for different types of tokens(assigning tokens to lexemes)
patterns_rg = [
    (r'(\/\/[^\n\r]*[\n\r])|\/\*[\s\S]*?\*\/', 'COMMENT'),
    (r'#include\b', 'INCLUDE_ID'),
    (r'<[A-Za-z/]+.h>', 'INCLUDE_DIRECTIVE'),
    (r'#(define|undef|if|elif|else|endif)\b', 'MACRO'),
    (r'#pragma\b', 'PRAGMA_DIRECTIVE'),
    (r'\b(int|void|char|bool|float|long|return)\b', 'KEYWORD'),
    (r'\b(const)\b', 'CONSTANT_KEY'),

    (r'\w+\[\s*\w*\s*\]', 'ARRAY'),
    (r'\*\w+\[\]', 'POINTER_TO_ARRAY'),
    (r'\*\w+', 'POINTER_TO_VAR'),
    (r'\bFILE |FILE\b\*', 'FILE_POINTER'),
    (r'\w+\.\w+', "STRUCTURE_MEMBER_ACCESS"),
    (r'&[a-zA-Z_][a-zA-Z0-9_]*.[a-zA-Z_][a-zA-Z0-9_]*', 'MEMORY_REFERENCE'),
    (r'\b(if)\b', 'IF'),
    (r'\b(else)\b', 'ELSE'),
    (r'\b(while)\b', 'WHILE'),
    (r'\b(true|false)\b', 'BOOLEAN'),
    (r'[0-9]+[.][0-9]+', 'FLOATING_POINT'),
    (r'\b[0-9]+\b', 'INTEGER'),
    (r"'.'", 'CHAR'),
    (r'\"(\\.|[^"])*\"', 'STRING'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'MULTIPLY'),
    (r'/(?![\/\*])[\n\s]*', 'DIVIDE'),
    (r'%', 'MODULUS'),
    (r'==', 'EQUAL'),
    (r'=', 'ASSIGN'),
    (r'!=', 'NOT_EQUAL'),
    (r'<=', 'LESS_THAN_EQUAL'),
    (r'<', 'LESS_THAN'),
    (r'>=', 'GREATER_THAN_EQUAL'),
    (r'>', 'GREATER_THAN'),
    (r'\(', 'LEFT_PAREN'),
    (r'\)', 'RIGHT_PAREN'),
    (r'\{', 'LEFT_BRACE'),
    (r'\}', 'RIGHT_BRACE'),
    (r';', 'SEMICOLON'),
    (r',', 'COMMA'),
    (r'\|\|', 'OR'),
    (r'\&\&', 'AND'),
    (r'\!', 'NOT'),
]


# ========= Define a function that reads a program from a  and generates a list of tokens ===
def scanner(program):

    line_number_track = 1  # keep track of lexical error position
    token_track = 1  # keep track of token position
    token_list = []  # initialized to empty list ( TOKEN_TYPE , TOKEN-VALUE )
    token_list2 = []  # initialized to empty list ( TOKEN_TYPE , TOKEN-VALUE, LINE-NUMBER )
    curser_position = 0  # initialized to zero
    while curser_position < len(program):
        match = None

        if program[curser_position] == '\n':  # Skip over empty lines
            line_number_track += 1  # incrementing line number
            curser_position += 1  # incrementing cursor position
            token_track += 1
            continue

        if re.match(r'\s', program[curser_position]):  # Skip over whitespace
            curser_position += 1
            continue

        for pattern, token_type in patterns_rg:
            regex = re.compile(pattern)
            match = regex.match(program, curser_position)
            # get rid of code comments logic skips over comment token_list
            if match:
                if token_type != 'COMMENT':
                    token_list.append((token_type, match.group(0)))  # adding found token in the token_list
                    token_list2.append((token_type, match.group(0), token_track))
                else:
                    token_track += 1
                    line_number_track += 1
                curser_position = match.end(0)
                break

        if not match:  # catch errors or illegal charachers that don't conform to the defined regular expressions
            print("LEXICAL ERROR -- Illegal character: " + program[curser_position], "at Line ", line_number_track)
            curser_position += 1  # incrementing cursor position
    return token_list2


