import time

class Program:

    def __init__(self):
        self.registers = {}
        self.last_played_sound_frequency = None
        self.counter = 0
        self.should_terminate = False

    def run(self, instructions):
        self.registers = {}
        self.last_played_sound_frequency = None
        self.counter = 0

        while (0 <= self.counter < len(instructions)) and not self.should_terminate:
            self.execute(instructions[self.counter])
    
    def execute(self, instruction):
        params = instruction.split(' ')

        ins = params[0]

        if ins == 'snd':
            self.snd(params[1])
        elif ins == 'set':
            self.set(params[1], params[2])
        elif ins == 'add':
            self.add(params[1], params[2])
        elif ins == 'mul':
            self.mul(params[1], params[2])
        elif ins == 'mod':
            self.mod(params[1], params[2])
        elif ins == 'rcv':
            self.rcv(params[1])
        elif ins == 'jgz':
            self.jgz(params[1], params[2])
        else:
            raise Exception("Unknown instruction: " + ins)

    def snd(self, arg):
        self.last_played_sound_frequency = self.value(arg)
        self.increment_counter()
            
    def set(self, register, arg):
        self.registers[register] = self.value(arg)
        self.increment_counter()

    def add(self, register, arg):
        self.arithemtic_operation(register, arg, lambda a, b: a + b)
    
    def mul(self, register, arg):
        self.arithemtic_operation(register, arg, lambda a, b: a * b)

    def mod(self, register, arg):
        self.arithemtic_operation(register, arg, lambda a, b: a % b)

    def rcv(self, arg):
        if self.value(arg) != 0:
            print(self.last_played_sound_frequency, flush=True)
            self.should_terminate = True
        self.increment_counter()
    
    def jgz(self, register, arg):
        if self.register_value(register) > 0:
            self.counter += self.value(arg)
        else:
            self.increment_counter()

    def arithemtic_operation(self, register, arg, operation):
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