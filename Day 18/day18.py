# pylint: disable=invalid-name
import sys
import os
from program import Program

path = os.path.join(sys.path[0], "day18_input")
file = open(path, "r")

instructions = file.read().splitlines()
print(instructions)

program0 = Program(0, instructions)
program1 = Program(1, instructions)

program0.snd_queue = program1.rcv_queue
program1.snd_queue = program0.rcv_queue


program0.start()
program1.start()
