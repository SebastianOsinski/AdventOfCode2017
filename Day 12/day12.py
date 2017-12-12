# pylint: disable=invalid-name
import sys
import os

path = os.path.join(sys.path[0], "day12_input")
file = open(path, "r")

index = 0
ls = []
for line in file:
    programs = [int(s) for s in line.split(" <-> ")[1].split(", ")]
    ls.append(programs)
    index += 1



def create_group_with_program(program_to_trace):
    visited_programs = set()

    def trace(index):
        programs = ls[index]
        should_trace = [(program not in visited_programs) for program in programs]

        for program in programs:
            visited_programs.add(program)
    
        for (program, should) in zip(programs, should_trace):
            if should:
                trace(program)

    trace(program_to_trace)
    return visited_programs

# Part 1
print(len(create_group_with_program(0)))

# Part 2

groups = []

for index in range(len(ls)):
    if not filter(lambda s: (index in s), groups):
        groups.append(create_group_with_program(index))

print(len(groups))