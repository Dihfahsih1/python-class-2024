def switch_cases(argument):
    if argument== "a":
        print(f"You selected option: {argument}")
        return "Apple"      # return only returns a value but it does not print

    elif argument== "b":
        return "Banana"

    elif argument== "c":
        return "Cherry"

    elif argument== "d":
        return "Dates"

    else:
        print("Invalid choice")

input= input("Enter the option:")
print(switch_cases(input))