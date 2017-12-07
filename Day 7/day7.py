import re

file = open("day7_input", "r")

pattern = re.compile("([a-z]+) \((\d+)\)(?: -> ([a-z, ]+))?")

possible_roots = []
parents = {}

# Part 1

for line in file:
    match = pattern.match(line)

    name = match.group(1)
    #weight = int(match.group(2))

    children_string = match.group(3)

    # omit programs without children - they can't be root
    if children_string is not None:
        children = children_string.split(", ")
        possible_roots.append(name)

        for child in children:
            parents[child] = name

for program in possible_roots:
    if program not in parents:
        print(program)