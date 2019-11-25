class Memory:

    def __init__(self):
        self.registers_memory = Registers()
        self.stack_memory = Stack()


class Registers:
    registers = {"%eax": "???", "%ebx": "???", "%ecx": "???", "%edx": "???"}

    def mov_instruction(self, register, value):
        result = {register : value}
        self.registers.update(result)

    def print_registers(self):
        for reg, val in self.registers.items():
            print(reg, ":", val)

    def get_register_value(self, register):
        result = self.registers.get(register)
        return result

    def xor_instruction(self, expr, register):
        register_value = self.get_register_value(register)
        expr_value = self.get_register_value(expr)
        if expr == register:
            result = {register: 0}
        elif register_value == "???" or expr_value == "???":
            result = {register: "???"}
        else:
            xor_result = (expr_value ^ register_value)
            result = {register: xor_result}
        self.registers.update(result)


class Stack:
    stack = []

    def push_instruction(self, value):
        self.stack.append(value)

    def int_instruction(self):
        result = "???"
        if len(self.stack) is not 0:
            result = self.stack.pop()
        print(result)
