class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        

    def introduction(self):
        
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am a {self.gender} ")

person1= Human("Alice", 20, "Female")
person1.introduction()
person2= Human("Ali", 15, "Male")
person2.introduction()