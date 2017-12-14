import sys
import os  

path = os.path.join(sys.path[0], "../Day 10")
sys.path.append(path)

from knot_hash import knot_hash

input = "hxtvlmkl"

rows = []

square_count = 0

def hex_to_bin(hex):
     return bin(int(hex, 16))[2:].zfill(4)

def bin_to_symbol(bin):
    if bin:
        return "#"
    else:
        return "."

for i in range(128):
    hash = knot_hash(input + "-" + str(i))
    row = [int(d) for d in "".join([hex_to_bin(c) for c in hash])]
    square_count += reduce(lambda a, b: a + b, row)
    rows.append(row)

# Part 1
print(square_count)

grid = []

for row in rows:
    grid_row = []
    for b in row:
        grid_row.append(bin_to_symbol(b))
    grid.append(grid_row)
   
def check_square(grid, row, col, current_region):
    if (not row in range(0, len(grid))) or (not col in range(0, len(grid))):
        return False
    
    if grid[row][col] == "#":
        grid[row][col] = str(current_region)
    else:
        return False

    neighbours = [(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)]

    for neighbour in neighbours:
        check_square(grid, neighbour[0], neighbour[1], current_region)

    return True

def print_grid(grid):
    for row in grid:
        print("".join(row))

#print_grid(grid)

def count_regions(grid):
    current_region = 1
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            #print("{0} {1}".format(r, c))
            if check_square(grid, r, c, current_region):
                current_region += 1

    return current_region - 1


# Part 2
print(count_regions(grid))