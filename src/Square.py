# Класс фигуры - квадрат

from Figure import Figure     

class Square(Figure):

    NAME = 'Square'

    def __init__(self, side_1):
            self.side_1 = side_1
            self.area = self.get_area()
            self.perimeter = self.get_perimeter()

# Функция расчета площади квадрата            
    def get_area(self):
        return self.side_1*self.side_1

# Функция расчета периметра квадрата
    def get_perimeter(self):
        return 2*(self.side_1+self.side_1)
