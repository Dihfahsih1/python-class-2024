from abc import ABC, abstractmethod



class Shape(ABC):
    @abstractmethod
    def shape_area(self):
        pass
    
    @abstractmethod
    def shape_perimeter(self):
        pass
    
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def shape_area(self):
        return self.width * self.height
    
    def shape_perimeter(self):
        return 2 * (self.width + self.height)
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def shape_area(self):
        return 3.14 * self.radius
    
    def shape_perimeter(self):
        return 2 * 3.14 * self.radius
    
my_rectangle = Rectangle(10, 4)
my_circle = Circle(3)


print(f"Area of a rectangle is: {my_rectangle.shape_area()}cm")
print(f"Perimeter of a rectangle is: {my_rectangle.shape_perimeter()}cm")



print("Area of a circle", my_circle.shape_area())
print("Perimeter of a circle", my_circle.shape_perimeter())