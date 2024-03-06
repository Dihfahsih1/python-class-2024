#an abstract function is a function that is declared in an abstract class but does not contain an implementation.

# Abstract functions within abstract classes act as placeholders that must be implemented by subclasses

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(5)
print("Circle area:", circle.area())

rectangle = Rectangle(3, 4)
print("Rectangle area:", rectangle.area())