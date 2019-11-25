# Generated from /home/kingus/PycharmProjects/JFK_ASM_INTERPRETER/interpreter/grammar/AsmGrammar.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("D\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\2\5\2\31\n\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3 \n\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4(\n")
        buf.write("\4\f\4\16\4+\13\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t@\n\t\3\t")
        buf.write("\3\t\3\t\2\3\6\n\2\4\6\b\n\f\16\20\2\3\3\2\7\b\2B\2\30")
        buf.write("\3\2\2\2\4\37\3\2\2\2\6!\3\2\2\2\b,\3\2\2\2\n/\3\2\2\2")
        buf.write("\f\61\3\2\2\2\16\66\3\2\2\2\20?\3\2\2\2\22\31\7\5\2\2")
        buf.write("\23\31\7\6\2\2\24\25\7\3\2\2\25\26\5\6\4\2\26\27\7\4\2")
        buf.write("\2\27\31\3\2\2\2\30\22\3\2\2\2\30\23\3\2\2\2\30\24\3\2")
        buf.write("\2\2\31\3\3\2\2\2\32 \5\2\2\2\33\34\5\2\2\2\34\35\7\t")
        buf.write("\2\2\35\36\5\4\3\2\36 \3\2\2\2\37\32\3\2\2\2\37\33\3\2")
        buf.write("\2\2 \5\3\2\2\2!\"\b\4\1\2\"#\5\4\3\2#)\3\2\2\2$%\f\3")
        buf.write("\2\2%&\t\2\2\2&(\5\4\3\2\'$\3\2\2\2(+\3\2\2\2)\'\3\2\2")
        buf.write("\2)*\3\2\2\2*\7\3\2\2\2+)\3\2\2\2,-\7\r\2\2-.\5\6\4\2")
        buf.write(".\t\3\2\2\2/\60\7\n\2\2\60\13\3\2\2\2\61\62\7\13\2\2\62")
        buf.write("\63\5\6\4\2\63\64\7\16\2\2\64\65\7\6\2\2\65\r\3\2\2\2")
        buf.write("\66\67\7\f\2\2\678\5\6\4\289\7\16\2\29:\7\6\2\2:\17\3")
        buf.write("\2\2\2;@\5\n\6\2<@\5\b\5\2=@\5\f\7\2>@\5\16\b\2?;\3\2")
        buf.write("\2\2?<\3\2\2\2?=\3\2\2\2?>\3\2\2\2@A\3\2\2\2AB\7\17\2")
        buf.write("\2B\21\3\2\2\2\6\30\37)?")
        return buf.getvalue()


