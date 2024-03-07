 # Encapsulation refers to the bundling of data and methods that operate on the data into a single unit,typically a class
  # Answer 1
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def getName(self):
        print(f"its name is {self.name}")

    def getAge(self):
        print(f"its age is {self.__age} years")


D = Dog("Spick",2)
D.getName()
D.getAge()


  #Answer 2

class Nuts:
    def __init__(self,name,breed):
        self.name = name
        self.__breed = breed

    def getId(self):
        print(f"its ID is {self.name}")

    def getbreed(self):
        print(f"its breed is {self.__breed} years")


D = Nuts("wallnut","norma")
D.getId()
D.getbreed()


