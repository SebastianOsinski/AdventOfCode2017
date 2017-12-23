# pylint: disable=invalid-name
import sys
import os

path = os.path.join(sys.path[0], "day21_input")
file = open(path, "r")

RULES = {}

for line in file:
    input_str, output_str = line.rstrip(os.linesep).split(" => ")

    input = [list(row) for row in input_str.split("/")]
    output = [list(row) for row in output_str.split("/")]

    RULES[str(input)] = output

def rotate_right(matrix):
    rotated_matrix = []

    size = len(matrix)

    for x in range(size):
        row = []
        for y in range(size):
            row.append(matrix[size - 1 - y][x])
        rotated_matrix.append(row)

    return rotated_matrix


print(rotate_right([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))