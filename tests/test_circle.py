import pytest


def test_add_area_triangle(circle, triangle):
    assert circle.add_area(triangle) == circle.area + triangle.area


def test_add_area_rectangle(circle, rectangle):
    assert circle.add_area(rectangle) == circle.area + rectangle.area


def test_add_area_square(circle, square):
    assert circle.add_area(square) == circle.area + square.area


def test_add_area_not_figure(circle):
    with pytest.raises(ValueError, match='Incorrect class was passed'):
        circle.add_area('String')


def test_name(circle):
    assert circle.name == 'Circle'


def test_perimeter(circle):
    assert circle.perimeter == 72.25663103256524


def test_area(circle):
    assert circle.area == 415.4756284372501


def test_radius_not_greater_than_zero(circle_radius_not_greater_than_zero):
    assert circle_radius_not_greater_than_zero is None
