input = 335

class CircularBuffer:

    def __init__(self, steps):
        self.steps = steps
        self.current_position = 0
        self.buffer = [0]

    def insert(self, value):
        insertion_index = ((self.current_position + self.steps)) % len(self.buffer) + 1
        self.buffer.insert(insertion_index, value)
        self.current_position = insertion_index

    def index(self, value):
        return self.buffer.index(value)

    def value(self, index):
        return self.buffer[index % len(self.buffer)]

# Part 1

buffer = CircularBuffer(input)

for i in range(1, 2018):
    buffer.insert(i)

print(buffer.buffer[buffer.current_position + 1])

# Part 2

def value_next_to_0(step):
    current_position = 0
    value = 0
    for i in range(1, 50_000_000 + 1):
        current_position = (current_position + step) % i + 1
        if current_position == 1:
            value = i
    return(value)

print(value_next_to_0(input))