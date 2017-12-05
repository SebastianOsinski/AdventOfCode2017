file = open("day5_input", "r")

jumps = [int(line) for line in file.readlines()]

def count_steps(jumps, transform_offset):
    jumps = list(jumps)
    steps = 0
    index = 0

    while index < len(jumps):
        offset = jumps[index]
        jumps[index] = transform_offset(offset)
        index += offset
        steps += 1

    return steps

# Part 1
print(count_steps(jumps, lambda o: o + 1))

# Part 2
print(count_steps(jumps, lambda o: o - 1 if o >= 3 else o + 1))