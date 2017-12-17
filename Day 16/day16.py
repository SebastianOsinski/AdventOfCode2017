# pylint: disable=invalid-name
import sys
import os

path = os.path.join(sys.path[0], "day16_input")
file = open(path, "r")

def find_program_index(program, programs):
    return programs.index(program)

def spin(n, programs):
    programs[:] = programs[-n:] + programs[:-n]

def exchange(first_program_index, second_program_index, programs):
    programs[first_program_index], programs[second_program_index] = programs[second_program_index], programs[first_program_index]

def partner(first_program, second_program, programs):
    first_program_index = find_program_index(first_program, programs)
    second_program_index = find_program_index(second_program, programs)
    exchange(first_program_index, second_program_index, programs)

programs = [chr(i) for i in range(ord('a'), ord('p') + 1)]

moves = file.readline().split(",")

times = 1_000_000_000
t = 0
while t < times:
    for move in moves:
        move_id = move[0]
        params = move[1:]

        if move_id == 's':
            n = int(params)
            spin(n, programs)
        elif move_id == 'x':
            (i, j) = [int(param) for param in params.split("/")]
            exchange(i, j, programs)
        else:
            (first, second) = params.split("/")
            partner(first, second, programs)
        t += 1


print("".join(programs))

