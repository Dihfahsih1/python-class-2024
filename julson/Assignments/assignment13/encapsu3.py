class BankAccount:
    def __init__(self):
        self.__balance = 0   # Private variable
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
print(account.get_balance())  # Output: 100
account.withdraw(50)
print(account.get_balance())  # Output: 50