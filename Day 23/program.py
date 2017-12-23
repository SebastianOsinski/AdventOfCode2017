class Program:

    def __init__(self, instructions):
        self.instructions = instructions
        self.registers = {}
        self.counter = 0
        self.mul_counter = 0

    def run(self):
        while self.can_run():
            self.execute(self.instructions[self.counter])
            
    def can_run(self):
        return (0 <= self.counter < len(self.instructions))
    
    def execute(self, instruction):
        params = instruction.split(' ')

        ins = params[0]

        if ins == 'set':
            self.set(params[1], params[2])
        elif ins == 'sub':
            self.sub(params[1], params[2])
        elif ins == 'mul':
            self.mul(params[1], params[2])
        elif ins == 'jnz':
            self.jnz(params[1], params[2])
        else:
            raise Exception("Unknown instruction: " + ins)
            
    def set(self, register, arg):
        self.registers[register] = self.value(arg)
        self.increment_counter()

    def sub(self, register, arg):
        self.arithmetic_operation(register, arg, lambda a, b: a - b)
    
    def mul(self, register, arg):
        self.arithmetic_operation(register, arg, lambda a, b: a * b)
        self.mul_counter += 1
    
    def jnz(self, arg0, arg1):
        if self.value(arg0) != 0:
            self.counter += self.value(arg1)
        else:
            self.increment_counter()

    def arithmetic_operation(self, register, arg, operation):
        self.registers[register] = operation(self.register_value(register), self.value(arg))
        self.increment_counter()

    def value(self, register_or_number):
        try:
            return int(register_or_number)
        except ValueError:
            return self.register_value(register_or_number)

    def register_value(self, register):
        return self.registers.get(register, 0)

    def increment_counter(self):
        self.counter += 1