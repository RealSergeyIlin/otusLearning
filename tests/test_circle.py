# Тесты класса Circle

import os
import sys
import pytest

sys.path.insert(1, os.path.join(sys.path[0], '../src'))
import Circle, Square

from Circle import Circle
from Square import Square

# Исходные данные
circle = Circle(4)
square = Square(10)
not_figure = 20

# Тест на корректность расчета периметра круга
def test_rectangle_perimeter():
    result = circle.perimeter
    expected_result = 25.12
    assert result == expected_result

# Тест на корректность расчета площади круга
def test_rectangle_area():
    result = circle.area
    excepted_result = 50.24
    assert result == excepted_result

# Тест на корректность сложения двух площадей функцией add_area()
def test_rectangle_add_area():
    result = circle.add_area(square)
    expected_result = 150.24
    assert result == expected_result

# Тест на корректность срабатывания ошибки функцией add_area(), если передана не геометрическая фигура
def test_triangle_add_area_error():
   with pytest.raises(ValueError):
    circle.add_area(not_figure)
