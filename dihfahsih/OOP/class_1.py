class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print(f"Hello, my name is {self.name}, I'm {self.age} years old and my gender is {self.gender}.")

# Creating objects    
person1 = Human('Alice', 30, 'Female')
person2 = Human('Ali', 20, 'Male')

person1.introduce()
person2.introduce()

class Man(Human):
    def __init__(self, name, age, gender, college, weight):
        super().__init__(name, age, gender)
        self.college = college
        self.weight = weight

# Creating a Man object
man1 = Man('John', 25, 'Male', 'XYZ College', 75)

# Accessing attributes of the Man object
print(f"{man1.name} attends {man1.college} and weighs {man1.weight} kgs.")
