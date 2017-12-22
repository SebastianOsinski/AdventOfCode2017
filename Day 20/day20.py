# pylint: disable=invalid-name
import sys
import os
import copy
from particle import Particle

path = os.path.join(sys.path[0], "day20_input")
file = open(path, "r")

particles = []

def parse_vector(string):
    stripped = string[3:][:-1]
    x, y, z = [int(d) for d in stripped.split(",")]
    return (x, y, z)

def argmax(array):
    max_index = 0
    for i in range(len(array)):
        if array[i] > array[max_index]:
            max_index = i

    return max_index

for line in file:
    p, v, a = [parse_vector(string) for string in line.rstrip(os.linesep).split(", ")]
    particles.append(Particle(p, v, a))


number_of_ticks = 1000

times_as_closest_particle = [0] * len(particles)

# Part 1

part1_particles = copy.deepcopy(particles)

for _ in range(number_of_ticks):
    closest_particle_index = 0
    for i in range(len(part1_particles)):
        particle = part1_particles[i]
        particle.tick()

        if particle.distance_from_zero() < part1_particles[closest_particle_index].distance_from_zero():
            closest_particle_index = i

    times_as_closest_particle[closest_particle_index] += 1

print(argmax(times_as_closest_particle))

# Part 2

part2_particles = copy.deepcopy(particles)

for _ in range(number_of_ticks):
    particles_at_position = {}
    for i in range(len(part2_particles)):
        particle = part2_particles[i]
        particle.tick()

        if particle.p in particles_at_position:
            particles_at_position[particle.p].append(i)
        else:
            particles_at_position[particle.p] = [i]
    
    indices_to_remove = []

    for _, indices in particles_at_position.items():
        if len(indices) > 1:
            indices_to_remove.extend(indices)

    indices_to_remove.sort(reverse=True)

    for index in indices_to_remove:
        del part2_particles[index]

print(len(part2_particles))



