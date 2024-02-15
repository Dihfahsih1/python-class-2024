def switch_cases(argument):
    if argument== "a":
        print("you selected option:{argument}")
        return "Apple" # return only returns a value but does not print

    elif argument== "b":
        return "Banana"

    elif argument== "b":
        return "Banana"

    elif argument== "b":
        return "Banana"
    
    else:
        print("Invalid choice")

input = input("enter the option:")
print(switch_cases(input))