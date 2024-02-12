a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))


def add(a,b):
    answer=a+b 
    print(str(a) + "+" + str(b) + "=" + str(answer))
    
def sub(a,b):
    answer=a-b 
    print(str(a) + "-" + str(b) + "=" + str(answer))
    
def div(a,b):
    answer=a/b 
    print(str(a) + "/" + str(b) + "=" + str(answer))
    
def mul(a,b):
    answer=a*b 
    print(str(a) + "*" + str(b) + "=" + str(answer))

print("Choose one of the following operations")
print("A. Addition") 
print("B. Subtraction") 
print("C, Multiplication") 
print("D, Division)") 


choice=input("input your choice: ")

if choice == 'a' or choice=="A":
    print("Addition")
    add(a,b)
    
elif choice == 'b' or choice=="B":
    print("Subtraction")
    sub(a,b)
    
elif choice == 'c' or choice=="C":
    print("Multiplication")
    mul(a,b)
    
elif choice == 'd' or choice=="D":
    print("Your Choice is Division")
    div(a,b)
    
else:
    print("Com'on you entered a wrong choice: ", choice)
    
 