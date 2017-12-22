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

    def __init__(self, diagram):
        self.diagram = diagram
        self.current_position = None
        self.finished = False
        self.direction = None
        self.visited_letters = []
        self.step_counter = 0

    def follow(self):
        self.find_starting_point()
        while not self.finished:
            print(f"{self.symbol_at_current_position()} {self.current_position}")
            self.move_from_current_position()


    def find_starting_point(self):
        self.direction = Direction.DOWN
        for i in range(0, len(self.diagram[0])):
            if self.diagram[0][i] is self.VERTICAL:
                self.current_position = (i, 0)
                break

    def move_from_current_position(self):
        if self.symbol_at_current_position() is self.EMPTY:
            self.finished = True
            return

        if self.direction == Direction.UP:
            self.move(self.update_position_up)
        elif self.direction == Direction.DOWN:
            self.move(self.update_position_down)
        elif self.direction == Direction.LEFT:
            self.move(self.update_position_left)
        else:
            self.move(self.update_position_right)

        self.step_counter += 1

    def symbol_at_position(self, position):
        dimY = len(self.diagram)
        dimX = len(self.diagram[0])

        if 0 <= position[0] < dimX and 0 <= position[1] < dimY:
            return self.diagram[position[1]][position[0]]
        else:
            return None

    def symbol_at_current_position(self):
        return self.symbol_at_position(self.current_position)

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

    def update_position_up(self, position):
        (x, y) = position
        return (x, y - 1)

    def update_position_down(self, position):
        (x, y) = position
        return (x, y + 1)

    def update_position_left(self, position):
        (x, y) = position
        return (x - 1, y)

    def update_position_right(self, position):
        (x, y) = position
        return (x + 1, y)

    def resolve_crossing(self):
        blocked_direction = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }   
        possible_directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        possible_directions.remove(blocked_direction[self.direction])

        if Direction.UP in possible_directions:
            up_position = self.update_position_up(self.current_position)
            symbol = self.symbol_at_position(up_position)
            if symbol is not None and (symbol is self.VERTICAL or self.is_symbol_letter(symbol)):
                self.current_position = up_position
                self.direction = Direction.UP
                return
        
        if Direction.DOWN in possible_directions:
            down_position = self.update_position_down(self.current_position)
            symbol = self.symbol_at_position(down_position)
            if symbol is not None and (symbol is self.VERTICAL or self.is_symbol_letter(symbol)):
                self.current_position = down_position
                self.direction = Direction.DOWN
                return

        if Direction.LEFT in possible_directions:
            left_position = self.update_position_left(self.current_position)
            symbol = self.symbol_at_position(left_position)
            if symbol is not None and (symbol is self.HORIZONTAL or self.is_symbol_letter(symbol)):
                self.current_position = left_position
                self.direction = Direction.LEFT
                return

        if Direction.RIGHT in possible_directions:
            right_position = self.update_position_right(self.current_position)
            symbol = self.symbol_at_position(right_position)
            if symbol is not None and (symbol is self.HORIZONTAL or self.is_symbol_letter(symbol)):
                self.current_position = right_position
                self.direction = Direction.RIGHT
                return

        raise Exception("Couldn't resolve crossing")

    def is_symbol_letter(self, symbol):
        return 65 <= ord(symbol) <= 90

    def is_current_symbol_letter(self):
        return self.is_symbol_letter(self.symbol_at_current_position())
        