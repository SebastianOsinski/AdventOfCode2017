# pylint: disable=invalid-name
import sys
import os
from path_follower import PathFollower

path = os.path.join(sys.path[0], "day19_input")
file = open(path, "r")

diagram = []

for line in file:
    diagram.append(list(line.rstrip(os.linesep)))

path_follower = PathFollower()
path_follower.follow(diagram)

print("".join(path_follower.visited_letters))
print(path_follower.step_counter)
