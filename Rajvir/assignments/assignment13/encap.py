#ENCAPSULATION
#this is used to restrict access of data members and functions in a class..

class Parent:
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

class Child(Parent):
    def __init__(self,name,age,mname):
        super().__init__(name,age)
        self.mname = mname

parent1 =Parent("Alice", 20)
print ("parents name is " , Parent.get_name())

child1 =Child("John", 20, "jack")
print ("childs name is " , Child.get_name())