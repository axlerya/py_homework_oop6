from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):  # реорганизовали класс, превратив его в абстрактный базовый класс (ABC). OCP принцип
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def print_name(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circule(Figure):

    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)

    def calculate_area(self):
        return f"Площадь: {self.radius ** 2 * pi}"

    def calculate_perimeter(self):
        return f"Периметр {self.radius * 2 * pi}"
    
    def print_name(self):
        return self.name


class Rectangle(Figure):

    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        super().__init__(name)

    def calculate_area(self):
        return f"Площадь: {self.length * self.width}"

    def calculate_perimeter(self):
        return f"Периметр: {(self.length + self.width) * 2}"
    
    def print_name(self):
        return self.name


class Square(Figure):  # переделали класс Square что бы он соответствовал принципу (LSP)
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def calculate_area(self):
        return f"Площадь: {self.side ** 2}"

    def calculate_perimeter(self):
        return f"Периметр: {self.side * 4}"
    
    def print_name(self):
        return self.name


circule = Circule("круг", 5)
print(circule.print_name())
print(circule.calculate_area())
print(circule.calculate_perimeter())
print("-------")
rectangle = Rectangle("прямоугольник", 2, 3)
print(rectangle.print_name())
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
print("-------")
square = Square("квадрат", 2)
print(square.print_name())
print(square.calculate_area())
print(square.calculate_perimeter())
