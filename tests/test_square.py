import pytest


def test_add_area_triangle(square, triangle):
    assert square.add_area(triangle) == square.area + triangle.area


def test_add_area_rectangle(square, rectangle):
    assert square.add_area(rectangle) == square.area + rectangle.area


def test_add_area_circle(square, circle):
    assert square.add_area(circle) == square.area + circle.area


def test_add_area_not_figure(square):
    with pytest.raises(ValueError, match='Incorrect class was passed'):
        square.add_area('String')


def test_name(square):
    assert square.name == 'Square'


def test_perimeter(square):
    assert square.perimeter == 85.6


def test_area(square):
    assert square.area == 457.9599999999999


def test_side_not_greater_than_zero(square_side_not_greater_than_zero):
    assert square_side_not_greater_than_zero is None
