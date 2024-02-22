
# Abstraction: refers to the process of hiding complex implementation details and showing only the essential features of an object

from abc import ABC, abstractmethod

class Shape(ABC):
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

rectangle = Rectangle(5,4)
circle = Circle(3)

print("Area of a rectangle", rectangle.area())
print("Area of a circle", circle.area())
        
        
        


