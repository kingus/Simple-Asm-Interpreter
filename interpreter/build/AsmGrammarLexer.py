# Generated from /home/kingus/PycharmProjects/JFK_ASM_INTERPRETER/interpreter/grammar/AsmGrammar.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("U\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\6\4%\n\4\r\4\16\4")
        buf.write("&\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\16\3\16\3\17\3\17\3\17\3\17\2\2\20\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\3\2\6\3\2\62;\3\2cf\3\2\f\f\4\2\13\13\"\"\2U\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\3\37\3\2\2\2\5!\3\2\2\2\7$\3\2\2\2\t(\3\2\2\2")
        buf.write("\13.\3\2\2\2\r\60\3\2\2\2\17\62\3\2\2\2\21\64\3\2\2\2")
        buf.write("\23=\3\2\2\2\25B\3\2\2\2\27G\3\2\2\2\31M\3\2\2\2\33O\3")
        buf.write("\2\2\2\35Q\3\2\2\2\37 \7*\2\2 \4\3\2\2\2!\"\7+\2\2\"\6")
        buf.write("\3\2\2\2#%\t\2\2\2$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3")
        buf.write("\2\2\2\'\b\3\2\2\2()\7\'\2\2)*\7g\2\2*+\3\2\2\2+,\t\3")
        buf.write("\2\2,-\7z\2\2-\n\3\2\2\2./\7-\2\2/\f\3\2\2\2\60\61\7/")
        buf.write("\2\2\61\16\3\2\2\2\62\63\7,\2\2\63\20\3\2\2\2\64\65\7")
        buf.write("k\2\2\65\66\7p\2\2\66\67\7v\2\2\678\7\"\2\289\7\62\2\2")
        buf.write("9:\7z\2\2:;\7:\2\2;<\7\62\2\2<\22\3\2\2\2=>\7o\2\2>?\7")
        buf.write("q\2\2?@\7x\2\2@A\7\"\2\2A\24\3\2\2\2BC\7z\2\2CD\7q\2\2")
        buf.write("DE\7t\2\2EF\7\"\2\2F\26\3\2\2\2GH\7r\2\2HI\7w\2\2IJ\7")
        buf.write("u\2\2JK\7j\2\2KL\7\"\2\2L\30\3\2\2\2MN\7.\2\2N\32\3\2")
        buf.write("\2\2OP\t\4\2\2P\34\3\2\2\2QR\t\5\2\2RS\3\2\2\2ST\b\17")
        buf.write("\2\2T\36\3\2\2\2\4\2&\3\b\2\2")
        return buf.getvalue()


class AsmGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LPAREN = 1
    RPAREN = 2
    INTEGER = 3
    REGISTER = 4
    PLUS = 5
    MINUS = 6
    MUL = 7
    INTERRUPT = 8
    MOV = 9
    XOR = 10
    PUSH = 11
    SEPARATOR = 12
    END = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'+'", "'-'", "'*'", "'int 0x80'", "'mov '", "'xor '", 
            "'push '", "','" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "INTEGER", "REGISTER", "PLUS", "MINUS", 
            "MUL", "INTERRUPT", "MOV", "XOR", "PUSH", "SEPARATOR", "END", 
            "WS" ]

    ruleNames = [ "LPAREN", "RPAREN", "INTEGER", "REGISTER", "PLUS", "MINUS", 
                  "MUL", "INTERRUPT", "MOV", "XOR", "PUSH", "SEPARATOR", 
                  "END", "WS" ]

    grammarFileName = "AsmGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


