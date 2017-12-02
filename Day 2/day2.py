import functools

file = open("day2_input", "r")

lines = file.readlines()

def numbers_from_line( line ):
    return [int(str) for str in line.split("\t")]

matrix = [numbers_from_line(line) for line in lines]

def sum(list):
    sum = 0
    for number in list:
        sum += number
    return sum

# Part 1

max_min_per_row = [(max(row), min(row)) for row in matrix]
checksum1 = sum([s[0] - s[1] for s in max_min_per_row])

print(checksum1)

# Part 2

def divide_divisibles(numbers):
    rng = range(0, len(numbers))
    for i in rng:
        for j in rng:
            if i != j:
                n_i = numbers[i]
                n_j = numbers[j]
                if n_i % n_j == 0:
                    return int(n_i / n_j)
                if n_j % n_i == 0:
                    return int(n_j / n_i)

checksum2 = sum([divide_divisibles(row) for row in matrix])

print(checksum2)
