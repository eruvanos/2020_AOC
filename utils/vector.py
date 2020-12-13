import math
from typing import NamedTuple


class Vector(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        x, y = other
        return Vector(self.x + x, self.y + y)

    def __sub__(self, other):
        x, y = other
        return Vector(self.x + x, self.y + y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def rotate_degree(self, degree):
        """
        Rotate clockwise
        """
        return self.rotate(math.radians(degree))

    def rotate(self, radian):
        """
        Rotate clockwise
        """
        cos = math.cos(-radian)
        sin = math.sin(-radian)
        x = self.x * cos - self.y * sin
        y = self.x * sin + self.y * cos
        return Vector(round(x), round(y))
