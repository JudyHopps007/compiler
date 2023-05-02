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


    # Visit a parse tree produced by C_grammarParser#statement.
    def visitStatement(self, ctx:C_grammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#assignment.
    def visitAssignment(self, ctx:C_grammarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#conditional.
    def visitConditional(self, ctx:C_grammarParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#loop.
    def visitLoop(self, ctx:C_grammarParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#print_statement.
    def visitPrint_statement(self, ctx:C_grammarParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#function_definition.
    def visitFunction_definition(self, ctx:C_grammarParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#procedure_definition.
    def visitProcedure_definition(self, ctx:C_grammarParser.Procedure_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#parameter_list.
    def visitParameter_list(self, ctx:C_grammarParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#parameter.
    def visitParameter(self, ctx:C_grammarParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#function_call.
    def visitFunction_call(self, ctx:C_grammarParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#procedure_call.
    def visitProcedure_call(self, ctx:C_grammarParser.Procedure_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#argument_list.
    def visitArgument_list(self, ctx:C_grammarParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#return_statement.
    def visitReturn_statement(self, ctx:C_grammarParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#array_declaration.
    def visitArray_declaration(self, ctx:C_grammarParser.Array_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#list_declaration.
    def visitList_declaration(self, ctx:C_grammarParser.List_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#expression_list.
    def visitExpression_list(self, ctx:C_grammarParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#array_access.
    def visitArray_access(self, ctx:C_grammarParser.Array_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#list_access.
    def visitList_access(self, ctx:C_grammarParser.List_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#class_declaration.
    def visitClass_declaration(self, ctx:C_grammarParser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#class_body.
    def visitClass_body(self, ctx:C_grammarParser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#member.
    def visitMember(self, ctx:C_grammarParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#attribute_declaration.
    def visitAttribute_declaration(self, ctx:C_grammarParser.Attribute_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#method_declaration.
    def visitMethod_declaration(self, ctx:C_grammarParser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#expression.
    def visitExpression(self, ctx:C_grammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#log_expr.
    def visitLog_expr(self, ctx:C_grammarParser.Log_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#relation.
    def visitRelation(self, ctx:C_grammarParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#arith_expr.
    def visitArith_expr(self, ctx:C_grammarParser.Arith_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#term.
    def visitTerm(self, ctx:C_grammarParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#factor.
    def visitFactor(self, ctx:C_grammarParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#identifier.
    def visitIdentifier(self, ctx:C_grammarParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#number.
    def visitNumber(self, ctx:C_grammarParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#datatype.
    def visitDatatype(self, ctx:C_grammarParser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#add_op.
    def visitAdd_op(self, ctx:C_grammarParser.Add_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#mul_op.
    def visitMul_op(self, ctx:C_grammarParser.Mul_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#rel_op.
    def visitRel_op(self, ctx:C_grammarParser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by C_grammarParser#log_op.
    def visitLog_op(self, ctx:C_grammarParser.Log_opContext):
        return self.visitChildren(ctx)



del C_grammarParser