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
    def __init__(self,radius):
        super().__init__(radius)

    def area(self):
        return self.radius*self.radius*(4.314)

    def perimeter(self):
        return self.radius* (2*4.314)

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        return self.length* self.length 

    def perimeter(self):
        return (4*self.length)

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length* self.width 

    def perimeter(self):
        return 2*(self.length)+ 2*(self.width)


print("Choose a shape:")
print("A. Circle")
print("B. Square")
print("C. Rectangle")

shape_input= input("Enter your shape: ")

if shape_input =="A" or shape_input== "a":
    radius = float(input("Enter the radius of the circle: "))
    circle1= Circle(radius) 
    print("The area of the circle is: ", circle1.area(radius))
    print("The perimeter of the circle is: ", circle1.perimeter(radius))

elif shape_input =="B" or shape_input== "b":
    length = float(input("Enter the length of the sqaure: "))
    square1= Square(length)
    print("The area of the square is: ", square1.area(length))
    print("The perimeter of the square is: ", sqaure1.perimeter(length))

elif shape_input =="C" or shape_input== "c":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle1= Rectangle(length, width)
    print("The area of the rectangle is: ", rectangle1.area(length, width))
    print("The perimeter of the rectangle is: ", rectangle1.perimeter(length, width))

else: 
    print(f"You entered a wrong choice: {shape_input}")





