# Класс фигуры - круг

from Figure import Figure     

class Circle(Figure):

    NAME = 'Circle'

    def __init__(self, radius):
            self.radius = radius
            self.area = self.get_area()
            self.perimeter = self.get_perimeter()

# Функция расчета площади круга            
    def get_area(self):
        return 3.14*(self.radius**2)

# Функция расчета периметра круга
    def get_perimeter(self):
         return 2*3.14*self.radius
