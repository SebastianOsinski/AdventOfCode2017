from generator import Generator

initA = 116
initB = 299

factorA = 16807
factorB = 48271

def count(generatorA, generatorB, number_of_pairs):
    counter = 0
    mask = int("0b1111111111111111", 2)

    for _ in range(number_of_pairs):
        valueA = generatorA.next()
        valueB = generatorB.next()

        if valueA & mask == valueB & mask:
            counter += 1

    return counter

# Part 1

generatorA = Generator(initA, factorA)
generatorB = Generator(initB, factorB)
print(count(generatorA, generatorB, 40000000))

# Part 2

generatorA = Generator(initA, factorA, lambda x: x % 4 == 0)
generatorB = Generator(initB, factorB, lambda x: x % 8 == 0)
print(count(generatorA, generatorB, 5000000))

