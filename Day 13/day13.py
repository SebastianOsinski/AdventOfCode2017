# pylint: disable=invalid-name
import sys
import os
from layer import Layer

path = os.path.join(sys.path[0], "day13_input")
file = open(path, "r")

index = 0
layers = []
for line in file:
    k, rng = [int(s) for s in line.split(": ")]
    
    while k > index:
        layers.append(None)
        index += 1
    
    layers.append(Layer(rng))
    index += 1

time = 0

# Part 1

total_severity = 0
for i in range(len(layers)):
    layer = layers[i]
    if layer is not None:
        if layer.scanner_position(i) == 0:
            total_severity += i * layer.range

print(total_severity)


# Part 2

delay = 0

perfect_delay_found = False
while not perfect_delay_found:
    for i in range(len(layers)):
        layer = layers[i]
        if layer is not None:
            if layer.scanner_position(i + delay) == 0:
                break
        if i == len(layers) - 1:
            perfect_delay_found = True
    
    if perfect_delay_found:
        break
    else:
        delay += 1

print(delay)