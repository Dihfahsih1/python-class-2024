# logical operations
age= input("Enter your age:")
age= int(age)           #this is neccesary beacuse operators >= only support integars
if (age >= 20):
    print("You are an adult")
else:
    print("You are still young", "\n")
print('*'*20)

#comparison operations
set1= ['John', 'Mary', 'Sarah']
set2= ['John', 'Sarah', 'Mark']
print(set1==set2, "\n")

def interest():
    p= input("Enter the priciple amount: ")
    p= int(p)
    r= input("Enter the rate: ")
    r= int(r)
    t= input("Enter the number of years:")
    t= int(t)

    interest1= (p*r*t)/100
    print("The total interest is: ",interest1)

    if (interest1 >100000):
        print("You have earned a large amount")
    else:
        print("You have earned little interest", "\n")
interest() 
print('*'*20)

#assignment operators

a= input("Enter any number: ")
b= input("Enter the exponent value:")

a=int(a)
b=int(b)

a**=b
print("The answer for 'a' is: ", a)
print('*'*20)

#precedence operators

a=6
b=19
c=20
d=21
e=10

f= a+b * c/d 
print("The value of a+b * c/d is:", f)

g= (a+b) * (c/d)
print("The value of (a+b) * (c/d) is:", g)

h= ((a+b)*c) /d 
print("The value of ((a+b)*c) /d is:", h)

i= a + (b*c)/d 
print("The value of a + (b*c)/d is:", i)



