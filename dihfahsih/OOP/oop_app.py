import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
if __name__ == "__main__":
    rectangle = Rectangle(5, 4)
    print("Rectangle Area:", rectangle.area())
    print("Rectangle Perimeter:", rectangle.perimeter())

    circle = Circle(7)
    print("Circle Area:", circle.area())
    print("Circle Perimeter:", circle.perimeter())

    square = Square(5)
    print("Square Area:", square.area())
    print("Square Perimeter:", square.perimeter())
