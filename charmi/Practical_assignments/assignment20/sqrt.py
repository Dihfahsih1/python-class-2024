import math

#using the math module

square_root = lambda x: math.sqrt(x)

x = int(input("Enter the number to find the square root of: "))

print("The square root is: ", square_root(x))      #remember to add the parameter x in ()

#using a formula

sqr_root = lambda num: num**(0.5)

num= int(input("Enter the number to find the square root of: "))

print(f"The asnwer is: {sqr_root(num)}")