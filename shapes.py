import math

class Shape:
    '''The area method is empty in the shape class so that it can be overidden'''
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width,length):
        self.width=width
        self.length=length 
        
    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2 *(self.width + self.length)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
        
    def area(self):
        return math.pi *self.radius **2
    
    def perimeter(self):
        return 2*math.pi * self.radius
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)
        
        
if __name__ == "__main__":
    rectangle=Rectangle(5,6)
    print("Rectangle Area: ", rectangle.area() )
    print("Rectangle Perimeter: ", rectangle.perimeter())
    
    circle=Circle(7)
    print("Area of A circle: ", circle.area())
    print("Perimeter of A circle: ", circle.perimeter())
    
    
    square=Square(5)
    print("Area of A square: ", square.area())
    print("Perimeter of A square: ", square.perimeter())
    
    
        