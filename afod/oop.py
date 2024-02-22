# create a class named student that will inherit properties and methods from a class named person

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display_name(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(fname, lname):
        super().__init__(fname, lname)

    def display_info(self):
        super().display_info()
        
student1=Person("afod", "mat")
