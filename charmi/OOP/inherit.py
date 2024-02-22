class Person:
    def __init__(self, fname, lname):
        self.firstname= fname
        self.lastname= lname

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.firstname=fname
        self.lastname=lname

    def study(self):
        print("Studying")
    
student1= Student("Charmi", "Panchal")
print(f"The student name is {student1.firstname} {student1.lastname}")
student1.study()