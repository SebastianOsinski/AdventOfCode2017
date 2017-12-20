import time
from queue import Queue

class Program:

    def __init__(self, program_id, instructions):
        self.program_id = program_id
        self.instructions = instructions
        self.registers = {}
        self.counter = 0
        self.rcv_queue = Queue()
        self.snd_queue = None
        self.snd_counter = 0
        self.waits_for_rcv = False

    def run(self):
        while self.can_run():
            self.execute(self.instructions[self.counter])
            
    def can_run(self):
        return (0 <= self.counter < len(self.instructions)) and (not self.waits_for_rcv or (self.waits_for_rcv and not self.rcv_queue.empty()))
    
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
        self.increment_counter()
            
    def set(self, register, arg):
        self.registers[register] = self.value(arg)
        self.increment_counter()

    def add(self, register, arg):
        self.arithmetic_operation(register, arg, lambda a, b: a + b)
    
    def mul(self, register, arg):
        self.arithmetic_operation(register, arg, lambda a, b: a * b)

    def mod(self, register, arg):
        self.arithmetic_operation(register, arg, lambda a, b: a % b)

    def rcv(self, register):
        if self.rcv_queue.empty():
            self.waits_for_rcv = True
            return
        else:
            self.waits_for_rcv = False

        self.registers[register] = self.rcv_queue.get()
        self.increment_counter()
    
    def jgz(self, arg0, arg1):
        if self.value(arg0) > 0:
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
        default_value = self.program_id if register is 'p' else 0
        return self.registers.get(register, default_value)

    def increment_counter(self):
        self.counter += 1