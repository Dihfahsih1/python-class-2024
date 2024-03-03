def temperature():

    temp_celsius = lambda f : (f-32)*(5/9)

    f = int(input("Enter the temperature in Fahrenheit: "))

    print("The temperature in Celsius is: ", temp_celsius(f))

temperature()