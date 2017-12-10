# pylint: disable=invalid-name
import sys
import os

path = os.path.join(sys.path[0], "day10_input")
file = open(path, "r")

lengths = [int(l) for l in file.readline().split(",")]

numbers = list(range(256))

numbers_length = len(numbers)

def reverse(list, position, length):
    list_len = len(list)
    for o in range(int((length + 1) / 2)):
        i = (position + o) % list_len
        j = (length + position - o - 1) % list_len

        (list[i], list[j]) = (list[j], list[i])

def knot(list, lengths, params):
    current_position = params[0]
    skip_size = params[1]
    for length in lengths:
        reverse(list, current_position, length)
        current_position = (current_position + length + skip_size) % numbers_length
        skip_size += 1


# Part 1
knot(numbers, lengths, (0, 0))

print(numbers[0] * numbers[1])