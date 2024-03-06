import math

class Shape:
    ''' The area method is empty in the shape class so that it can be
    def area(self);
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def_init_(self, width,length):
        self.width=width
        self.length=length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 *(self.width + self.length)

class Circle(Shape)
    def_init_(self, radius):
        self.radius=radius

    def area(self): I
        return math.pi *self.radius **2

    def perimeter(self):
        return 2*math.pi * self.radius

class Square(Rectangle):
    def_init_(self, side):
        super()._init_(side,side)



if _name_ == " main ":
    rectangle=Rectangle(5,6)
    print("Rectangle Area:", rectangle.area() )
    print("Rectangle Perimeter: ", rectangle.perimeter())

    circle=Circle(7)
    print(Area of A circle: ", circle.area())
    print("Perimeter of A circle ", circle.perimeter())


    square=Square(5)
    print("Area of A square: ", square.area())
    print("Perimeter of A square: ", square.perimeter())