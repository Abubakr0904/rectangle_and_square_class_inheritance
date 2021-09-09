# class MyClass():
#     def __init__(self, name = 'undefined', color = 'black'):
#         self.name = name
#         self.color = color
# undefinedCar = MyClass()
# bmw = MyClass("BMW", "White")
# print(undefinedCar.name)
# print(bmw.name)


class Rectangle:
    def __init__(self, length: int, breadth: int):
        self.length = length
        self.breadth = breadth
    def print_area(self):
        print(self.length * self.breadth)

    def print_perimeter(self):
        print("Perimeter: %d" % (self.length * 2 + self.breadth * 2))

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(length = side, breadth = side)

square = Square(4)
rectangle = Rectangle(2, 5)
rectangle.print_area()
square.print_area()
square.print_perimeter()
rectangle.print_perimeter()