# Класс фигуры - треугольник

from Figure import Figure    
    
class Triangle(Figure):

    NAME = 'Triangle'

    def __init__(self, side_1, side_2, side_3):
            self.side_1 = side_1
            self.side_2 = side_2
            self.side_3 = side_3
            if self.side_1 <= 0 or self.side_2 <= 0 or self.side_3 <= 0:
                raise ValueError
            self.area = self.get_area()
            self.perimeter = self.get_perimeter()

# Функция расчета площади треугольника
    def get_area(self):
        p = ((self.side_1+self.side_2+self.side_3)/2)
        return ((p*(p-self.side_1)*(p-self.side_2)*(p-self.side_3))**0.5)

# Функция расчета периметра треугольника
    def get_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3
