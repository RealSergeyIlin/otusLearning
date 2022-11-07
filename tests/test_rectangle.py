# Тесты класса Rectangle

import os
import sys
import pytest

sys.path.insert(1, os.path.join(sys.path[0], '../src'))
import Rectangle, Square

from Rectangle import Rectangle
from Square import Square

# Исходные данные
rectangle = Rectangle(10, 15)
square = Square(10)
not_figure = 15

# Тест на корректность расчета периметра прямоугольника
def test_rectangle_perimeter():
    result = rectangle.perimeter
    expected_result = 50
    assert result == expected_result

# Тест на корректность расчета площади прямоугольника
def test_rectangle_area():
    result = rectangle.area
    excepted_result = 150
    assert result == excepted_result

# Тест на корректность сложения двух площадей функцией add_area()
def test_rectangle_add_area():
    result = rectangle.add_area(square)
    expected_result = 250
    assert result == expected_result

# Тест на корректность срабатывания ошибки функцией add_area(), если передана не геометрическая фигура
def test_triangle_add_area_error():
   with pytest.raises(ValueError):
    rectangle.add_area(not_figure)
