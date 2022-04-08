from src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    name = 'Triangle'

    def __new__(cls, first_side, second_side, third_side):
        if first_side < 0 or second_side < 0 or third_side < 0 or (first_side > second_side + third_side) or (
                second_side > first_side + third_side) or (third_side > first_side + second_side):
            return None
        return super(Triangle, cls).__new__(cls)

    def __init__(self, first_side, second_side, third_side):
        self.__first_side = first_side
        self.__second_side = second_side
        self.__third_side = third_side

    @property
    def perimeter(self):
        return self.__first_side + self.__second_side + self.__third_side

    @property
    def area(self):
        half_of_perimeter = self.perimeter / 2
        return sqrt(
            half_of_perimeter * (half_of_perimeter - self.__first_side) * (half_of_perimeter - self.__second_side) * (
                    half_of_perimeter - self.__third_side))
