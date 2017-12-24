# pylint: disable=invalid-name
import sys
import os
from copy import deepcopy
from component import Component

path = os.path.join(sys.path[0], "day24_input")
file = open(path, "r")

components = []

for line in file:
    a,b = [int(d) for d in line.split("/")]
    components.append(Component(a, b))

def find_zeros_and_rest(components):
    pairs = []

    for i in range(len(components) - 1, -1, -1):
        component = components[i]
        if component.has_zero():
            components_copy = deepcopy(components)
            if component.a != 0:
                component.rotate()
            del components_copy[i]

            pairs.append((component, components_copy))

    return pairs

def find_strongest_subcomponents(start, rest_of_components):
    if len(rest_of_components) == 0:
        return ([], 0)

    strongest_subcomponents = []
    strongest_subcomponents_strength = 0

    for i in range(len(rest_of_components) - 1, -1, -1):
        if rest_of_components[i].a == start.b or rest_of_components[i].b == start.b:
            rest_copy = deepcopy(rest_of_components)

            sub_start = rest_copy.pop(i)

            if sub_start.b == start.b:
                sub_start.rotate()

            subcomponents, subcomponents_strength = find_strongest_subcomponents(sub_start, rest_copy)

            if len(subcomponents) > len(strongest_subcomponents):
                strongest_subcomponents = subcomponents
                strongest_subcomponents_strength = subcomponents_strength
            elif len(subcomponents) == len(strongest_subcomponents) and subcomponents_strength > strongest_subcomponents_strength:
                strongest_subcomponents = subcomponents
                strongest_subcomponents_strength = subcomponents_strength

    return ([start] + strongest_subcomponents, start.a + start.b + strongest_subcomponents_strength)


def find_strongest(components):
    zeros_rest_pairs = find_zeros_and_rest(components)

    max_strength = 0
    max_length = 0

    for pair in zeros_rest_pairs:
        zero = pair[0]
        rest = pair[1]

        subcomponents, subcomponents_strength  = find_strongest_subcomponents(zero, rest)

        if len(subcomponents) > max_length:
            max_length = len(subcomponents)
            max_strength = subcomponents_strength
        elif len(subcomponents) == max_length and subcomponents_strength > max_strength:
            max_strength = subcomponents_strength

    return max_strength

print(find_strongest(components))