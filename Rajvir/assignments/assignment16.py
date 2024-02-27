# this is a basic application that uses all 4 elements of class to create a math application...

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass 

class Triangle(Shape):
    def __init__(self,a, b, c):
        self.A= a 
        self.B= b 
        self.C= c 
        
    def calculate_area(self):
        area1=(self.A + self.B + self.C)/2
        return area1

    def calculate_perimeter(self):
        return self.A + self.B + self.C 

class Square(Shape):
    def __init__(self,side__length):
        self.side__length= side__length

    def calculate_area(self):
        return self.side__length**2

    def calculate_perimeter(self):
        return 4*self.side__length

# inorder to attain users input variables are created for the specific input from the sub/child class..
# float will be used because some answers can come as points...

A= float(input("Enter the first length: "))
B= float(input("Enter the second length: "))
C= float(input("Enter the third length: "))
# now the object..
triangle1=Triangle(A,B,C)
#variable..
side__length= float(input("Enter the side length: "))
#object..
square1= Square(side__length)

# printing the objects created..
print(f"The area is.. {triangle1.calculate_area()}")
print(f"The perimeter is.. {triangle1.calculate_perimeter()}")

# squareprinting
print(f"The area is.. {square1.calculate_area()}")
print(f"The perimeter is.. {square1.calculate_perimeter()}")




