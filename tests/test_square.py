# Тесты класса Square

import os
import sys
import pytest

sys.path.insert(1, os.path.join(sys.path[0], '../src'))
import Triangle, Square

from Triangle import Triangle
from Square import Square

# Исходные данные
square = Square(10)
triangle = Triangle(13, 14, 15)
not_figure = 10

# Тест на корректность расчета периметра квадрата
def test_square_perimeter():
    result = square.perimeter
    expected_result = 40
    assert result == expected_result

# Тест на корректность расчета площади квадрата
def test_square_area():
    result = square.area
    excepted_result = 100
    assert result == excepted_result

# Тест на корректность сложения двух площадей функцией add_area()
def test_square_add_area():
    result = square.add_area(triangle)
    expected_result = 184
    assert result == expected_result

# Тест на корректность срабатывания ошибки функцией add_area(), если передана не геометрическая фигура
def test_triangle_add_area_error():
   with pytest.raises(ValueError):
    square.add_area(not_figure)
