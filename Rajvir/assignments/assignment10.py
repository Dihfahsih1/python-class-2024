#object oriented programming..
class Car:
    def __init__(self,make,model,year,color):
        self.make= make
        self.model= model
        self.year= year
        self.color= color
    
    def drive(self):
        print("this car is driving")

    def stop(self):
        print("this car has stoped")
    
    def printyr(self):
        print(self.make,self.model,self.year,self.color)

car_1= Car("chevy","corvette",2011,"blue")
car_1.drive( )

x =Car( "charm","RAJ.123",2011, "blue") #parent class used..
x.printyr()




