#Arithmetic operators, used to perform common mathmatical operations..

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("the sum is:", a+b)
print("the difference is ", a-b)
print("the product is ", a*b)
# assignment operators are used to assign values to variables..

x= 7
y= 4
x+=y # x=x+y 
print(x)

# comparison operators 
 
a =14
var2= 16
print (a==var2)

# logical operators

def name():
    name= input("Enter your name: ")
    if(len(name)>=7):
        print("you have an interesting name")
    else:
        print("your name is cool")
name()

#bitwise 
q= 10
g= 8 

print(" q & g = " ,q & g)
print(" q | g = ", q | g )
print(" q ^ g = ", q ^ g)
print(" ~q = ", ~q)

#precedence 
Z= (4+9)/(3+4)
print(Z) 