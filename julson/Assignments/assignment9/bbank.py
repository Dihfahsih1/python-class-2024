balance = 0

def deposit(amount):
    global balance     #global function can be called from multiple parts of the code
    balance += amount
    print("Deposited ${}. Current balance: ${}".format(amount, balance))

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrew ${}. Current balance: ${}".format(amount, balance))
    else:
        print("Insufficient funds.")

def check_balance():
    print("Current balance: ${}".format(balance))

while True:
    print("\nATM services Available Options:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        check_balance()
    elif choice == 2:
        amount = float(input("Enter deposit amount: $"))
        deposit(amount)
    elif choice == 3:
        amount = float(input("Enter withdrawal amount: $"))
        withdraw(amount)
    elif choice == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")