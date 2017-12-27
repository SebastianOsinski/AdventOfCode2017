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

def flip(matrix):
    flipped_matrix = []

    size = len(matrix)

    for i in range(size):
        flipped_matrix.append(matrix[i][::-1])

    return flipped_matrix

def empty_grid(size):
    grid = []
    for _ in range(size):
        grid.append(['.'] * size)
    return grid

def submatrix(matrix, top_left_corner_x, top_left_corner_y, size):
    submatrix = empty_grid(size)

    for i in range(size):
        for j in range(size):
            submatrix[i][j] = matrix[top_left_corner_x + i][top_left_corner_y + j]

    return submatrix

def enhanced(matrix):
    input = matrix
    for _ in range(4):
        key = str(input)
        if key in RULES:
            return RULES[key]

        flipped_input = flip(input)
        key = str(flipped_input)

        if key in RULES:
            return RULES[key]
        input = rotate_right(input)
    raise Exception("No rule for given input " + str(input))

def replace_in_matrix(matrix, submatrix, top_left_corner_x, top_left_corner_y):
    size = len(submatrix)
    for i in range(size):
        for j in range(size):
            matrix[top_left_corner_x + i][top_left_corner_y + j] = submatrix[i][j]

def enhance(grid):
    size = len(grid)

    if size % 2 == 0:
        times = len(grid) // 2
        new_size = times * 3
        step = 2
        new_step = 3
    else:
        times = len(grid) // 3
        new_size = times * 4
        step = 3
        new_step = 4

    new_grid = empty_grid(new_size)

    for i in range(times):
        for j in range(times):
            subgrid = submatrix(grid, i * step, j * step, step)
            enhanced_subgrid = enhanced(subgrid)
            replace_in_matrix(new_grid, enhanced_subgrid, i * new_step, j * new_step)

    return new_grid

def count_on_pixels(grid):
    size = len(grid)
    count = 0
    for i in range(size):
        for j in range(size):
            if grid[i][j] is '#':
                count += 1

    return count

grid = [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]
iterations = 18

for i in range(iterations):
    grid = enhance(grid)

print(count_on_pixels(grid))