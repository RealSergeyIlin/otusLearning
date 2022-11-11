# Класс фигуры - прямоугольник

from Figure import Figure     

class Rectangle(Figure):

    NAME = 'Rectangle'

    def __init__(self, side_1, side_2):
            self.side_1 = side_1
            self.side_2 = side_2   
            self.area = self.get_area()
            self.perimeter = self.get_perimeter()

# Функция расчета площади прямоугольника           
    def get_area(self):
        return self.side_1*self.side_2

# Функция расчета периметра прямоугольника
    def get_perimeter(self):
         return 2*(self.side_1+self.side_2)
