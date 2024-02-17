class Human:
    def __init__(self, name, age, gender):
        self.age=age
        self.name=name 
        self.gender=gender
        
    def introduce(self):
        print(f"Hello, my name is {self.name}, i'm {self.age} years old and my gender is {self.gender} ")
#creating objects    
person1 = Human('Alice', 30, 'Female')
person2 = Human('Ali', 20, 'Male')

person1.introduce()
person2.introduce()

class Man(Human):
    def __init__(self, college, weight):
        super().__init__(self)
        self.age=age

    