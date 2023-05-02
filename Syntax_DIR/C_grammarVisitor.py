# Generated from C_grammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .C_grammarParser import C_grammarParser
else:
    from C_grammarParser import C_grammarParser

# This class defines a complete generic visitor for a parse tree produced by C_grammarParser.

class C_grammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by C_grammarParser#program.
    def visitProgram(self, ctx:C_grammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#include_list.
    def visitInclude_list(self, ctx:C_grammarParser.Include_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#function.
    def visitFunction(self, ctx:C_grammarParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#main_function.
    def visitMain_function(self, ctx:C_grammarParser.Main_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#declaration.
    def visitDeclaration(self, ctx:C_grammarParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#params.
    def visitParams(self, ctx:C_grammarParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#compound_statement.
    def visitCompound_statement(self, ctx:C_grammarParser.Compound_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#statement.
    def visitStatement(self, ctx:C_grammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#assignment.
    def visitAssignment(self, ctx:C_grammarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#function_call.
    def visitFunction_call(self, ctx:C_grammarParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#initializing.
    def visitInitializing(self, ctx:C_grammarParser.InitializingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#if_statement.
    def visitIf_statement(self, ctx:C_grammarParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#while_statement.
    def visitWhile_statement(self, ctx:C_grammarParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#condition_statement_RFC.
    def visitCondition_statement_RFC(self, ctx:C_grammarParser.Condition_statement_RFCContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#return_statement.
    def visitReturn_statement(self, ctx:C_grammarParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#expression.
    def visitExpression(self, ctx:C_grammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#term.
    def visitTerm(self, ctx:C_grammarParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#operator.
    def visitOperator(self, ctx:C_grammarParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#type_specifier.
    def visitType_specifier(self, ctx:C_grammarParser.Type_specifierContext):
        return self.visitChildren(ctx)



del C_grammarParser