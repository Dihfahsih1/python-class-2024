def add(num1,num2):
    return (num1+num2)

def get_input():
    number1=int(input("Enter first value: "))
    number2=int(input("Enter second value: " ))
    result=add(number1,number2)
    print("The summed value is: ", result)
get_input()

