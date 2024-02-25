def switch_case(argument):
    print(f"You selected option: {argument}")
    if argument=='a':
        
        return "Apple"
    
    elif argument=='b':
        return "Bananas"
    
    elif argument=='c':
        return "Cherry"
    
    elif argument=='d':
        return "dates"
    
    else:
        print("Invalid choice!")
        
input=input("Enter the option: ")      
print(switch_case(input))
    