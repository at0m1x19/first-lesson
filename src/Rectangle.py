from src.Figure import Figure


class Rectangle(Figure):
    name = 'Rectangle'

    def __new__(cls, length, width):
        if length <= 0 or width <= 0:
            return None
        return super(Rectangle, cls).__new__(cls)

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def perimeter(self):
        return (self.__length + self.__width) * 2

    @property
    def area(self):
        return self.__length * self.__width
