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


    # Enter a parse tree produced by C_grammarParser#conditional.
    def enterConditional(self, ctx:C_grammarParser.ConditionalContext):
        pass

    # Exit a parse tree produced by C_grammarParser#conditional.
    def exitConditional(self, ctx:C_grammarParser.ConditionalContext):
        pass


    # Enter a parse tree produced by C_grammarParser#loop.
    def enterLoop(self, ctx:C_grammarParser.LoopContext):
        pass

    # Exit a parse tree produced by C_grammarParser#loop.
    def exitLoop(self, ctx:C_grammarParser.LoopContext):
        pass


    # Enter a parse tree produced by C_grammarParser#print_statement.
    def enterPrint_statement(self, ctx:C_grammarParser.Print_statementContext):
        pass

    # Exit a parse tree produced by C_grammarParser#print_statement.
    def exitPrint_statement(self, ctx:C_grammarParser.Print_statementContext):
        pass


    # Enter a parse tree produced by C_grammarParser#function_definition.
    def enterFunction_definition(self, ctx:C_grammarParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by C_grammarParser#function_definition.
    def exitFunction_definition(self, ctx:C_grammarParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by C_grammarParser#procedure_definition.
    def enterProcedure_definition(self, ctx:C_grammarParser.Procedure_definitionContext):
        pass

    # Exit a parse tree produced by C_grammarParser#procedure_definition.
    def exitProcedure_definition(self, ctx:C_grammarParser.Procedure_definitionContext):
        pass


    # Enter a parse tree produced by C_grammarParser#parameter_list.
    def enterParameter_list(self, ctx:C_grammarParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by C_grammarParser#parameter_list.
    def exitParameter_list(self, ctx:C_grammarParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by C_grammarParser#parameter.
    def enterParameter(self, ctx:C_grammarParser.ParameterContext):
        pass

    # Exit a parse tree produced by C_grammarParser#parameter.
    def exitParameter(self, ctx:C_grammarParser.ParameterContext):
        pass


    # Enter a parse tree produced by C_grammarParser#function_call.
    def enterFunction_call(self, ctx:C_grammarParser.Function_callContext):
        pass

    # Exit a parse tree produced by C_grammarParser#function_call.
    def exitFunction_call(self, ctx:C_grammarParser.Function_callContext):
        pass


    # Enter a parse tree produced by C_grammarParser#procedure_call.
    def enterProcedure_call(self, ctx:C_grammarParser.Procedure_callContext):
        pass

    # Exit a parse tree produced by C_grammarParser#procedure_call.
    def exitProcedure_call(self, ctx:C_grammarParser.Procedure_callContext):
        pass


    # Enter a parse tree produced by C_grammarParser#argument_list.
    def enterArgument_list(self, ctx:C_grammarParser.Argument_listContext):
        pass

    # Exit a parse tree produced by C_grammarParser#argument_list.
    def exitArgument_list(self, ctx:C_grammarParser.Argument_listContext):
        pass


    # Enter a parse tree produced by C_grammarParser#return_statement.
    def enterReturn_statement(self, ctx:C_grammarParser.Return_statementContext):
        pass

    # Exit a parse tree produced by C_grammarParser#return_statement.
    def exitReturn_statement(self, ctx:C_grammarParser.Return_statementContext):
        pass


    # Enter a parse tree produced by C_grammarParser#array_declaration.
    def enterArray_declaration(self, ctx:C_grammarParser.Array_declarationContext):
        pass

    # Exit a parse tree produced by C_grammarParser#array_declaration.
    def exitArray_declaration(self, ctx:C_grammarParser.Array_declarationContext):
        pass


    # Enter a parse tree produced by C_grammarParser#list_declaration.
    def enterList_declaration(self, ctx:C_grammarParser.List_declarationContext):
        pass

    # Exit a parse tree produced by C_grammarParser#list_declaration.
    def exitList_declaration(self, ctx:C_grammarParser.List_declarationContext):
        pass


    # Enter a parse tree produced by C_grammarParser#expression_list.
    def enterExpression_list(self, ctx:C_grammarParser.Expression_listContext):
        pass

    # Exit a parse tree produced by C_grammarParser#expression_list.
    def exitExpression_list(self, ctx:C_grammarParser.Expression_listContext):
        pass


    # Enter a parse tree produced by C_grammarParser#array_access.
    def enterArray_access(self, ctx:C_grammarParser.Array_accessContext):
        pass

    # Exit a parse tree produced by C_grammarParser#array_access.
    def exitArray_access(self, ctx:C_grammarParser.Array_accessContext):
        pass


    # Enter a parse tree produced by C_grammarParser#list_access.
    def enterList_access(self, ctx:C_grammarParser.List_accessContext):
        pass

    # Exit a parse tree produced by C_grammarParser#list_access.
    def exitList_access(self, ctx:C_grammarParser.List_accessContext):
        pass


    # Enter a parse tree produced by C_grammarParser#class_declaration.
    def enterClass_declaration(self, ctx:C_grammarParser.Class_declarationContext):
        pass

    # Exit a parse tree produced by C_grammarParser#class_declaration.
    def exitClass_declaration(self, ctx:C_grammarParser.Class_declarationContext):
        pass


    # Enter a parse tree produced by C_grammarParser#class_body.
    def enterClass_body(self, ctx:C_grammarParser.Class_bodyContext):
        pass

    # Exit a parse tree produced by C_grammarParser#class_body.
    def exitClass_body(self, ctx:C_grammarParser.Class_bodyContext):
        pass


    # Enter a parse tree produced by C_grammarParser#member.
    def enterMember(self, ctx:C_grammarParser.MemberContext):
        pass

    # Exit a parse tree produced by C_grammarParser#member.
    def exitMember(self, ctx:C_grammarParser.MemberContext):
        pass


    # Enter a parse tree produced by C_grammarParser#attribute_declaration.
    def enterAttribute_declaration(self, ctx:C_grammarParser.Attribute_declarationContext):
        pass

    # Exit a parse tree produced by C_grammarParser#attribute_declaration.
    def exitAttribute_declaration(self, ctx:C_grammarParser.Attribute_declarationContext):
        pass


    # Enter a parse tree produced by C_grammarParser#method_declaration.
    def enterMethod_declaration(self, ctx:C_grammarParser.Method_declarationContext):
        pass

    # Exit a parse tree produced by C_grammarParser#method_declaration.
    def exitMethod_declaration(self, ctx:C_grammarParser.Method_declarationContext):
        pass


    # Enter a parse tree produced by C_grammarParser#expression.
    def enterExpression(self, ctx:C_grammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by C_grammarParser#expression.
    def exitExpression(self, ctx:C_grammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by C_grammarParser#log_expr.
    def enterLog_expr(self, ctx:C_grammarParser.Log_exprContext):
        pass

    # Exit a parse tree produced by C_grammarParser#log_expr.
    def exitLog_expr(self, ctx:C_grammarParser.Log_exprContext):
        pass


    # Enter a parse tree produced by C_grammarParser#relation.
    def enterRelation(self, ctx:C_grammarParser.RelationContext):
        pass

    # Exit a parse tree produced by C_grammarParser#relation.
    def exitRelation(self, ctx:C_grammarParser.RelationContext):
        pass


    # Enter a parse tree produced by C_grammarParser#arith_expr.
    def enterArith_expr(self, ctx:C_grammarParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by C_grammarParser#arith_expr.
    def exitArith_expr(self, ctx:C_grammarParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by C_grammarParser#term.
    def enterTerm(self, ctx:C_grammarParser.TermContext):
        pass

    # Exit a parse tree produced by C_grammarParser#term.
    def exitTerm(self, ctx:C_grammarParser.TermContext):
        pass


    # Enter a parse tree produced by C_grammarParser#factor.
    def enterFactor(self, ctx:C_grammarParser.FactorContext):
        pass

    # Exit a parse tree produced by C_grammarParser#factor.
    def exitFactor(self, ctx:C_grammarParser.FactorContext):
        pass


    # Enter a parse tree produced by C_grammarParser#identifier.
    def enterIdentifier(self, ctx:C_grammarParser.IdentifierContext):
        pass

    # Exit a parse tree produced by C_grammarParser#identifier.
    def exitIdentifier(self, ctx:C_grammarParser.IdentifierContext):
        pass


    # Enter a parse tree produced by C_grammarParser#number.
    def enterNumber(self, ctx:C_grammarParser.NumberContext):
        pass

    # Exit a parse tree produced by C_grammarParser#number.
    def exitNumber(self, ctx:C_grammarParser.NumberContext):
        pass


    # Enter a parse tree produced by C_grammarParser#datatype.
    def enterDatatype(self, ctx:C_grammarParser.DatatypeContext):
        pass

    # Exit a parse tree produced by C_grammarParser#datatype.
    def exitDatatype(self, ctx:C_grammarParser.DatatypeContext):
        pass


    # Enter a parse tree produced by C_grammarParser#add_op.
    def enterAdd_op(self, ctx:C_grammarParser.Add_opContext):
        pass

    # Exit a parse tree produced by C_grammarParser#add_op.
    def exitAdd_op(self, ctx:C_grammarParser.Add_opContext):
        pass


    # Enter a parse tree produced by C_grammarParser#mul_op.
    def enterMul_op(self, ctx:C_grammarParser.Mul_opContext):
        pass

    # Exit a parse tree produced by C_grammarParser#mul_op.
    def exitMul_op(self, ctx:C_grammarParser.Mul_opContext):
        pass


    # Enter a parse tree produced by C_grammarParser#rel_op.
    def enterRel_op(self, ctx:C_grammarParser.Rel_opContext):
        pass

    # Exit a parse tree produced by C_grammarParser#rel_op.
    def exitRel_op(self, ctx:C_grammarParser.Rel_opContext):
        pass


    # Enter a parse tree produced by C_grammarParser#log_op.
    def enterLog_op(self, ctx:C_grammarParser.Log_opContext):
        pass

    # Exit a parse tree produced by C_grammarParser#log_op.
    def exitLog_op(self, ctx:C_grammarParser.Log_opContext):
        pass



del C_grammarParser