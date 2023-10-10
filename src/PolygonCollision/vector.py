class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def subtract(self, other):
        return Vector(self.x - other.x, self.y - other.y)