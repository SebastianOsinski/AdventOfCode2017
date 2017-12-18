# pylint: disable=invalid-name
import sys
import os
from program import Program

path = os.path.join(sys.path[0], "day18_input")
file = open(path, "r")

instructions = file.read().splitlines()

program = Program()

program.run(instructions)