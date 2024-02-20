#Subtraction
def sub(num1, num2):
    return (num1-num2)


number1= input("Enter first value:")
number2= input("Enter second value:")
print ("The subtracted value is:", sub(int(number1),int(number2)), "\n")

#Multiplication
def mult(num1, num2):
    return (num1*num2)


number1= input("Enter first value:")
number2= input("Enter second value:")
print ("The product of the values is:", mult(int(number1),int(number2)), "\n")

#Division
def div(num1, num2):
    return (num1/num2)


number1= input("Enter the any value to be divided:")
number2= input("Enter the divisor value:")
print ("The answer is:", div(int(number1),int(number2)), "\n")

#Power of a number
def pwr(num1, num2):
    return (num1**num2)


number1= input("Enter any value:")
number2= input("Enter the power:")
print ("The answer is:", pwr(int(number1),int(number2)), "\n")



