import pytest


def test_add_area_triangle(rectangle, triangle):
    assert rectangle.add_area(triangle) == rectangle.area + triangle.area


def test_add_area_square(rectangle, square):
    assert rectangle.add_area(square) == rectangle.area + square.area


def test_add_area_circle(rectangle, circle):
    assert rectangle.add_area(circle) == rectangle.area + circle.area


def test_add_area_not_figure(rectangle):
    with pytest.raises(ValueError, match='Incorrect class was passed'):
        rectangle.add_area('String')


def test_name(rectangle):
    assert rectangle.name == 'Rectangle'


def test_perimeter(rectangle):
    assert rectangle.perimeter == 100.2


def test_area(rectangle):
    assert rectangle.area == 603


def test_length_not_greater_than_zero(rectangle_length_not_greater_than_zero):
    assert rectangle_length_not_greater_than_zero is None


def test_width_not_greater_than_zero(rectangle_width_not_greater_than_zero):
    assert rectangle_width_not_greater_than_zero is None
