class Particle:

    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a
    
    def tick(self):
        self.v = (self.v[0] + self.a[0], self.v[1] + self.a[1], self.v[2] + self.a[2])
        self.p = (self.p[0] + self.v[0], self.p[1] + self.v[1], self.p[2] + self.v[2])

    def distance_from_zero(self):
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])