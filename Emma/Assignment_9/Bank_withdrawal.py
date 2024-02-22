
# Depositing function
def addx(a,b):
    Answer=int(a)+int(b)
    print("This is your new account balance : ",Answer)
    return

# Withdrawal function
def subx(s,b):
    Answer=int(b)-int(s)
    print("this is your new account balance :",Answer)
    return;


#Account balance
b=10000
print("Your Account balance : ",b)


# bank operation function
def bank_op():
    print("What would you like to do ?")
    print("A : Withdraw")
    print("B : Deposit")
    print("C : Exit")
    option_selected = input("Enter your selected option :")

    if  option_selected == "A" :
        s=input("put in your value to be withdrawn :")
        subx(s,b)
    elif option_selected== "B"  :
        a=input("put in your value to be deposited : ")
        addx(a,b)
    elif option_selected== "C" :
        print("Thank you for using our bank")
    elif option_selected != "A" or "B" or "C" :
        print("invalid option")
    
    return
bank_op()













    


  
   











    


  
   


    
    