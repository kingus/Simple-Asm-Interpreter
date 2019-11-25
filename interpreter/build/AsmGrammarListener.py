# Generated from /home/kingus/PycharmProjects/JFK_ASM_INTERPRETER/interpreter/grammar/AsmGrammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AsmGrammarParser import AsmGrammarParser
else:
    from AsmGrammarParser import AsmGrammarParser

# This class defines a complete listener for a parse tree produced by AsmGrammarParser.
class AsmGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by AsmGrammarParser#factor.
    def enterFactor(self, ctx:AsmGrammarParser.FactorContext):
        pass

    # Exit a parse tree produced by AsmGrammarParser#factor.
    def exitFactor(self, ctx:AsmGrammarParser.FactorContext):
        pass


    # Enter a parse tree produced by AsmGrammarParser#term.
    def enterTerm(self, ctx:AsmGrammarParser.TermContext):
        pass

    # Exit a parse tree produced by AsmGrammarParser#term.
    def exitTerm(self, ctx:AsmGrammarParser.TermContext):
        pass


    # Enter a parse tree produced by AsmGrammarParser#expr.
    def enterExpr(self, ctx:AsmGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by AsmGrammarParser#expr.
    def exitExpr(self, ctx:AsmGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by AsmGrammarParser#push_cmd.
    def enterPush_cmd(self, ctx:AsmGrammarParser.Push_cmdContext):
        pass

    # Exit a parse tree produced by AsmGrammarParser#push_cmd.
    def exitPush_cmd(self, ctx:AsmGrammarParser.Push_cmdContext):
        pass


    # Enter a parse tree produced by AsmGrammarParser#int_cmd.
    def enterInt_cmd(self, ctx:AsmGrammarParser.Int_cmdContext):
        pass

    # Exit a parse tree produced by AsmGrammarParser#int_cmd.
    def exitInt_cmd(self, ctx:AsmGrammarParser.Int_cmdContext):
        pass


    # Enter a parse tree produced by AsmGrammarParser#mov_cmd.
    def enterMov_cmd(self, ctx:AsmGrammarParser.Mov_cmdContext):
        pass

    # Exit a parse tree produced by AsmGrammarParser#mov_cmd.
    def exitMov_cmd(self, ctx:AsmGrammarParser.Mov_cmdContext):
        pass


    # Enter a parse tree produced by AsmGrammarParser#xor_cmd.
    def enterXor_cmd(self, ctx:AsmGrammarParser.Xor_cmdContext):
        pass

    # Exit a parse tree produced by AsmGrammarParser#xor_cmd.
    def exitXor_cmd(self, ctx:AsmGrammarParser.Xor_cmdContext):
        pass


    # Enter a parse tree produced by AsmGrammarParser#commands.
    def enterCommands(self, ctx:AsmGrammarParser.CommandsContext):
        pass

    # Exit a parse tree produced by AsmGrammarParser#commands.
    def exitCommands(self, ctx:AsmGrammarParser.CommandsContext):
        pass


