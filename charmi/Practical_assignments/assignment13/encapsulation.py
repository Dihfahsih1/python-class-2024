#Encapsulation
#Encapsulation helps impelement on private and public variables using either single underscore or double underscore

#Example 1
class Student:

    def __init__(self, name, marks):
        self.__name=name            #this double underscore makes name a private variable
        self.__marks=marks

class Student_profile(Student):

    def Student_data(self):
        print(f"The student name is {self.__name} with {self.__marks} marks")

student1= Student("John", 91)
    

#Example 2 
class Employee:

    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def employee_data(self):
        print("This is the Employee's private data")


class Employee_info(Employee):
    def employee_data(self):
        print("This is the Employee's private data")

employee1= Employee("David", 30)
employee2= Employee("Sarah", 40)

# print(employee1.name)            #this wont print because name and age is private in the employee parent class
# print(employee2.age)


