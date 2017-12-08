from instruction import Instruction
from sys import maxsize

class CPU:

    def __init__(self):
        self.registers = {}
        self.conditions = {
            "<": lambda x, y: x < y,
            "<=": lambda x, y: x <= y,
            "==": lambda x, y: x == y,
            "!=": lambda x, y: x != y,
            ">=": lambda x, y: x >= y,
            ">": lambda x, y: x > y
        }
        self.lifetime_max = None

    def value_of_register(self, register):
        if register in self.registers:
            return self.registers[register]
        else:
            self.registers[register] = 0
            return 0

    def increment_register(self, register, value):
        new_value = self.value_of_register(register) + value
        self.registers[register] = new_value
        self.change_lifetime_max_if_needed(new_value)

    def decrement_register(self, register, value):
        new_value = self.value_of_register(register) - value
        self.registers[register] = new_value
        self.change_lifetime_max_if_needed(new_value)

    def execute_instruction(self, instruction):
        condition = self.conditions[instruction.condition]
        condition_register_value = self.value_of_register(instruction.condition_register)

        if condition(condition_register_value, instruction.condition_value):
            if instruction.operation == "inc":
                self.increment_register(instruction.register, instruction.value)
            else:
                self.decrement_register(instruction.register, instruction.value)

    def find_largest_register_value(self):
        max = -maxsize - 1
        for register in self.registers:
            value = self.registers[register]
            if value > max:
                max = value

        return max

    def change_lifetime_max_if_needed(self, value):
        if self.lifetime_max is None:
            self.lifetime_max = value
        elif value > self.lifetime_max:
            self.lifetime_max = value
