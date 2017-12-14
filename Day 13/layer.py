class Layer:

    def __init__(self, range):
        self.range = range

    def scanner_position(self, time):
        last = self.range - 1
        return last - abs(time % (2 * last) - last)