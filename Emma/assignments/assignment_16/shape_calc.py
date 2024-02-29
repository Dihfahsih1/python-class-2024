
import time
 # Area classes
class Area_square():
    def __init__(self,length):
        self.length=length
        
        
    def calculate_Area(self):
        Answer = self.length **2
        print(" ____________")
        print("|            |")
        print("|            |", self.length,units)
        print("|            |")
        print(" ------------")
        print("your square's area is ", Answer ,units)

class Area_rectangle(Area_square):
    def __init__(self,length,width):
        super().__init__(length)
        self.width=width

    def calculate_Area(self):
        Answer= self.length*self.width
        print(" -------------")
        print("|             |" ,self.length,units)
        print("|             |")
        print(" -------------")
        print( self.width,units)

        print("Your area of rectangle : " , Answer ,units)

class Area_triangle(Area_rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
        
    def calculate_Area(self):
    
        Answer = 1/2 * self.length*self.width
        print("     /\    ")
        print("    /  \  ")
        print("   /    \ " "height : ",self.width,units)
        print("  /      \ ")
        print("  -------- ")
        print("base : ",self.length,units)
        print("Area of triangle : ",Answer ,units)
class Area_circle(Area_square):
    def __init__(self, length):
        super().__init__(length)

    def calculate_Area(self):
        Answer = 3.14 * self.length**2
        print("   ---   ")
        print(" /     \ ")
        print("|----   |" ,"radius : ", self.length,units)
        print(" \     / ")
        print("   --- ")
        print("Area of your circle : ", Answer ,units)



  # perimeter classes
class perimeter_square:
    def __init__(self,length):
        self.length=length
    
    def calculate_perimeter(self):
        Answer = 4*self.length
        print(" ____________")
        print("|            |")
        print("|            |", self.length,units)
        print("|            |")
        print(" ------------")
        print("Your square's perimeter : " ,Answer ,units)

class perimeter_rectangle(perimeter_square):
    def __init__(self,length,width):
        super().__init__(length)
        self.width = width
    
    def calculate_perimeter(self):
        Answer = 2*(self.length+self.width)
        print(" -------------")
        print("|             |" ,self.length,units)
        print("|             |")
        print(" -------------")
        print( self.width,units)
        print("Your rectangle's perimeter : ", Answer ,units)

class perimeter_triangle(perimeter_rectangle):
    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height=height

    def calculate_perimeter(self):
        Answer = self.length + self.width + self.height
        print("     /\    ")
        print("    /  \  ")
        print("   /    \ " "height : ",self.width,units)
        print("  /      \ ")
        print("  -------- ")
        print("width : ",self.length,units)
        print("length : ",self.length,units)
        print("Your triangle's perimeter : ", Answer ,units)


class perimeter_circle(perimeter_square):
    def __init__(self, length):
        super().__init__(length)

    def calculate_perimeter(self):
        Answer = 2*3.14*self.length
        print("   ---")
        print(" /     \ ")
        print("|----   |" ,"radius : ", self.length,units)
        print(" \     /")
        print("   --- ")
        print("Your perimeter of a circle : ",Answer ,units)

print("..........................................")
units = input("what units are you using ? \n: ")

print("What operation would you like to do ?")

print("1. Area of a square     5. perimeter of a Square \n2. Area of a rectangle  6. perimeter of a rectangle \n3. Area of a triangle   7. perimeter of a triangle \n4. Area of a circle     8. perimeter of a circle")

    # input option to activate the if statements
Input1 = input("Put in your option \n :")

if Input1 == "1":
    S = Area_square(int(input("put in your value : ")))
    S.calculate_Area()

elif Input1 == "2":
    R = Area_rectangle(int(input("Put in your length : ")),int(input("Put in your width : ")))
    R.calculate_Area()
elif Input1 == "3":
    T = Area_triangle(int(input("Put in your Base : ")),int(input("Put in your height : ")))
    T.calculate_Area()
elif Input1 == "4":
    C = Area_circle(int(input("Put in your radius : ")))
    C.calculate_Area()
elif Input1 == "5":
    PS = perimeter_square(int(input("Put in your length : ")))
    PS.calculate_perimeter()
elif Input1 == "6":
    PR = perimeter_rectangle(int(input("Put in your length : ")),int(input("Put in your width : ")))
    PR.calculate_perimeter()
elif Input1 == "7":
    PT = perimeter_triangle(int(input("Put in your length : ")),int(input("Put in your width : ")),int(input("Put in your height")))
    PT.calculate_perimeter()
elif Input1 == "8":
    PC = perimeter_circle(int(input("Put in your radius : ")))
    PC.calculate_perimeter()

else:
    print("This option is not there ")



    