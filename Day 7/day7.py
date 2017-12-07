import re

from Program import Program

file = open("day7_input", "r")

pattern = re.compile("([a-z]+) \((\d+)\)(?: -> ([a-z, ]+))?")

possible_roots_names = []
parent_of = {}

children_of = {}
program_with_name = {}

# Part 1

# find root and build dictionaries of children
for line in file:
    match = pattern.match(line)

    name = match.group(1)
    weight = int(match.group(2))

    children_string = match.group(3)

    # omit programs without children - they can't be root
    if children_string is not None:
        children_of_current_program = children_string.split(", ")
        possible_roots_names.append(name)

        for child in children_of_current_program:
            parent_of[child] = name
    else:
        children_of_current_program = []

    children_of[name] = children_of_current_program

    program_with_name[name] = Program(name, weight, [])

root_name = None

for program in possible_roots_names:
    if program not in parent_of:
        root_name = program
        break

print("Root: ")
print(root_name)

# build tree

def build(node_name):
    node = program_with_name[node_name]
    if node.name in children_of:
        node.children = [build(child) for child in children_of[node.name]]
    return node

tree = build(root_name)

# Part 2

weight = tree.find_correct_weight_for_wrongly_weighted_program(None)
print(weight)
