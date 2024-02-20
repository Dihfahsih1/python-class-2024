class BankAccount:
    def init (self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}.")
        else:
            print("Insufficient funds or invalid withdrawl amount.")

    def get_balance(self):
        print(f"Balance of account {self.account_number}: {self.balance}")
        return

    balance = 1000

    # Withdrawl operation
    amount_ to _withdraw = float(input("Enter the amount to withdrew: "))
    if amount_ to_withdraw > 0:
        if amount_to_withdraw <= balance:
            balance -= amount_to_withdraw
            print("Withdrawl successful.")
            print("Remaining balance:", balance)
        else:
            print("Insufficient funds.")
    else:
        print("Invalid amount.")