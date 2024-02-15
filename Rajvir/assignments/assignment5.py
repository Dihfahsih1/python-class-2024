#if and else to create a bank operation...

name = input("enter your name:")
print(name)

balance = float(input("Enter your balance"))
print("your balance is: " , balance)

transaction = input("enter w for withdraw or d for deposit")
print (transaction)
if(transaction == "d" or transaction == "D"):
    amount = int(input("Enter deposit amount"))
    if(amount< 0):
        print("amount cannot be negative")
    else:
        new_balance = balance + amount
        print("your new balance is: ", new_balance)
else:
    (transaction == "w" or transaction == "W")
    amount= int(input("enter your withdraw amount"))
    if(amount > balance):
        print("insuffiient funds")
    else:
        new_balance = balance- amount
    print("your new balance is:", new_balance)