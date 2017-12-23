from enum import Enum

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def rotated_right(self):
        return Direction((self.value + 1) % 4)

    def rotated_left(self):
        return Direction((self.value - 1) % 4)

class State(Enum):
    CLEAN = 0
    WEAKENED = 1
    INFECTED = 2
    FLAGGED = 3

    SYMBOLS = {CLEAN: ".", WEAKENED: "W", INFECTED: "#", FLAGGED: "F"}

    def next(self):
        return State((self.value + 1) % 4)

    def symbol(self):
        return self.SYMBOLS[self]


class Virus:

    def __init__(self, infection_map, no_of_bursts):
        self.infection_map = infection_map
        self.no_of_bursts = no_of_bursts
        self.current_x = len(infection_map[0]) // 2
        self.current_y = len(infection_map) // 2
        self.direction = Direction.UP
        self.infecting_bursts_count = 0 

    def start(self):
        for _ in range(self.no_of_bursts):
            self.resize_map_if_needed()
            self.burst()

    def burst(self):
        is_current_infected = self.infection_map[self.current_x][self.current_y] == State.INFECTED

        if is_current_infected:
            self.direction = self.direction.rotated_right()
        else:
            self.direction = self.direction.rotated_left()

        self.infection_map[self.current_x][self.current_y] = State.CLEAN if is_current_infected else State.INFECTED

        if not is_current_infected:
            self.infecting_bursts_count += 1

        if self.direction is Direction.UP:
            self.current_x -= 1
        elif self.direction is Direction.DOWN:
            self.current_x += 1
        elif self.direction is Direction.RIGHT:
            self.current_y += 1
        else:
            self.current_y -= 1

    def resize_map_if_needed(self):
        if (0 < self.current_x < len(self.infection_map[0])) and (0 < self.current_y < len(self.infection_map)):
            return

        new_width = len(self.infection_map[0]) + 2

        resized_map = [[State.CLEAN] * new_width]

        for row in self.infection_map:
            new_row = [State.CLEAN]
            new_row.extend(row)
            new_row.append(State.CLEAN)
            resized_map.append(new_row)

        resized_map.append([State.CLEAN] * new_width)

        self.infection_map = resized_map

        self.current_x += 1
        self.current_y += 1

    def print_map(self):
        for r in range(len(self.infection_map)):
            row = self.infection_map[r]
            if self.current_x == r:
                line = " ".join(["#" if p else "." for p in row[0:self.current_y]])
                if len(row[0:self.current_y]):
                    line = " " + line
                line += "[" + ("#" if row[self.current_x] else ".") + "]"
                line += " ".join(["#" if p else "." for p in row[self.current_y + 1:]])
                print(line, flush=True)
            else:    
                print(" " + " ".join(["#" if p else "." for p in row]), flush=True)
        print("", flush=True)
    