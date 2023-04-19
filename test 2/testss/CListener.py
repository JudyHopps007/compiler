# Generated from C.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete listener for a parse tree produced by CParser.
class CListener(ParseTreeListener):

    # Enter a parse tree produced by CParser#program.
    def enterProgram(self, ctx:CParser.ProgramContext):
        pass

    # Exit a parse tree produced by CParser#program.
    def exitProgram(self, ctx:CParser.ProgramContext):
        pass


    # Enter a parse tree produced by CParser#function.
    def enterFunction(self, ctx:CParser.FunctionContext):
        pass

    # Exit a parse tree produced by CParser#function.
    def exitFunction(self, ctx:CParser.FunctionContext):
        pass


    # Enter a parse tree produced by CParser#declaration.
    def enterDeclaration(self, ctx:CParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CParser#declaration.
    def exitDeclaration(self, ctx:CParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CParser#params.
    def enterParams(self, ctx:CParser.ParamsContext):
        pass

    # Exit a parse tree produced by CParser#params.
    def exitParams(self, ctx:CParser.ParamsContext):
        pass


    # Enter a parse tree produced by CParser#compound_statement.
    def enterCompound_statement(self, ctx:CParser.Compound_statementContext):
        pass

    # Exit a parse tree produced by CParser#compound_statement.
    def exitCompound_statement(self, ctx:CParser.Compound_statementContext):
        pass


    # Enter a parse tree produced by CParser#statement.
    def enterStatement(self, ctx:CParser.StatementContext):
        pass

    # Exit a parse tree produced by CParser#statement.
    def exitStatement(self, ctx:CParser.StatementContext):
        pass


    # Enter a parse tree produced by CParser#assignment.
    def enterAssignment(self, ctx:CParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CParser#assignment.
    def exitAssignment(self, ctx:CParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CParser#if_statement.
    def enterIf_statement(self, ctx:CParser.If_statementContext):
        pass

    # Exit a parse tree produced by CParser#if_statement.
    def exitIf_statement(self, ctx:CParser.If_statementContext):
        pass


    # Enter a parse tree produced by CParser#while_statement.
    def enterWhile_statement(self, ctx:CParser.While_statementContext):
        pass

    # Exit a parse tree produced by CParser#while_statement.
    def exitWhile_statement(self, ctx:CParser.While_statementContext):
        pass


    # Enter a parse tree produced by CParser#return_statement.
    def enterReturn_statement(self, ctx:CParser.Return_statementContext):
        pass

    # Exit a parse tree produced by CParser#return_statement.
    def exitReturn_statement(self, ctx:CParser.Return_statementContext):
        pass


    # Enter a parse tree produced by CParser#expression_statement.
    def enterExpression_statement(self, ctx:CParser.Expression_statementContext):
        pass

    # Exit a parse tree produced by CParser#expression_statement.
    def exitExpression_statement(self, ctx:CParser.Expression_statementContext):
        pass


    # Enter a parse tree produced by CParser#expression.
    def enterExpression(self, ctx:CParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CParser#expression.
    def exitExpression(self, ctx:CParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CParser#term.
    def enterTerm(self, ctx:CParser.TermContext):
        pass

    # Exit a parse tree produced by CParser#term.
    def exitTerm(self, ctx:CParser.TermContext):
        pass


    # Enter a parse tree produced by CParser#op.
    def enterOp(self, ctx:CParser.OpContext):
        pass

    # Exit a parse tree produced by CParser#op.
    def exitOp(self, ctx:CParser.OpContext):
        pass


    # Enter a parse tree produced by CParser#type.
    def enterType(self, ctx:CParser.TypeContext):
        pass

    # Exit a parse tree produced by CParser#type.
    def exitType(self, ctx:CParser.TypeContext):
        pass



del CParser