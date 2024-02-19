from abc import ABC , abstractmethod

class Human:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
    def speak(self):
        print(f"{self.name} said we should go")
    @abstractmethod
    def Gender(self):
        print(f"I am a {self.gender}")
    
    def Name(self):
        print(f"My name is {self.name}")

class Person1(Human):
    def Genderx(self):
        super().Gender()

P1 = Person1("Chris","M",20)
P1.Genderx()


        