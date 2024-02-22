class Person:
  def __init__(self, name,age):
    self.Name=name 
    self.Age=age
class Student(Person):
    def __init__(self):
      print(f'name: {self.Name},"age: {self.Age}')
object=Student("Maurice",20)

