#what is abstraction and encapsulation in object oriented programming and give two examples.
#ABSTRACTION
    #This refers to the process of hiding the implementation details of a class and only showing the essential
# features of the project.
# it focuses on what the project does and not how it does.
# in python the way we achieve abstraction is by inheritence,abstract classes and interfaces
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

# Usage
circle = Circle(5)
rectangle = Rectangle(3, 4)
print(circle.area())      # Output: 78.5
print(rectangle.area())   # Output: 12