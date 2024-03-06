def max_min():

    comparision = lambda num1,num2: num1 < num2
    
    num1= int(input("Enter first number: "))
    num2= int(input("Enter second number: "))

    print(comparision(num1,num2))

    if comparision(num1,num2) == True:
        print("Second number is greater than First number")

    else:
        print("First number is greater than Second number")


    maxmin = lambda x,y,z: max(x,y,z)

    x = int(input("Enter the number 1: "))
    y = int(input("Enter the number 2: "))
    z = int(input("Enter the number 3: "))

    print(maxmin(x,y,z))

max_min()