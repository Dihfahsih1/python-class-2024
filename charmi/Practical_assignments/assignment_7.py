# Banking program

#example 1
print('*'*20)
print("Select an option: ")
print(" A: Withdrawing money.")
print(" B: Depositing money.")
print('*'*20)

action= input("Enter your option: ")
print('*'*20)

if( action=='a' or action=='A'):
    w= int(input("Enter the amount you want to withdraw: "))
    print('*'*20)
    b= int(input("Enter the current amount of bank balance in your account: "))
    print('*'*20)

    def sub(b,w):
        answer=b-w
        print("Your new account balance is: ")
        print(str(b) + '-' + str(w) + '=' + "Shs." + str(answer))
    sub(b,w)

elif( action=='b' or action=='B'):
    d= int(input("Enter the amount you want to deposit: "))
    print('*'*20)
    b= int(input("Enter the current amount of bank balance in your account: "))
    print('*'*20)

    def add(b,d):
        answer=b+d 
        print("Your new account balance is: ")
        print(str(b) + '+' + str(d) + '=' + "Shs." + str(answer))
    add(b,d)

else:
    print("Opps! An ivalid letter was chosen:", action)


#example 2

def deposit_operation(balance, amount):    #this function is to carry deposit operation
    balance += amount
    return balance


def withdraw_operation(balance, amount):   #this function is to carry withdraw operation
    if amount < balance:
        balance -= amount
        return balance
    else:
        print("Insufficient funds to withdraw from!!!")

def bank_operation():
    print("------------------------------")
    print("\nWelcome to CP Bank.")
    print("\n------------------------------")

    acc_no= int(input("Enter your bank account number: "))
    balance = 0
    
    while True:
        print('*'*20)
        print("Select an option: ")
        print(" A: Depositing money.")
        print(" B: Withdrawing money.")
        print('*'*20)

        operation= input("\nEnter your option: ")

        if( operation=='a' or operation=='A'):
            amount = int(input("\nEnter the amount to want to deposit: "))
            balance = deposit_operation(balance, amount)

            print(f"\nThe deposit of Shs. {amount} was successful!")
            print(f"Your current balance in account no. {acc_no} is Shs. {balance}")

        elif( operation=='b' or operation=='B'):
            amount = int(input("Enter the amount to want to withdraw: "))
            balance = withdraw_operation(balance, amount)

            print(f"\nThe withdraw of Shs. {amount} was successful!")
            print(f"Your current balance in account no. {acc_no} is Shs. {balance}")
            break            #break will help exit the while loop once the user has withdrawed from the deposited money

        else:
            print("Invalid choice: ",operation)

bank_operation()




    


