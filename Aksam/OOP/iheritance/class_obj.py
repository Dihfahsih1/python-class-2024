class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def display_info(self):
        print(f"First name: {self.fname}, Last name: {self.lname}")
    

class Students(Person):
    def __init__(self, fname, lname, student_id):
        super().__init__(fname, lname)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")


person1 = Person("Aksam", "Cyrus", "7")
person1.display_info()

student1 = Students("Bob", "Marley", "4")
student1.display_info()