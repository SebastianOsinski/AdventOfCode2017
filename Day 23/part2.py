from math import sqrt

h = 0
b = 93 * 100 + 100_000
c = b + 17_000

def prime(number):
    if number < 2:
        return False

    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


for i in range(b, c + 1, 17):
    if not prime(i):
        h += 1

print(h)