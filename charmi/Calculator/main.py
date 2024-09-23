a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("*"*20)

def add(a,b):
    answer=a+b
    print(str(a) + "+" + str(b) + "=" + str(answer))     #only strings can be concatenated

def sub(a,b):
    answer=a-b
    print(str(a) + "-" + str(b)  + "=" + str(answer))
    
def mul(a,b):
    answer=a*b
    print(str(a) + "*" + str(b) + "=" + str(answer))

def div(a,b):
    answer=a/b
    print(str(a) + "/" + str(b) + "=" + "{:.2f}".format(answer)) # printing the answer to 2 decimal places
    
print("Select an option: ")
print('A: Addtion')
print('B: Subtraction')
print('C: Multipication')
print('D: Division')
choice=input("Enter your option:")
print("*"*20)

if(choice=='a' or choice=='A'):
    print("the sum is: ")
    add(a,b)
    

elif(choice=='b' or choice=='B'):
    print("the difference is: ")
    sub(a,b) 
    

elif(choice=='c' or choice=='C'):
    print("the product is: ") 
    mul(a,b)
    

elif(choice=='d' or choice=='D'):
    print("the quotient is: ")
    div(a,b)
    

else:
    print("You entered a wrong choice...........", choice)

