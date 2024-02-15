a= int (input("Enter the first number: "))
b= int (input("Enter the second number: "))

def add(a,b):
    answer= a+b
    print(str(a) + "+" + str (b) + "=" + str(answer))

def sub(a,b):
    answer=a-b
    print(str(a)+ "-" + str (b) + "=" + str(answer))

def mul(a,b):
    answer=a*b
    print(str(a)+ "*" + str (b) + "=" + str(answer))

def div(a,b):
    answer=a/b
    print(str(a)+ "/" + str (b) + "=" + str(answer))

print("select an option: ")
print('A: Addition')
print('B: Subtraction')
print('C: multiplication')
print('D: Division')
choice=input("Enter your choice: ")

if(choice== "a" or choice=="A"):
    Print("The sum is: ")
    add(a,b)

elif(choice== "b" or choice== "B"):
    Print("The difference is: ")
    sub (a,b)

elif(choice== "c" or choice== "C"):
    Print("The product is: ")
    mul(a,b)

elif(choice== "d" or choice=="D"):
    Print("The quotient is: ")
    div(a,b)

else: 
    print("you entered the wrong choice.....", choice)


