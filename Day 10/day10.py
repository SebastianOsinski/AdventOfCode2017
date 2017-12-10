# pylint: disable=invalid-name
import sys
import os

path = os.path.join(sys.path[0], "day10_input")
file = open(path, "r")

input = file.readline()
lengths = [int(l) for l in input.split(",")]

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
    return (current_position, skip_size)


# Part 1
knot(numbers, lengths, (0, 0))
print(numbers[0] * numbers[1])

# Part 2

def chunks(list, n):
    return [list[i:i + n] for i in range(0, len(list), n)]

def padded_hex(dec):
    return "{0:02x}".format(dec)

def knot_hash(string):
    lengths = [ord(c) for c in string] + [17, 31, 73, 47, 23]

    number_of_rounds = 64

    params = (0, 0)

    numbers = list(range(256))
    numbers_length = len(numbers)

    for _ in range(number_of_rounds):
        params = knot(numbers, lengths, params)

    number_chunks = chunks(numbers, 16)
    dense_hash = [reduce(lambda x, y: x ^ y, chunk) for chunk in number_chunks]

    return "".join([padded_hex(num) for num in dense_hash])



print(knot_hash(input))
