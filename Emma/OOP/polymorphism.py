# Polymorphism refers to the occurance of where a variable , function or any data type is  in multiple forms
#Using Polymorphism`:`
class Mul:
    def __init__(self,name,age):
        self.name = name
        self.age = age
       
    def mul(self,n1,n2):
        n1 = self.name
        n2 = self.age
        A = int(n1*n2)
        print("Answer in int : " , A)
    def mul(self,num1,num2):
        num1 = self.name
        num2= self.age
        A2 = str(num1+num2)
        print("answer in str : " ,A2)

g = Mul(9,6)
g.mul()
