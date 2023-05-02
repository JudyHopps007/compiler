# Generated from C_grammar.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,195,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,5,
        0,42,8,0,10,0,12,0,45,9,0,1,0,3,0,48,8,0,1,1,1,1,1,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,5,1,5,5,5,77,8,5,10,5,12,5,80,9,5,3,5,82,8,5,1,6,1,
        6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,95,8,7,10,7,12,7,98,9,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,108,8,8,1,9,1,9,1,9,1,9,1,
        9,5,9,115,8,9,10,9,12,9,118,9,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,5,11,144,8,11,10,11,12,11,147,9,11,1,11,1,11,
        1,11,1,11,1,11,3,11,154,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,3,13,169,8,13,1,14,1,14,1,14,1,14,
        1,15,1,15,1,15,1,15,5,15,179,8,15,10,15,12,15,182,9,15,1,15,1,15,
        1,15,3,15,187,8,15,1,16,1,16,1,17,1,17,1,18,1,18,1,18,0,0,19,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,3,1,0,31,33,1,
        0,15,21,1,0,22,28,197,0,43,1,0,0,0,2,49,1,0,0,0,4,52,1,0,0,0,6,59,
        1,0,0,0,8,66,1,0,0,0,10,81,1,0,0,0,12,83,1,0,0,0,14,96,1,0,0,0,16,
        107,1,0,0,0,18,109,1,0,0,0,20,122,1,0,0,0,22,128,1,0,0,0,24,155,
        1,0,0,0,26,168,1,0,0,0,28,170,1,0,0,0,30,186,1,0,0,0,32,188,1,0,
        0,0,34,190,1,0,0,0,36,192,1,0,0,0,38,42,3,2,1,0,39,42,3,8,4,0,40,
        42,3,4,2,0,41,38,1,0,0,0,41,39,1,0,0,0,41,40,1,0,0,0,42,45,1,0,0,
        0,43,41,1,0,0,0,43,44,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,46,48,
        3,6,3,0,47,46,1,0,0,0,47,48,1,0,0,0,48,1,1,0,0,0,49,50,5,1,0,0,50,
        51,5,34,0,0,51,3,1,0,0,0,52,53,3,36,18,0,53,54,5,31,0,0,54,55,5,
        2,0,0,55,56,3,10,5,0,56,57,5,3,0,0,57,58,3,12,6,0,58,5,1,0,0,0,59,
        60,3,36,18,0,60,61,5,4,0,0,61,62,5,2,0,0,62,63,3,10,5,0,63,64,5,
        3,0,0,64,65,3,12,6,0,65,7,1,0,0,0,66,67,3,36,18,0,67,68,5,31,0,0,
        68,69,5,5,0,0,69,9,1,0,0,0,70,71,3,36,18,0,71,78,5,31,0,0,72,73,
        5,6,0,0,73,74,3,36,18,0,74,75,5,31,0,0,75,77,1,0,0,0,76,72,1,0,0,
        0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,82,1,0,0,0,80,78,
        1,0,0,0,81,70,1,0,0,0,81,82,1,0,0,0,82,11,1,0,0,0,83,84,5,7,0,0,
        84,85,3,14,7,0,85,86,5,8,0,0,86,13,1,0,0,0,87,95,3,8,4,0,88,95,3,
        20,10,0,89,95,3,18,9,0,90,95,3,16,8,0,91,95,3,22,11,0,92,95,3,24,
        12,0,93,95,3,28,14,0,94,87,1,0,0,0,94,88,1,0,0,0,94,89,1,0,0,0,94,
        90,1,0,0,0,94,91,1,0,0,0,94,92,1,0,0,0,94,93,1,0,0,0,95,98,1,0,0,
        0,96,94,1,0,0,0,96,97,1,0,0,0,97,15,1,0,0,0,98,96,1,0,0,0,99,100,
        5,31,0,0,100,101,5,9,0,0,101,102,3,30,15,0,102,103,5,5,0,0,103,108,
        1,0,0,0,104,105,5,31,0,0,105,106,5,9,0,0,106,108,3,18,9,0,107,99,
        1,0,0,0,107,104,1,0,0,0,108,17,1,0,0,0,109,110,5,31,0,0,110,111,
        5,2,0,0,111,116,3,30,15,0,112,113,5,6,0,0,113,115,3,30,15,0,114,
        112,1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,
        119,1,0,0,0,118,116,1,0,0,0,119,120,5,3,0,0,120,121,5,5,0,0,121,
        19,1,0,0,0,122,123,3,36,18,0,123,124,5,31,0,0,124,125,5,9,0,0,125,
        126,3,30,15,0,126,127,5,5,0,0,127,21,1,0,0,0,128,129,5,10,0,0,129,
        130,5,2,0,0,130,131,3,26,13,0,131,132,5,3,0,0,132,133,5,7,0,0,133,
        134,3,14,7,0,134,145,5,8,0,0,135,136,5,11,0,0,136,137,5,2,0,0,137,
        138,3,26,13,0,138,139,5,3,0,0,139,140,5,7,0,0,140,141,3,14,7,0,141,
        142,5,8,0,0,142,144,1,0,0,0,143,135,1,0,0,0,144,147,1,0,0,0,145,
        143,1,0,0,0,145,146,1,0,0,0,146,153,1,0,0,0,147,145,1,0,0,0,148,
        149,5,12,0,0,149,150,5,7,0,0,150,151,3,14,7,0,151,152,5,8,0,0,152,
        154,1,0,0,0,153,148,1,0,0,0,153,154,1,0,0,0,154,23,1,0,0,0,155,156,
        5,13,0,0,156,157,5,2,0,0,157,158,3,26,13,0,158,159,5,3,0,0,159,160,
        5,7,0,0,160,161,3,14,7,0,161,162,5,8,0,0,162,25,1,0,0,0,163,164,
        3,30,15,0,164,165,5,29,0,0,165,166,3,30,15,0,166,169,1,0,0,0,167,
        169,5,31,0,0,168,163,1,0,0,0,168,167,1,0,0,0,169,27,1,0,0,0,170,
        171,5,14,0,0,171,172,3,30,15,0,172,173,5,5,0,0,173,29,1,0,0,0,174,
        180,3,32,16,0,175,176,3,34,17,0,176,177,3,32,16,0,177,179,1,0,0,
        0,178,175,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,
        0,181,187,1,0,0,0,182,180,1,0,0,0,183,187,5,35,0,0,184,187,5,36,
        0,0,185,187,5,37,0,0,186,174,1,0,0,0,186,183,1,0,0,0,186,184,1,0,
        0,0,186,185,1,0,0,0,187,31,1,0,0,0,188,189,7,0,0,0,189,33,1,0,0,
        0,190,191,7,1,0,0,191,35,1,0,0,0,192,193,7,2,0,0,193,37,1,0,0,0,
        14,41,43,47,78,81,94,96,107,116,145,153,168,180,186
    ]

