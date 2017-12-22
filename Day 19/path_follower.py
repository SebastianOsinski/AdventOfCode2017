from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class PathFollower:
    VERTICAL = '|'
    HORIZONTAL = '-'
    CROSSING = '+'
    EMPTY = " "

    POSITION_TRANSLATION = {
        Direction.UP: lambda pos: (pos[0], pos[1] - 1),
        Direction.DOWN: lambda pos: (pos[0], pos[1] + 1),
        Direction.LEFT: lambda pos: (pos[0] - 1, pos[1]),
        Direction.RIGHT: lambda pos: (pos[0] + 1, pos[1])
    }

    BLOCKED_DIRECTION = {
        Direction.UP: Direction.DOWN,
        Direction.DOWN: Direction.UP,
        Direction.LEFT: Direction.RIGHT,
        Direction.RIGHT: Direction.LEFT
    }

    DIRECTION_LINE_SYMBOL = {
        Direction.UP: VERTICAL,
        Direction.DOWN: VERTICAL,
        Direction.LEFT: HORIZONTAL,
        Direction.RIGHT: HORIZONTAL
    }  

    def __init__(self):
        self.clear()

    def clear(self):
        self.diagram = None
        self.current_position = None
        self.finished = False
        self.direction = None
        self.visited_letters = []
        self.step_counter = 0

    def follow(self, diagram):
        self.clear()
        self.diagram = diagram
        self.find_starting_position()
        while not self.finished:
            self.move_from_current_position()

    def find_starting_position(self):
        self.direction = Direction.DOWN
        for i in range(0, len(self.diagram[0])):
            if self.diagram[0][i] is self.VERTICAL:
                self.current_position = (i, 0)
                break

    def move_from_current_position(self):
        if self.symbol_at_current_position() is self.EMPTY:
            self.finished = True
            return

        self.move(self.POSITION_TRANSLATION[self.direction])
        self.step_counter += 1

    def move(self, update_position):
        if self.symbol_at_current_position() in [self.VERTICAL, self.HORIZONTAL]:
            self.current_position = update_position(self.current_position)
        elif self.is_current_symbol_letter():
            self.visited_letters.append(self.symbol_at_current_position())
            self.current_position = update_position(self.current_position)
        elif self.symbol_at_current_position() is self.CROSSING:
            self.resolve_crossing()
        else:
            raise Exception("Unexpected symbol: " + self.symbol_at_current_position())

    def resolve_crossing(self):
        possible_directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        possible_directions.remove(self.BLOCKED_DIRECTION[self.direction])

        for direction in possible_directions:
            position = self.POSITION_TRANSLATION[direction](self.current_position)
            symbol = self.symbol_at_position(position)
            if symbol is not None and (symbol is self.DIRECTION_LINE_SYMBOL[direction] or self.is_symbol_letter(symbol)):
                self.current_position = position
                self.direction = direction
                return

        raise Exception("Couldn't resolve crossing")

    def symbol_at_position(self, position):
        dimY = len(self.diagram)
        dimX = len(self.diagram[0])

        if 0 <= position[0] < dimX and 0 <= position[1] < dimY:
            return self.diagram[position[1]][position[0]]
        else:
            return None

    def symbol_at_current_position(self):
        return self.symbol_at_position(self.current_position)

    def is_symbol_letter(self, symbol):
        return ord('A') <= ord(symbol) <= ord('Z')

    def is_current_symbol_letter(self):
        return self.is_symbol_letter(self.symbol_at_current_position())
        