file = open("day1_input", "r")

string = file.read()

numbers = list(map(int, list(string)))

sum = 0

step = int(len(numbers) / 2)

for i in range(0, len(numbers)):
    lhs = numbers[i]
    rhs = numbers[(i + step) % len(numbers)]

    if lhs == rhs:
        sum += lhs

print(sum)