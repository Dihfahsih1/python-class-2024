# class BankAccount:
#     def __init__(self,account_no,owner,balance):
#         self.account_no = account_no
#         self.owner = owner
#         self.__balance = balance
    
#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount
#     def withdraw(self,amount):
#         if 0<amount<= self.__balance:
#             self.__balance -= amount
#     def get_balance(self):
#         return self.__balance
    
# class SavingAccount(BankAccount):
#     def __init__(self, account_no, owner, balance, interest_rate = 0.1):
#         super().__init__(account_no, owner, balance)
#         self.__interest_rate = interest_rate

#     def add_interest(self):
#         interest = self.get_balance() * self.__interest_rate
#         self.deposit(interest)

#     def get_balance(self):
#         balance = super().get_balance()
#         interest = balance*self.__interest_rate
#         return balance + interest
# # john_account = BankAccount(10010, "John", 9000)
# # print(john_account.owner)
# # print(john_account.__balance)

# savings_account = SavingAccount(10011, "Alice", 9000)
# savings_account.deposit(1000)
# print(savings_account.get_balance())
# savings_account.withdraw(200)
# print(savings_account.get_balance())
# savings_account.add_interest()
# print(savings_account.get_balance())






PENNIES_PER_DOLLAR = 100
PENNIES_PER_QUARTER = 25

userInput = input("Enter bill value: ")
billValue = int(userInput)
userInput = input("Enter item price in pennies: ")
itemPrice = int(userInput)

changeDue = PENNIES_PER_DOLLAR * billValue - itemPrice
dollarCoins = changeDue // PENNIES_PER_DOLLAR
changeDue = changeDue %PENNIES_PER_DOLLAR
quarters = changeDue // PENNIES_PER_QUARTER

print(f"Dollar coins: {dollarCoins}")
print(f"Quarters : {quarters}")