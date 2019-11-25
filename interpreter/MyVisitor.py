from interpreter.build.AsmGrammarParser import AsmGrammarParser
from interpreter.build.AsmGrammarVisitor import AsmGrammarVisitor
from interpreter.Memory import Memory


class MyVisitor(AsmGrammarVisitor):

    def __init__(self):
        self.memory = Memory()

    def visitFactor(self, ctx: AsmGrammarParser.FactorContext):
        if ctx.INTEGER():
            return int(ctx.INTEGER().getText())
        elif ctx.REGISTER():
            register = str(ctx.REGISTER().getText())
            register_value = self.memory.registers_memory.get_register_value(register)
            return register_value
        elif ctx.LPAREN():
            return self.visitExpr(ctx.expr())

    def visitTerm(self, ctx: AsmGrammarParser.TermContext):
        result = None
        if ctx.MUL():
            factor = self.visitFactor(ctx.factor())
            term = self.visitTerm(ctx.term())
            result = factor * term
        elif ctx.factor():
            factor = self.visitFactor(ctx.factor())
            result = factor
        return result

    def visitExpr(self, ctx: AsmGrammarParser.ExprContext):

        if ctx.term():
            term = self.visitTerm(ctx.term())
            result = term
        if ctx.PLUS():
            term = self.visitTerm(ctx.term())
            expr = self.visitExpr(ctx.expr())
            result = term + expr
        if ctx.MINUS():
            expr = self.visitExpr(ctx.expr())
            term = self.visitTerm(ctx.term())
            result = expr - term
        return result

    def visitPush_cmd(self, ctx: AsmGrammarParser.Push_cmdContext):
        if ctx.PUSH() is not None:
            expr = self.visitExpr(ctx.expr())
            if expr is not None:
                self.memory.stack_memory.push_instruction(expr)
        else:
            return None

    def visitInt_cmd(self, ctx: AsmGrammarParser.Int_cmdContext):
        if ctx.INTERRUPT():
            self.memory.stack_memory.int_instruction()

    def visitMov_cmd(self, ctx: AsmGrammarParser.Mov_cmdContext):
        if ctx.MOV():
            expr = self.visitExpr(ctx.expr())
            register = ctx.REGISTER().getText()
            self.memory.registers_memory.mov_instruction(register, expr)

    def visitXor_cmd(self, ctx: AsmGrammarParser.Xor_cmdContext):
        if ctx.XOR():
            expr = ctx.expr().getText()
            register = ctx.REGISTER().getText()
            self.memory.registers_memory.xor_instruction(expr, register)

    def visitCommands(self, ctx: AsmGrammarParser.CommandsContext):
        if ctx.int_cmd():
            return self.visitInt_cmd(ctx.int_cmd())

        if ctx.push_cmd():
            return self.visitPush_cmd(ctx.push_cmd())

        if ctx.mov_cmd():
            return self.visitMov_cmd(ctx.mov_cmd())

        if ctx.xor_cmd():
            return self.visitXor_cmd(ctx.xor_cmd())