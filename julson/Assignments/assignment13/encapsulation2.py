class Person:
    def __init__(self, name):
        self.__name = name   # Private variable
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

person = Person("Alice")
print(person.name)    # Output: Alice
person.name = "Bob"
print(person.name)    # Output: Bob