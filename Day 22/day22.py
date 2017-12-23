# pylint: disable=invalid-name
import sys
import os
from virus import Virus

path = os.path.join(sys.path[0], "day22_input")
file = open(path, "r")

infection_map = []
no_of_bursts = 10_000

for line in file:
    infection_map.append([c == '#' for c in list(line.rstrip(os.linesep))])

virus = Virus(infection_map, no_of_bursts)
virus.start()

print(virus.infecting_bursts_count)