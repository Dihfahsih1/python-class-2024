class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

def make_sound(animal):
    return animal.sound()

dog = Dog()
cat = Cat()

print(make_sound(dog))  # Output: Woof!
print(make_sound(cat))  # Output: Meow!