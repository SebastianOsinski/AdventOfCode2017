# pylint: disable=invalid-name
import sys
import os
from knot_hash import knot
from knot_hash import knot_hash

path = os.path.join(sys.path[0], "day10_input")
file = open(path, "r")

input = file.readline()
lengths = [int(l) for l in input.split(",")]

numbers = list(range(256))

# Part 1
knot(numbers, lengths, (0, 0))
print(numbers[0] * numbers[1])

# Part 2

print(knot_hash(input))
