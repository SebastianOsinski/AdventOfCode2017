from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

input = 312051

# Part 1

def find_square_position(square):
    x = 0
    y = 0
    i = 1

    direction = Direction.DOWN
    steps_to_make = 0
    steps_made_in_current_direction = 0

    while i < square:
        if direction == Direction.RIGHT:
            if steps_made_in_current_direction < steps_to_make:
                x += 1
                steps_made_in_current_direction += 1
                i += 1
            else:
                direction = Direction.UP
                steps_made_in_current_direction = 0
        elif direction == Direction.UP:
            if steps_made_in_current_direction < steps_to_make:
                y += 1
                steps_made_in_current_direction += 1
                i += 1
            else:
                direction = Direction.LEFT
                steps_to_make += 1
                steps_made_in_current_direction = 0
        elif direction == Direction.LEFT:
            if steps_made_in_current_direction < steps_to_make:
                x -= 1
                steps_made_in_current_direction += 1
                i += 1
            else:
                direction = Direction.DOWN
                steps_made_in_current_direction = 0
        else:
            if steps_made_in_current_direction < steps_to_make:
                y -= 1
                steps_made_in_current_direction += 1
                i += 1
            else:
                direction = Direction.RIGHT
                steps_to_make += 1
                steps_made_in_current_direction = 0
    return (x, y)

def manhatten_dist(point):
    return abs(point[0]) + abs(point[1])

print(manhatten_dist(find_square_position(input)))

# Part 2

class Spiral:
    square_values = { (0,0): 1 }

    def find_value(self, x, y):
        neighbours = [
            (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
            (x, y - 1), (x, y), (x, y + 1),
            (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
        ]

        value = 0

        for neighbour in neighbours:
            if neighbour in self.square_values:
                value += self.square_values[neighbour]

        self.square_values[(x, y)] = value

        return value

    def find_first_greater(self, number):
        x = 0
        y = 0
        value = 1

        direction = Direction.DOWN
        steps_to_make = 0
        steps_made_in_current_direction = 0

        while value <= number:
            if direction == Direction.RIGHT:
                if steps_made_in_current_direction < steps_to_make:
                    x += 1
                    steps_made_in_current_direction += 1
                    value = self.find_value(x, y)
                else:
                    direction = Direction.UP
                    steps_made_in_current_direction = 0
            elif direction == Direction.UP:
                if steps_made_in_current_direction < steps_to_make:
                    y += 1
                    steps_made_in_current_direction += 1
                    value = self.find_value(x, y)
                else:
                    direction = Direction.LEFT
                    steps_to_make += 1
                    steps_made_in_current_direction = 0
            elif direction == Direction.LEFT:
                if steps_made_in_current_direction < steps_to_make:
                    x -= 1
                    steps_made_in_current_direction += 1
                    value = self.find_value(x, y)
                else:
                    direction = Direction.DOWN
                    steps_made_in_current_direction = 0
            else:
                if steps_made_in_current_direction < steps_to_make:
                    y -= 1
                    steps_made_in_current_direction += 1
                    value = self.find_value(x, y)
                else:
                    direction = Direction.RIGHT
                    steps_to_make += 1
                    steps_made_in_current_direction = 0

        return value

spiral = Spiral()
print(spiral.find_first_greater(input))