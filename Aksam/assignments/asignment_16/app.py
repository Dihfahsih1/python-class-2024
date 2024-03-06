import math

# We have a `Shape` base class with `area()` and `perimeter()` methods 
class Shape:
    def __init__(self, name):
        self.name = name
        
    def area(self):
        pass
    
    def perimeter(self):
        pass

# Circle has inherited methods from class Shape
# Sub classes below inherite from shape and provide thier implementations for these methods
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        # to show that the area is multiplied by two
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        # to show that the perimeter of a cicle
        return 2 * math.pi * self.radius
    
# eash class encapsulates its data eg width, height, radius etc and methods within
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
# polymorphism is demonstrated by calling the `area()` and `perimeter()`
# methods on objects of different shapes, and each shape provides the appopriate result based on its implementation

class Triangle(Shape):
    def __init__(self, name, side1, side2, side3):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    

# Examples
#  creating objects

if __name__ == "__main__":
    print("--------------------- CIRCLE -------------")
    num_circle = int(input("Please enter a number: "))

    circle = Circle("Circle", num_circle)
    print(circle.name)
    print(f"Area: {circle.area()}")
    print(f"Perimeter: {circle.perimeter()}")
    print("------------------------------------------")
    print()


    print("--------------------- RECTANGLE -------------")
    num_rectangle_1 = int(input("Please enter the first number: "))
    num_rectangle_2 = int(input("Please enter the second number: "))

    rectangle = Rectangle("Rectangle", num_rectangle_1, num_rectangle_2)
    print(rectangle.name)
    print(f"Area: {rectangle.area()}")
    print(f"Perimeter: {rectangle.perimeter()}")
    print("------------------------------------------")
    print()


    print("--------------------- TRIANGLE -------------")
    # num_triangle_1 = int(input("Please enter the first number: "))
    # num_triangle_2 = int(input("Please enter the second number: "))
    # num_triangle_3 = int(input("Please enter the third number: "))

    triangle = Triangle("Triangle", 1, 2, 18)
    print(triangle.name)
    print(f"Area: {triangle.area()}")
    print(f"Perimeter: {triangle.perimeter()}")
    print("------------------------------------------")