class C_grammarParser ( Parser ):

    grammarFileName = "C_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#include'", "'('", "')'", "'main'", 
                     "';'", "','", "'{'", "'}'", "'='", "'if'", "'else if'", 
                     "'else'", "'while'", "'return'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'&&'", "'||'", "'int'", "'float'", "'char'", 
                     "'double'", "'void'", "'bool'", "'long'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "CONDITIONAL_OPERATOR", "LOGICAL_OPERATOR", 
                      "IDENTIFIER", "INTEGER", "FLOAT", "INCLUDE_DIRECTIVE", 
                      "CHAR_LITERAL", "STRING_LITERAL", "BOOLEAN", "SING_LINE_COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_include_list = 1
    RULE_function = 2
    RULE_main_function = 3
    RULE_declaration = 4
    RULE_params = 5
    RULE_compound_statement = 6
    RULE_statement = 7
    RULE_assignment = 8
    RULE_function_call = 9
    RULE_initializing = 10
    RULE_if_statement = 11
    RULE_while_statement = 12
    RULE_condition_statement_RFC = 13
    RULE_return_statement = 14
    RULE_expression = 15
    RULE_term = 16
    RULE_operator = 17
    RULE_type_specifier = 18

    ruleNames =  [ "program", "include_list", "function", "main_function", 
                   "declaration", "params", "compound_statement", "statement", 
                   "assignment", "function_call", "initializing", "if_statement", 
                   "while_statement", "condition_statement_RFC", "return_statement", 
                   "expression", "term", "operator", "type_specifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    CONDITIONAL_OPERATOR=29
    LOGICAL_OPERATOR=30
    IDENTIFIER=31
    INTEGER=32
    FLOAT=33
    INCLUDE_DIRECTIVE=34
    CHAR_LITERAL=35
    STRING_LITERAL=36
    BOOLEAN=37
    SING_LINE_COMMENT=38
    WS=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def include_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.Include_listContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.Include_listContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.DeclarationContext,i)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.FunctionContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.FunctionContext,i)


        def main_function(self):
            return self.getTypedRuleContext(C_grammarParser.Main_functionContext,0)


        def getRuleIndex(self):
            return C_grammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = C_grammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 41
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 38
                        self.include_list()
                        pass

                    elif la_ == 2:
                        self.state = 39
                        self.declaration()
                        pass

                    elif la_ == 3:
                        self.state = 40
                        self.function()
                        pass

             
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 532676608) != 0):
                self.state = 46
                self.main_function()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Include_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCLUDE_DIRECTIVE(self):
            return self.getToken(C_grammarParser.INCLUDE_DIRECTIVE, 0)

        def getRuleIndex(self):
            return C_grammarParser.RULE_include_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInclude_list" ):
                listener.enterInclude_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInclude_list" ):
                listener.exitInclude_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude_list" ):
                return visitor.visitInclude_list(self)
            else:
                return visitor.visitChildren(self)




    def include_list(self):

        localctx = C_grammarParser.Include_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_include_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(C_grammarParser.T__0)
            self.state = 50
            self.match(C_grammarParser.INCLUDE_DIRECTIVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specifier(self):
            return self.getTypedRuleContext(C_grammarParser.Type_specifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(C_grammarParser.IDENTIFIER, 0)

        def params(self):
            return self.getTypedRuleContext(C_grammarParser.ParamsContext,0)


        def compound_statement(self):
            return self.getTypedRuleContext(C_grammarParser.Compound_statementContext,0)


        def getRuleIndex(self):
            return C_grammarParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = C_grammarParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.type_specifier()
            self.state = 53
            self.match(C_grammarParser.IDENTIFIER)
            self.state = 54
            self.match(C_grammarParser.T__1)
            self.state = 55
            self.params()
            self.state = 56
            self.match(C_grammarParser.T__2)
            self.state = 57
            self.compound_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specifier(self):
            return self.getTypedRuleContext(C_grammarParser.Type_specifierContext,0)


        def params(self):
            return self.getTypedRuleContext(C_grammarParser.ParamsContext,0)


        def compound_statement(self):
            return self.getTypedRuleContext(C_grammarParser.Compound_statementContext,0)


        def getRuleIndex(self):
            return C_grammarParser.RULE_main_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_function" ):
                listener.enterMain_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_function" ):
                listener.exitMain_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_function" ):
                return visitor.visitMain_function(self)
            else:
                return visitor.visitChildren(self)




    def main_function(self):

        localctx = C_grammarParser.Main_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_main_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.type_specifier()
            self.state = 60
            self.match(C_grammarParser.T__3)
            self.state = 61
            self.match(C_grammarParser.T__1)
            self.state = 62
            self.params()
            self.state = 63
            self.match(C_grammarParser.T__2)
            self.state = 64
            self.compound_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specifier(self):
            return self.getTypedRuleContext(C_grammarParser.Type_specifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(C_grammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return C_grammarParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = C_grammarParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.type_specifier()
            self.state = 67
            self.match(C_grammarParser.IDENTIFIER)
            self.state = 68
            self.match(C_grammarParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.Type_specifierContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.Type_specifierContext,i)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(C_grammarParser.IDENTIFIER)
            else:
                return self.getToken(C_grammarParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return C_grammarParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = C_grammarParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 532676608) != 0):
                self.state = 70
                self.type_specifier()
                self.state = 71
                self.match(C_grammarParser.IDENTIFIER)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 72
                    self.match(C_grammarParser.T__5)
                    self.state = 73
                    self.type_specifier()
                    self.state = 74
                    self.match(C_grammarParser.IDENTIFIER)
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(C_grammarParser.StatementContext,0)


        def getRuleIndex(self):
            return C_grammarParser.RULE_compound_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_statement" ):
                listener.enterCompound_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_statement" ):
                listener.exitCompound_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_statement" ):
                return visitor.visitCompound_statement(self)
            else:
                return visitor.visitChildren(self)




    def compound_statement(self):

        localctx = C_grammarParser.Compound_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_compound_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(C_grammarParser.T__6)
            self.state = 84
            self.statement()
            self.state = 85
            self.match(C_grammarParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.DeclarationContext,i)


        def initializing(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.InitializingContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.InitializingContext,i)


        def function_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.Function_callContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.Function_callContext,i)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.AssignmentContext,i)


        def if_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.If_statementContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.If_statementContext,i)


        def while_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.While_statementContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.While_statementContext,i)


        def return_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.Return_statementContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.Return_statementContext,i)


        def getRuleIndex(self):
            return C_grammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = C_grammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2680185856) != 0):
                self.state = 94
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 87
                    self.declaration()
                    pass

                elif la_ == 2:
                    self.state = 88
                    self.initializing()
                    pass

                elif la_ == 3:
                    self.state = 89
                    self.function_call()
                    pass

                elif la_ == 4:
                    self.state = 90
                    self.assignment()
                    pass

                elif la_ == 5:
                    self.state = 91
                    self.if_statement()
                    pass

                elif la_ == 6:
                    self.state = 92
                    self.while_statement()
                    pass

                elif la_ == 7:
                    self.state = 93
                    self.return_statement()
                    pass


                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(C_grammarParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(C_grammarParser.ExpressionContext,0)


        def function_call(self):
            return self.getTypedRuleContext(C_grammarParser.Function_callContext,0)


        def getRuleIndex(self):
            return C_grammarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = C_grammarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.match(C_grammarParser.IDENTIFIER)
                self.state = 100
                self.match(C_grammarParser.T__8)
                self.state = 101
                self.expression()
                self.state = 102
                self.match(C_grammarParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(C_grammarParser.IDENTIFIER)
                self.state = 105
                self.match(C_grammarParser.T__8)
                self.state = 106
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(C_grammarParser.IDENTIFIER, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return C_grammarParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = C_grammarParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(C_grammarParser.IDENTIFIER)
            self.state = 110
            self.match(C_grammarParser.T__1)
            self.state = 111
            self.expression()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 112
                self.match(C_grammarParser.T__5)
                self.state = 113
                self.expression()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self.match(C_grammarParser.T__2)
            self.state = 120
            self.match(C_grammarParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specifier(self):
            return self.getTypedRuleContext(C_grammarParser.Type_specifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(C_grammarParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(C_grammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return C_grammarParser.RULE_initializing

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializing" ):
                listener.enterInitializing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializing" ):
                listener.exitInitializing(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializing" ):
                return visitor.visitInitializing(self)
            else:
                return visitor.visitChildren(self)




    def initializing(self):

        localctx = C_grammarParser.InitializingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_initializing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.type_specifier()
            self.state = 123
            self.match(C_grammarParser.IDENTIFIER)
            self.state = 124
            self.match(C_grammarParser.T__8)
            self.state = 125
            self.expression()
            self.state = 126
            self.match(C_grammarParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition_statement_RFC(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.Condition_statement_RFCContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.Condition_statement_RFCContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.StatementContext,i)


        def getRuleIndex(self):
            return C_grammarParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = C_grammarParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(C_grammarParser.T__9)
            self.state = 129
            self.match(C_grammarParser.T__1)
            self.state = 130
            self.condition_statement_RFC()
            self.state = 131
            self.match(C_grammarParser.T__2)
            self.state = 132
            self.match(C_grammarParser.T__6)
            self.state = 133
            self.statement()
            self.state = 134
            self.match(C_grammarParser.T__7)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 135
                self.match(C_grammarParser.T__10)
                self.state = 136
                self.match(C_grammarParser.T__1)
                self.state = 137
                self.condition_statement_RFC()
                self.state = 138
                self.match(C_grammarParser.T__2)
                self.state = 139
                self.match(C_grammarParser.T__6)
                self.state = 140
                self.statement()
                self.state = 141
                self.match(C_grammarParser.T__7)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 148
                self.match(C_grammarParser.T__11)
                self.state = 149
                self.match(C_grammarParser.T__6)
                self.state = 150
                self.statement()
                self.state = 151
                self.match(C_grammarParser.T__7)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition_statement_RFC(self):
            return self.getTypedRuleContext(C_grammarParser.Condition_statement_RFCContext,0)


        def statement(self):
            return self.getTypedRuleContext(C_grammarParser.StatementContext,0)


        def getRuleIndex(self):
            return C_grammarParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = C_grammarParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(C_grammarParser.T__12)
            self.state = 156
            self.match(C_grammarParser.T__1)
            self.state = 157
            self.condition_statement_RFC()
            self.state = 158
            self.match(C_grammarParser.T__2)
            self.state = 159
            self.match(C_grammarParser.T__6)
            self.state = 160
            self.statement()
            self.state = 161
            self.match(C_grammarParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_statement_RFCContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.ExpressionContext,i)


        def CONDITIONAL_OPERATOR(self):
            return self.getToken(C_grammarParser.CONDITIONAL_OPERATOR, 0)

        def IDENTIFIER(self):
            return self.getToken(C_grammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return C_grammarParser.RULE_condition_statement_RFC

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_statement_RFC" ):
                listener.enterCondition_statement_RFC(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_statement_RFC" ):
                listener.exitCondition_statement_RFC(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_statement_RFC" ):
                return visitor.visitCondition_statement_RFC(self)
            else:
                return visitor.visitChildren(self)




    def condition_statement_RFC(self):

        localctx = C_grammarParser.Condition_statement_RFCContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_condition_statement_RFC)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.expression()
                self.state = 164
                self.match(C_grammarParser.CONDITIONAL_OPERATOR)
                self.state = 165
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(C_grammarParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(C_grammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return C_grammarParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = C_grammarParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(C_grammarParser.T__13)
            self.state = 171
            self.expression()
            self.state = 172
            self.match(C_grammarParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.TermContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.TermContext,i)


        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(C_grammarParser.OperatorContext)
            else:
                return self.getTypedRuleContext(C_grammarParser.OperatorContext,i)


        def CHAR_LITERAL(self):
            return self.getToken(C_grammarParser.CHAR_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(C_grammarParser.STRING_LITERAL, 0)

        def BOOLEAN(self):
            return self.getToken(C_grammarParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return C_grammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = C_grammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.term()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4161536) != 0):
                    self.state = 175
                    self.operator()
                    self.state = 176
                    self.term()
                    self.state = 182
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.match(C_grammarParser.CHAR_LITERAL)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.match(C_grammarParser.STRING_LITERAL)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 185
                self.match(C_grammarParser.BOOLEAN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(C_grammarParser.IDENTIFIER, 0)

        def INTEGER(self):
            return self.getToken(C_grammarParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(C_grammarParser.FLOAT, 0)

        def getRuleIndex(self):
            return C_grammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = C_grammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385536) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return C_grammarParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = C_grammarParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4161536) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_specifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return C_grammarParser.RULE_type_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_specifier" ):
                listener.enterType_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_specifier" ):
                listener.exitType_specifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_specifier" ):
                return visitor.visitType_specifier(self)
            else:
                return visitor.visitChildren(self)




    def type_specifier(self):

        localctx = C_grammarParser.Type_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_type_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 532676608) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





