# Generated from /home/kingus/PycharmProjects/JFK_ASM_INTERPRETER/interpreter/grammar/AsmGrammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AsmGrammarParser import AsmGrammarParser
else:
    from AsmGrammarParser import AsmGrammarParser

# This class defines a complete generic visitor for a parse tree produced by AsmGrammarParser.

class AsmGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AsmGrammarParser#factor.
    def visitFactor(self, ctx:AsmGrammarParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmGrammarParser#term.
    def visitTerm(self, ctx:AsmGrammarParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmGrammarParser#expr.
    def visitExpr(self, ctx:AsmGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmGrammarParser#push_cmd.
    def visitPush_cmd(self, ctx:AsmGrammarParser.Push_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmGrammarParser#int_cmd.
    def visitInt_cmd(self, ctx:AsmGrammarParser.Int_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmGrammarParser#mov_cmd.
    def visitMov_cmd(self, ctx:AsmGrammarParser.Mov_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmGrammarParser#xor_cmd.
    def visitXor_cmd(self, ctx:AsmGrammarParser.Xor_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsmGrammarParser#commands.
    def visitCommands(self, ctx:AsmGrammarParser.CommandsContext):
        return self.visitChildren(ctx)



del AsmGrammarParser