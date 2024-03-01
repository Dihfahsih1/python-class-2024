import math

num = int(input("Enter the number: "))
number = lambda x: math.sqrt(num)
print(f"The square root of {num} is {number(num)}")