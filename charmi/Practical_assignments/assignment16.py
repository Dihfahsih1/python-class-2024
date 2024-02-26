from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, length, width, radius):
        self.length=length
        self.width=width
        self.radius=radius
 
    @abstractmethod
    def area(self):
        pass
        # print("This is for calculating the area of the shape.")

    @abstractmethod
    def perimeter(self):
        pass
        # print("This is for calculating the perimeter of the shape.")

    def length(self):
        return self.length

    def width(self):
        return self.width

    def radius(self):
        return self.radius

class Circle(Shape):
    def __init__(self,length, width, radius):
        super().__init__(length, width, radius)
        self.length=length
        self.width=width
        self.radius=radius

#this is to calculate the area and perimeter of the circle
    def area(self):
        return self.radius*self.radius*(4.314)

    def perimeter(self):
        return self.radius* (2*4.314)

class Square(Shape):
    def __init__(self, length, width, radius):
        super().__init__(length, width, radius)
        self.length=length
        self.width=width
        self.radius=radius

#this is to calculate the area and perimeter of the square
    def area(self):
        return self.length* self.length 

    def perimeter(self):
        return (4*self.length)

class Rectangle(Shape):
    def __init__(self, length, width, radius):
        super().__init__(length, width, radius)
        self.length=length
        self.width=width
        self.radius=radius

#this is to calculate the area and perimeter of the rectangle
    def area(self):
        return self.length* self.width 

    def perimeter(self):
        return 2*(self.length)+ 2*(self.width)


print("Choose a shape to find the area and perimeter of:")
print("A. Circle")
print("B. Square")
print("C. Rectangle")

shape_input= input("Enter your shape: ")

if shape_input =="A" or shape_input== "a":
    length = 0
    width = 0
    radius = float(input("Enter the radius of the circle: "))
    circle1= Circle(length, width, radius) 
    print("\nThe area of the circle is: ", circle1.area())
    print("The perimeter of the circle is: ", circle1.perimeter())

elif shape_input =="B" or shape_input== "b":
    radius = 0
    width = 0
    length = float(input("Enter the length of the sqaure: "))
    square1= Square(length, width, radius)
    print("\nThe area of the square is: ", square1.area())
    print("The perimeter of the square is: ", square1.perimeter())

elif shape_input =="C" or shape_input== "c":
    radius = 0
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle1= Rectangle(length, width, radius)
    print("\nThe area of the rectangle is: ", rectangle1.area())
    print("The perimeter of the rectangle is: ", rectangle1.perimeter())

else: 
    print(f"\nYou entered a wrong choice: {shape_input}")

print("------------------------------------------")



