import math


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def __str__(self):
        return f"Circle({self.radius})"

    def __repr__(self):
        return self.__str__()

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value=1):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self._radius = value

    @property
    def diameter(self):
        self._diameter = self._radius * 2
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = self._diameter / 2

    @property
    def area(self):
        return math.pi * self._radius ** 2