class AsmGrammarParser ( Parser ):

    grammarFileName = "AsmGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'int 0x80'", "'mov '", "'xor '", 
                     "'push '", "','" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "INTEGER", "REGISTER", 
                      "PLUS", "MINUS", "MUL", "INTERRUPT", "MOV", "XOR", 
                      "PUSH", "SEPARATOR", "END", "WS" ]

    RULE_factor = 0
    RULE_term = 1
    RULE_expr = 2
    RULE_push_cmd = 3
    RULE_int_cmd = 4
    RULE_mov_cmd = 5
    RULE_xor_cmd = 6
    RULE_commands = 7

    ruleNames =  [ "factor", "term", "expr", "push_cmd", "int_cmd", "mov_cmd", 
                   "xor_cmd", "commands" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    INTEGER=3
    REGISTER=4
    PLUS=5
    MINUS=6
    MUL=7
    INTERRUPT=8
    MOV=9
    XOR=10
    PUSH=11
    SEPARATOR=12
    END=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(AsmGrammarParser.INTEGER, 0)

        def REGISTER(self):
            return self.getToken(AsmGrammarParser.REGISTER, 0)

        def LPAREN(self):
            return self.getToken(AsmGrammarParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(AsmGrammarParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(AsmGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return AsmGrammarParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = AsmGrammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_factor)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AsmGrammarParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(AsmGrammarParser.INTEGER)
                pass
            elif token in [AsmGrammarParser.REGISTER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(AsmGrammarParser.REGISTER)
                pass
            elif token in [AsmGrammarParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 18
                self.match(AsmGrammarParser.LPAREN)
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(AsmGrammarParser.RPAREN)
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(AsmGrammarParser.FactorContext,0)


        def MUL(self):
            return self.getToken(AsmGrammarParser.MUL, 0)

        def term(self):
            return self.getTypedRuleContext(AsmGrammarParser.TermContext,0)


        def getRuleIndex(self):
            return AsmGrammarParser.RULE_term

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

        localctx = AsmGrammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.factor()
                self.state = 26
                self.match(AsmGrammarParser.MUL)
                self.state = 27
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(AsmGrammarParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(AsmGrammarParser.ExprContext,0)


        def PLUS(self):
            return self.getToken(AsmGrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(AsmGrammarParser.MINUS, 0)

        def getRuleIndex(self):
            return AsmGrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AsmGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AsmGrammarParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 34
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 35
                    _la = self._input.LA(1)
                    if not(_la==AsmGrammarParser.PLUS or _la==AsmGrammarParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 36
                    self.term() 
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Push_cmdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUSH(self):
            return self.getToken(AsmGrammarParser.PUSH, 0)

        def expr(self):
            return self.getTypedRuleContext(AsmGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return AsmGrammarParser.RULE_push_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPush_cmd" ):
                listener.enterPush_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPush_cmd" ):
                listener.exitPush_cmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPush_cmd" ):
                return visitor.visitPush_cmd(self)
            else:
                return visitor.visitChildren(self)




    def push_cmd(self):

        localctx = AsmGrammarParser.Push_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_push_cmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(AsmGrammarParser.PUSH)
            self.state = 43
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_cmdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERRUPT(self):
            return self.getToken(AsmGrammarParser.INTERRUPT, 0)

        def getRuleIndex(self):
            return AsmGrammarParser.RULE_int_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_cmd" ):
                listener.enterInt_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_cmd" ):
                listener.exitInt_cmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_cmd" ):
                return visitor.visitInt_cmd(self)
            else:
                return visitor.visitChildren(self)




    def int_cmd(self):

        localctx = AsmGrammarParser.Int_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_int_cmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(AsmGrammarParser.INTERRUPT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mov_cmdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOV(self):
            return self.getToken(AsmGrammarParser.MOV, 0)

        def expr(self):
            return self.getTypedRuleContext(AsmGrammarParser.ExprContext,0)


        def SEPARATOR(self):
            return self.getToken(AsmGrammarParser.SEPARATOR, 0)

        def REGISTER(self):
            return self.getToken(AsmGrammarParser.REGISTER, 0)

        def getRuleIndex(self):
            return AsmGrammarParser.RULE_mov_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMov_cmd" ):
                listener.enterMov_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMov_cmd" ):
                listener.exitMov_cmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMov_cmd" ):
                return visitor.visitMov_cmd(self)
            else:
                return visitor.visitChildren(self)




    def mov_cmd(self):

        localctx = AsmGrammarParser.Mov_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mov_cmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(AsmGrammarParser.MOV)
            self.state = 48
            self.expr(0)
            self.state = 49
            self.match(AsmGrammarParser.SEPARATOR)
            self.state = 50
            self.match(AsmGrammarParser.REGISTER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Xor_cmdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XOR(self):
            return self.getToken(AsmGrammarParser.XOR, 0)

        def expr(self):
            return self.getTypedRuleContext(AsmGrammarParser.ExprContext,0)


        def SEPARATOR(self):
            return self.getToken(AsmGrammarParser.SEPARATOR, 0)

        def REGISTER(self):
            return self.getToken(AsmGrammarParser.REGISTER, 0)

        def getRuleIndex(self):
            return AsmGrammarParser.RULE_xor_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXor_cmd" ):
                listener.enterXor_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXor_cmd" ):
                listener.exitXor_cmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitXor_cmd" ):
                return visitor.visitXor_cmd(self)
            else:
                return visitor.visitChildren(self)




    def xor_cmd(self):

        localctx = AsmGrammarParser.Xor_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_xor_cmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(AsmGrammarParser.XOR)
            self.state = 53
            self.expr(0)
            self.state = 54
            self.match(AsmGrammarParser.SEPARATOR)
            self.state = 55
            self.match(AsmGrammarParser.REGISTER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(AsmGrammarParser.END, 0)

        def int_cmd(self):
            return self.getTypedRuleContext(AsmGrammarParser.Int_cmdContext,0)


        def push_cmd(self):
            return self.getTypedRuleContext(AsmGrammarParser.Push_cmdContext,0)


        def mov_cmd(self):
            return self.getTypedRuleContext(AsmGrammarParser.Mov_cmdContext,0)


        def xor_cmd(self):
            return self.getTypedRuleContext(AsmGrammarParser.Xor_cmdContext,0)


        def getRuleIndex(self):
            return AsmGrammarParser.RULE_commands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommands" ):
                listener.enterCommands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommands" ):
                listener.exitCommands(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommands" ):
                return visitor.visitCommands(self)
            else:
                return visitor.visitChildren(self)




    def commands(self):

        localctx = AsmGrammarParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_commands)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AsmGrammarParser.INTERRUPT]:
                self.state = 57
                self.int_cmd()
                pass
            elif token in [AsmGrammarParser.PUSH]:
                self.state = 58
                self.push_cmd()
                pass
            elif token in [AsmGrammarParser.MOV]:
                self.state = 59
                self.mov_cmd()
                pass
            elif token in [AsmGrammarParser.XOR]:
                self.state = 60
                self.xor_cmd()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 63
            self.match(AsmGrammarParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




