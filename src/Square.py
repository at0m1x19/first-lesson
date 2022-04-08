from src.Figure import Figure


class Square(Figure):
    name = 'Square'

    def __new__(cls, side):
        if side <= 0:
            return None
        return super(Square, cls).__new__(cls)

    def __init__(self, side):
        self.__side = side

    @property
    def perimeter(self):
        return self.__side * 4

    @property
    def area(self):
        return self.__side ** 2
