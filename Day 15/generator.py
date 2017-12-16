class Generator:

    def __init__(self, initial_value, factor, acceptance_criterion = lambda x: True):
        self.previous_value = initial_value
        self.factor = factor
        self.acceptance_criterion = acceptance_criterion
    
    def next(self):
        next_value = (self.previous_value * self.factor) % 2147483647
        self.previous_value = next_value
        if self.acceptance_criterion(next_value):
            return next_value
        else:
            return self.next()
