#  Polymorphism refers to the ability of different classes to be treated as instances of the same class hierachy
class Human:
    def brain(self):
        return "Thinking"
class Cow(Human):
    def brain(self):
        return "Closure"
class Goat(Human):
    def brain(self):
        return "Meow"

# polymorphism example 1

def make_sound(animal):
    return animal.brain()

cow = Cow()
goat = Goat()

print(make_sound(cow))
print(make_sound(goat))


# polymorphism example 2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
p1 = Point(1,2)
p2 = Point(28,12)

result = p1 + p2
print(f"Result: {result.x}, {result.y}")




# Encapsulation: Refers to the bundling of data(attributes) and methds(functions) that operate on the data into a single unit,typically a class

class BankAccount():
    def __init__(self, account_number, balance):
        self._account_number = account_number # encapsulated attribute
        self._balance = balance # encapsulated attribute
        
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds")

balance = int(input("Enter bank balance: "))
account_num = int(input("Enter bank account number: "))
account1 = BankAccount(account_num, balance)

depos = int(input("Enter money to deposit: "))
wid = int(input("Enter money to withdraw: "))
account1.deposit(depos)
account1.withdraw(wid)

print("-----------------------------")