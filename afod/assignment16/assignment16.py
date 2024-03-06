#create a simple application for managing shapes. use the concepts of abstraction, inheritence, encapsulation and polymorhism
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def display_radius(self):
        print(f"{self.radius}")

    def area(self):
        area = 3.142 * (self.radius**2)
        print(area)

    def circumference(self):
        circumference = 3.142(self.radius*2)
        print(circumference)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        area = self.side**2
        print(area)

    def perimeter(self):
        perimeter = self.side*4
        print(perimeter)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(area)

    def perimeter(self):
        perimeter = (self.length*2) + (self.width*2)
        print(perimeter)

class Sphere(Circle, Shape):
    def __init__(self, radius):
        super().__init__(radius)

    def area(self):
        area = 4*3.132*(self.radius**2)
        print(area)

class Trapezium(Shape):
    def __init__(self, a, b, height):
        self.__a= a
        self.__b = b
        self.__height=height

    #getter
    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_height(self):
        return self.__height

        #setter
    def set_a(self, a):
        self.__a = a 

    def set_b(self, b):
        self.__b = b

    def set_height(self, height):
        self.__height = height

    def area(self):
        area = 0.5*(self.__a + self.__b)*self.__height
        print(f"a = {self.__a}, b = {self.__b}, height = {self.__height}")
        print(area)



