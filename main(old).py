class Figure:

    def __init__(self, name):  
        self.name = name

    def print_name(self):
        return print(self.name)


class Circule(Figure):

    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)

    def calculate_area(self):
        return print(f"Площадь: {self.radius ** 2 * 3.14}")

    def calculate_perimeter(self):
        return print(f"Периметр {self.radius * 2 * 3.14}")


class Rectangle(Figure):

    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        super().__init__(name)

    def calculate_area(self):
        return print(f"Площадь: {self.length * self.width}")

    def calculate_perimeter(self):
        return print(f"Периметр: {(self.length + self.width) * 2}")


class Square(Rectangle):
    def __init__(self, name, length):
        super().__init__(name, length, length)


 
circule = Circule("круг", 5)
circule.print_name()
circule.calculate_area()
circule.calculate_perimeter()
print("-------")
rectangle = Rectangle("прямоугольник", 2, 3)
rectangle.print_name()
rectangle.calculate_area()
rectangle.calculate_perimeter()
print("-------")
square = Square("квадрат", 2)
square.print_name()
square.calculate_area()
square.calculate_perimeter()


