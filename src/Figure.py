# Базовый класс фигуры

class Figure:
   
    NAME = None

    area = None

    perimeter = None 

# Функция принимающая другую геометрическую фигуру и возвращает сумму площадей этих фигур.
    def add_area(self, figure):
        if isinstance(figure, Figure) is True: 
            return self.area + figure.area
        else:
            raise ValueError