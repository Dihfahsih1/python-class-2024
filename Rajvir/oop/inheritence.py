class Person:
    def __init__(self,name,age):
     self.name= name
     self.age = age
 
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name,age)
        self.middlename =name
  
    def cook(self):
        print(f"{self.middlename} cooking!!")


kid1 =Student("Raj", 19)
print(kid1.cook())