class Machine:

    def __init__(self):
        self.state = 'A'
        self.cursor_position = 0
        self.tape = {}

    def run(self, times):
        for _ in range(times):
            if self.state is 'A':
                self.in_state_A()
            elif self.state is 'B':
                self.in_state_B()
            elif self.state is 'C':
                self.in_state_C()
            elif self.state is 'D':
                self.in_state_D()
            elif self.state is 'E':
                self.in_state_E()
            else:
                self.in_state_F()
    
    def in_state_A(self):
        if self.current_value() == 0:
            self.write_1_to_current_slot()
            self.move_right()
            self.state = 'B'
        else:
            self.write_0_to_current_slot()
            self.move_left()
            self.state = 'C'

    def in_state_B(self):
        if self.current_value() == 0:
            self.write_1_to_current_slot()
            self.move_left()
            self.state = 'A'
        else:
            self.write_1_to_current_slot()
            self.move_right()
            self.state = 'C'

    def in_state_C(self):
        if self.current_value() == 0:
            self.write_1_to_current_slot()
            self.move_right()
            self.state = 'A'
        else:
            self.write_0_to_current_slot()
            self.move_left()
            self.state = 'D'
    
    def in_state_D(self):
        if self.current_value() == 0:
            self.write_1_to_current_slot()
            self.move_left()
            self.state = 'E'
        else:
            self.write_1_to_current_slot()
            self.move_left()
            self.state = 'C'

    def in_state_E(self):
        if self.current_value() == 0:
            self.write_1_to_current_slot()
            self.move_right()
            self.state = 'F'
        else:
            self.write_1_to_current_slot()
            self.move_right()
            self.state = 'A'

    def in_state_F(self):
        if self.current_value() == 0:
            self.write_1_to_current_slot()
            self.move_right()
            self.state = 'A'
        else:
            self.write_1_to_current_slot()
            self.move_right()
            self.state = 'E'

    def write_0_to_current_slot(self):
        self.tape[self.cursor_position] = 0

    def write_1_to_current_slot(self):
        self.tape[self.cursor_position] = 1

    def current_value(self):
        return self.tape.get(self.cursor_position, 0)

    def move_right(self):
        self.cursor_position += 1
    
    def move_left(self):
        self.cursor_position -= 1

    def checksum(self):
        sum = 0
        for value in self.tape.values():
            sum += value
        return sum

    

    