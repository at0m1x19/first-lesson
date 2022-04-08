import pytest

from src.Square import Square
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Circle import Circle


@pytest.fixture
def triangle():
    triangle = Triangle(first_side=10.5, second_side=21, third_side=14)
    yield triangle
    del triangle


@pytest.fixture
def triangle_first_side_too_big():
    triangle = Triangle(first_side=36, second_side=21, third_side=14)
    yield triangle
    del triangle


@pytest.fixture
def triangle_second_side_too_big():
    triangle = Triangle(first_side=10.5, second_side=30, third_side=14)
    yield triangle
    del triangle


@pytest.fixture
def triangle_third_side_too_big():
    triangle = Triangle(first_side=10.5, second_side=21, third_side=31.51)
    yield triangle
    del triangle


@pytest.fixture
def triangle_first_side_less_than_zero():
    triangle = Triangle(first_side=-1, second_side=21, third_side=14)
    yield triangle
    del triangle


@pytest.fixture
def triangle_second_side_less_than_zero():
    triangle = Triangle(first_side=10.5, second_side=-21, third_side=14)
    yield triangle
    del triangle


@pytest.fixture
def triangle_third_side_less_than_zero():
    triangle = Triangle(first_side=10.5, second_side=21, third_side=-4.5)
    yield triangle
    del triangle


@pytest.fixture
def rectangle():
    rectangle = Rectangle(length=20.1, width=30)
    yield rectangle
    del rectangle


@pytest.fixture
def rectangle_length_not_greater_than_zero():
    rectangle = Rectangle(length=-20.1, width=30)
    yield rectangle
    del rectangle


@pytest.fixture
def rectangle_width_not_greater_than_zero():
    rectangle = Rectangle(length=20.1, width=-1)
    yield rectangle
    del rectangle


@pytest.fixture
def square():
    square = Square(side=21.4)
    yield square
    del square


@pytest.fixture
def square_side_not_greater_than_zero():
    square = Square(side=0)
    yield square
    del square


@pytest.fixture
def circle():
    circle = Circle(radius=11.5)
    yield circle
    del circle


@pytest.fixture
def circle_radius_not_greater_than_zero():
    circle = Circle(radius=-1.5)
    yield circle
    del circle
