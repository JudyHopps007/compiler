# Generated from C_grammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .C_grammarParser import C_grammarParser
else:
    from C_grammarParser import C_grammarParser

# This class defines a complete listener for a parse tree produced by C_grammarParser.
class C_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by C_grammarParser#program.
    def enterProgram(self, ctx:C_grammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by C_grammarParser#program.
    def exitProgram(self, ctx:C_grammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by C_grammarParser#include_list.
    def enterInclude_list(self, ctx:C_grammarParser.Include_listContext):
        pass

    # Exit a parse tree produced by C_grammarParser#include_list.
    def exitInclude_list(self, ctx:C_grammarParser.Include_listContext):
        pass


    # Enter a parse tree produced by C_grammarParser#function.
    def enterFunction(self, ctx:C_grammarParser.FunctionContext):
        pass

    # Exit a parse tree produced by C_grammarParser#function.
    def exitFunction(self, ctx:C_grammarParser.FunctionContext):
        pass


    # Enter a parse tree produced by C_grammarParser#main_function.
    def enterMain_function(self, ctx:C_grammarParser.Main_functionContext):
        pass

    # Exit a parse tree produced by C_grammarParser#main_function.
    def exitMain_function(self, ctx:C_grammarParser.Main_functionContext):
        pass


    # Enter a parse tree produced by C_grammarParser#declaration.
    def enterDeclaration(self, ctx:C_grammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by C_grammarParser#declaration.
    def exitDeclaration(self, ctx:C_grammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by C_grammarParser#params.
    def enterParams(self, ctx:C_grammarParser.ParamsContext):
        pass

    # Exit a parse tree produced by C_grammarParser#params.
    def exitParams(self, ctx:C_grammarParser.ParamsContext):
        pass


    # Enter a parse tree produced by C_grammarParser#compound_statement.
    def enterCompound_statement(self, ctx:C_grammarParser.Compound_statementContext):
        pass

    # Exit a parse tree produced by C_grammarParser#compound_statement.
    def exitCompound_statement(self, ctx:C_grammarParser.Compound_statementContext):
        pass


    # Enter a parse tree produced by C_grammarParser#statement.
    def enterStatement(self, ctx:C_grammarParser.StatementContext):
        pass

    # Exit a parse tree produced by C_grammarParser#statement.
    def exitStatement(self, ctx:C_grammarParser.StatementContext):
        pass


    # Enter a parse tree produced by C_grammarParser#assignment.
    def enterAssignment(self, ctx:C_grammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by C_grammarParser#assignment.
    def exitAssignment(self, ctx:C_grammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by C_grammarParser#function_call.
    def enterFunction_call(self, ctx:C_grammarParser.Function_callContext):
        pass

    # Exit a parse tree produced by C_grammarParser#function_call.
    def exitFunction_call(self, ctx:C_grammarParser.Function_callContext):
        pass


    # Enter a parse tree produced by C_grammarParser#initializing.
    def enterInitializing(self, ctx:C_grammarParser.InitializingContext):
        pass

    # Exit a parse tree produced by C_grammarParser#initializing.
    def exitInitializing(self, ctx:C_grammarParser.InitializingContext):
        pass


    # Enter a parse tree produced by C_grammarParser#if_statement.
    def enterIf_statement(self, ctx:C_grammarParser.If_statementContext):
        pass

    # Exit a parse tree produced by C_grammarParser#if_statement.
    def exitIf_statement(self, ctx:C_grammarParser.If_statementContext):
        pass


    # Enter a parse tree produced by C_grammarParser#while_statement.
    def enterWhile_statement(self, ctx:C_grammarParser.While_statementContext):
        pass

    # Exit a parse tree produced by C_grammarParser#while_statement.
    def exitWhile_statement(self, ctx:C_grammarParser.While_statementContext):
        pass


    # Enter a parse tree produced by C_grammarParser#condition.
    def enterCondition(self, ctx:C_grammarParser.ConditionContext):
        pass

    # Exit a parse tree produced by C_grammarParser#condition.
    def exitCondition(self, ctx:C_grammarParser.ConditionContext):
        pass


    # Enter a parse tree produced by C_grammarParser#return_statement.
    def enterReturn_statement(self, ctx:C_grammarParser.Return_statementContext):
        pass

    # Exit a parse tree produced by C_grammarParser#return_statement.
    def exitReturn_statement(self, ctx:C_grammarParser.Return_statementContext):
        pass


    # Enter a parse tree produced by C_grammarParser#expression.
    def enterExpression(self, ctx:C_grammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by C_grammarParser#expression.
    def exitExpression(self, ctx:C_grammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by C_grammarParser#term.
    def enterTerm(self, ctx:C_grammarParser.TermContext):
        pass

    # Exit a parse tree produced by C_grammarParser#term.
    def exitTerm(self, ctx:C_grammarParser.TermContext):
        pass


    # Enter a parse tree produced by C_grammarParser#operator.
    def enterOperator(self, ctx:C_grammarParser.OperatorContext):
        pass

    # Exit a parse tree produced by C_grammarParser#operator.
    def exitOperator(self, ctx:C_grammarParser.OperatorContext):
        pass


    # Enter a parse tree produced by C_grammarParser#type_specifier.
    def enterType_specifier(self, ctx:C_grammarParser.Type_specifierContext):
        pass

    # Exit a parse tree produced by C_grammarParser#type_specifier.
    def exitType_specifier(self, ctx:C_grammarParser.Type_specifierContext):
        pass



del C_grammarParser