from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return f"Withdrawing {amount}. New balance: {self.balance}"
        else:
            return "Insufficient funds."

# Example usage
savings_account = SavingsAccount(100)
print(savings_account.withdraw(50))