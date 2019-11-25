from interpreter.build.AsmGrammarParser import AsmGrammarParser
from interpreter.build.AsmGrammarLexer import AsmGrammarLexer
from interpreter.MyVisitor import MyVisitor
from antlr4 import *
from interpreter.MyErrorListener import MyErrorListener, SyntaxException


def main():

    while True:
        try:
            inp = input('')
            inp = inp + "\n"
            if inp is "\n":
                continue
        except EOFError:
            break
        try:
            text = InputStream(inp)
            lexer = AsmGrammarLexer(text)
            lexer.removeErrorListeners()
            stream = CommonTokenStream(lexer)
            parser = AsmGrammarParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(MyErrorListener())
            tree = parser.commands()
            visitor = MyVisitor()
            visitor.visit(tree)
        except SyntaxException as e:
            print(e)