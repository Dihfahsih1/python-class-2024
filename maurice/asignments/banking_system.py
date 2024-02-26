
balance=0
def deposit(amount):
    global balance
    balance += amount
    print("Deposit ${}.Current balance: ${}".format(amount, balance))
def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("withdraw ${}.Current balance: ${}".format(amount,balance))
    else:
        print("Insufficient funds.")
def check_balance():
    print("Curent balance: ${}".format(balance))
while True:
    print("\nATM services available options:")
    print("1. Check Balance: ")
    print("2. Deposit ")
    print("3.Withdraw ")
    print("4. Exit program.")
    choice=int(input("Enter choice: "))
    if choice==1:
     check_balance()
    elif choice==2:
      amount = float(input("Enter deposit amount: $"))
      deposit(amount)
    elif choice == 3:
       amount=float(input("Enter withdrawal amount: $"))
       withdraw(amount) 
    elif choice == 4:
      print("Exit program.")
      break  
    else:
       print("Invalid choice.Please try again.")  
