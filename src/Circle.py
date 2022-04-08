from src.Figure import Figure
from math import pi


class Circle(Figure):
    name = 'Circle'

    def __new__(cls, radius):
        if radius <= 0:
            return None
        return super(Circle, cls).__new__(cls)

    def __init__(self, radius):
        self.__radius = radius

    @property
    def perimeter(self):
        return self.__radius * pi * 2

    @property
    def area(self):
        return self.__radius ** 2 * pi
