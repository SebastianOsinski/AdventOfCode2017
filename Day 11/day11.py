# pylint: disable=invalid-name
import sys
import os

path = os.path.join(sys.path[0], "day11_input")
file = open(path, "r")

directions = file.readline()

def steps_minimized_x(x, y, z):
    return abs(y - x) + abs(z - x) 

def steps_minimized_y(x, y, z):
    return abs(x - y) + abs(z- y) 

def steps_minimized_z(x, y, z):
    return abs(x - z) + abs(y - z) 

def min_steps(x, y, z):
    return min([steps_minimized_x(x, y, z), steps_minimized_y(x, y, z), steps_minimized_z(x, y, z)])

def count_steps(directions):
    x = 0
    y = 0
    z = 0

    step = {"n": -1, "s": 1, "nw": 1, "se": -1, "ne": 1, "sw": -1}

    furthest_steps = 0

    for direction in directions.split(","):
        if direction in ["nw", "se"]:
            x += step[direction]
        elif direction in ["ne", "sw"]:
            y += step[direction]
        else:
            z += step[direction]
        furthest_steps = max(furthest_steps, min_steps(x, y, z))



    return (min_steps(x, y, z), furthest_steps)


print(count_steps(directions))