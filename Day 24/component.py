class Component:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"{self.a}/{self.b}"

    def rotate(self):
        (self.a, self.b) = (self.b, self.a)

    def has_zero(self):
        return self.a == 0 or self.b == 0
