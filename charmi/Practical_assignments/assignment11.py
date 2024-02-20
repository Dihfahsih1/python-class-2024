#Polymorphism

# 'Example one'

class Vehical:
    def __init__(self, model, year):
        self.model=model
        self.year=year

    def move(self):
        print("The vehical is moving!")

class Bus(Vehical):
    def move(self):
        print("Driving!")

class Bike(Vehical):
    def move(self):
        print("Peddle!")

bus1=Bus("MiniBus", 2019) 
bike1=Bike("E-bike", 2020)
print("The bus model is: ", bus1.model)
print("The bike model is: ", bike1.model)

print("*"*20)

#Example 2

class Exams:
    def __init__(self,subject,topic):
        self.subject=subject
        self.topic=topic

    def study(self):
        print("Revision is going on!")

class Sem_1(Exams):
    def study(self):
        print("Semester one revision is going on.")

class Sem_2(Exams):
    def study(self):
        print("Semester two revision is going on.")

exam1=Sem_1("Mathematics", "Calculus")
exam2=Sem_2("Physics", "Waves")

print(exam1.subject)
print(exam1.topic)
print(exam2.subject)
print(exam2.topic)



