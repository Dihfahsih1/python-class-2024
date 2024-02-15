class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def stud_name(self):
        print(f"My name is {self.name}")

    def stud_age(self):
        print(f"my age is {self.age}")

class student(person):
    def __init__(self,name,age):
        super().__init__(name,age)

Jam = student("Greg",19)

Jam.stud_name()
Jam.stud_age()
