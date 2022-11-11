# Тесты класса Triangle

import os
import sys
import pytest

sys.path.insert(1, os.path.join(sys.path[0], '../src'))
import Triangle, Square

from Triangle import Triangle
from Square import Square

# Исходные данные
triangle = Triangle(13, 14, 15)
square = Square(10)
not_figure = 5

# Тест на корректность срабатывания ошибки при создании фигуры треугольника с одной из сторон равной 0
def test_create_triangle_error():
    with pytest.raises(ValueError):
        Triangle(13, 14, 0)

# Тест на корректность расчета периметра треугольника
def test_triangle_perimeter():
    result = triangle.perimeter
    expected_result = 42
    assert result == expected_result

# Тест на корректность расчета площади треугольника
def test_triangle_area():
    result = triangle.area
    excepted_result = 84
    assert result == excepted_result

# Тест на корректность сложения двух площадей функцией add_area()
def test_triangle_add_area():
    result = triangle.add_area(square)
    expected_result = 184
    assert result == expected_result

# Тест на корректность срабатывания ошибки функцией add_area(), если передана не геометрическая фигура
def test_triangle_add_area_error():
   with pytest.raises(ValueError):
    triangle.add_area(not_figure)
