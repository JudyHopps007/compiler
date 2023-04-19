import re
from lexical_Analyzer import lexical_analyzer

class Parser:
    def __init__(self, input_string):
        self.input_string = input_string
        self.index = 0
        self.tokens = lexical_analyzer(input_string)

    def print_token(self):
        for i in self.tokens:
            print(i)

    
    def parse(self):
        self.index = 0
        print("true")
        self.P()

    def match(self, expected_token_type):
        if self.index >= len(self.tokens):
            print('Unexpected end of input')
        token_type, token_value = self.tokens[self.index]
        print(token_type)
        if token_type != expected_token_type :
            print('Unexpected token: %s' % token_value )
        self.index += 1
        print("true")
        
    def match_value(self, expected_token_type,value):
        if self.index >= len(self.tokens):
            print('Unexpected end of input')
        token_type, token_value = self.tokens[self.index]
        print(token_value)
        if token_value != value and token_type == expected_token_type :
            print('Unexpected token value: %s' % token_value )
        self.index += 1
        print("true")

    def P(self):
        print("p")
        # self.iL()
        self.fL()
        # self.mF()

    def iL(self):
        if (self.index < len(self.tokens)) and ((self.tokens[self.index])[0] == 'INCLUDE_ID'):
            self.match('INCLUDE_ID')
            self.match('INCLUDE_DIRECTIVE')
            self.match('SEMICOLON')
            self.iL()
            

    def fL(self):
        self.fS()
        # self.fL()

    def types(self):
        if (self.index < len(self.tokens)) and self.tokens[self.index][0] == "KEYWORD":
            self.match('KEYWORD')

    def pL(self):
        self.dL()

    def dL(self):
        self.dS()
        while self.tokens[self.index] == ',':
            self.match(',')
            self.dS()

    def dS(self):
        self.types()
        self.match("IDENTIFIER")

    def fB(self):
        self.dL()
        self.sL()
    
    def sL():
        self.statement()
        self.sL()
    
        def statement(self):
        if self.tokens[self.index][1].startswith(('int', 'bool', 'float', 'char')):
            self.assign()
        elif self.tokens[self.index][1] == ('while'):
            self.while_loop()
        elif self.tokens[self.index][1] == ('if'):
            self.if_statement()
        elif self.tokens[self.index][1] == (('continue', 'break')):
            self.match("")
    def fS(self):
        self.types()
        self.match('IDENTIFIER')
        self.match("LEFT_PAREN")
        # self.pL()
        self.match("RIGHT_PAREN")
        self.match("LEFT_BRACE")
        self.fB()
        # self.match_value("KEYWORD","return")
        self.match("RIGHT_BRACE")
        # self.parse_fS()
        # self.parse_fL()



passed = "D:\parser\Compiler\program.c"
parse = Parser(passed)

parse.print_token()
# parse.parse()

