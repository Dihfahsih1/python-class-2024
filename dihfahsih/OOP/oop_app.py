import math

# Abstraction: We will define a Shape class as the abstract base class.
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

# Encapsulation: We'll encapsulate the properties and methods of each shape within its respective class.
# Inheritance: Different shapes will inherit from the Shape class and implement their specific functionalities.
# Polymorphism: We will use polymorphism to calculate the area and perimeter of different shapes using the same method names.

# Define a Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Define a Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Define a Square class inheriting from Rectangle
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

# Example usage:
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
