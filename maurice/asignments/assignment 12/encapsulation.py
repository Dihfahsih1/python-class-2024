# Encapsulation refers to creating a shield that that prevents data from being accessed by the code outside the shield
class Student:
    def __init__(self,name,height):
        self.__name=name
        self.__height=height
    def set_height(self,value):
        self.__height=value 
    def get_height(self):
       return self.__height
    def set_name(self,value):
        self.__name=value
    def get_name(self):
        return self.__name
s1=Student("Ben",20)
s2=Student("George",14)
s1.set_height(60)
s1.set_name("Mary")
print(s1.get_height())
print(s1.get_name())

