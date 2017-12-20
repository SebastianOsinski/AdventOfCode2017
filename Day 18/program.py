import time
from threading import Thread
from queue import Queue

class Program(Thread):

    def __init__(self, program_id, instructions):
        Thread.__init__(self)
        self.program_id = program_id
        self.instructions = instructions
        self.registers = {}
        self.counter = 0
        self.rcv_queue = Queue()
        self.snd_queue = None
        self.snd_counter = 0

    def run(self):
        while (0 <= self.counter < len(self.instructions)):
            self.execute(self.instructions[self.counter])
    
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
        self.snd_queue.put(self.value(arg))
        self.snd_counter += 1
        print(f"snd {self.program_id}: {self.value(arg)}, {self.snd_counter}", flush=True)
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

    def rcv(self, register):
        self.registers[register] = self.rcv_queue.get()
        print(f"rcv {self.program_id}: {self.registers[register]}", flush=True)
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
        default_value = self.program_id if register == 'p' else 0
        return self.registers.get(register, default_value)

    def increment_counter(self):
        self.counter += 1