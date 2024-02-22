# Banking program


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
    


