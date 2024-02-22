#Abstraction in OOP, focusing on what an object does rather than how it does it.. 
# it provides a high-level view of an objects functionality, making it easier to understaand and use without 
# getting bogged down in internal details.
# this is achieved through the use of abstract classes and interfaces. 

# example 1

from abc import ABC,abstractmethod 

class Shape(ABC):
    def __init__(self,name):
        self.name = name 

    @abstractmethod
    def area(self):
        pass 

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,name,width,height):
        super().__init__(name)
        self.width= width
        self.height = height 

    def area(self):
        return  self.width*self.height

    def perimeter(self):
        return 2* (self.width+self.height)

rectangle=Rectangle("Rectangle",5,4)

print("Area of", rectangle.name,":",rectangle.area())
print("Perimeter of",rectangle.name, ":", rectangle.perimeter())

#ENCAPSULATION
#this is used to restrict access of data members and functions in a class..

class Student:
    def __init__(self,name,age):
        self.__name= name
        self.__age= age 

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_age(self,age):
        return self.__age

    def set_age(self,age):
        if age >= 0:
            self.__age = age
        else: 
            print("age cant be negative man..")

student1 = Student("Alice", 20)
print ("students name" , student1.get_name())