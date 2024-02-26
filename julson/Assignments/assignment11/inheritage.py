class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass  # Placeholder method to be overridden by subclasses

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")  # Call superclass constructor
        self.breed = breed

    def make_sound(self):
        return "Woof!"  # Implement method specific to Dog subclass
    
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)  # Output: Buddy
print(my_dog.species)  # Output: Dog
print(my_dog.breed)  # Output: Golden Retriever
print(my_dog.make_sound())  # Output: Woof!