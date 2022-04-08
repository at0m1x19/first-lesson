import pytest


def test_add_area_rectangle(triangle, rectangle):
    assert triangle.add_area(rectangle) == triangle.area + rectangle.area


def test_add_area_square(triangle, square):
    assert triangle.add_area(square) == triangle.area + square.area


def test_add_area_circle(triangle, circle):
    assert triangle.add_area(circle) == triangle.area + circle.area


def test_add_area_not_figure(triangle):
    with pytest.raises(ValueError, match='Incorrect class was passed'):
        triangle.add_area('String')


def test_name(triangle):
    assert triangle.name == 'Triangle'


def test_perimeter(triangle):
    assert triangle.perimeter == 45.5


def test_area(triangle):
    assert triangle.area == 65.32535758608597


def test_first_side_less_than_zero(triangle_first_side_less_than_zero):
    assert triangle_first_side_less_than_zero is None


def test_second_side_less_than_zero(triangle_second_side_less_than_zero):
    assert triangle_second_side_less_than_zero is None


def test_third_side_less_than_zero(triangle_third_side_less_than_zero):
    assert triangle_third_side_less_than_zero is None


def test_first_side_too_big(triangle_first_side_too_big):
    assert triangle_first_side_too_big is None


def test_second_side_too_big(triangle_second_side_too_big):
    assert triangle_second_side_too_big is None


def test_third_side_too_big(triangle_third_side_too_big):
    assert triangle_third_side_too_big is None
