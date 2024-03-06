

def custom_range(start, end, step=1):
    result = []
    while start < end:
        result.append(start)
        start += step
    return result

def main():
    start = int(input("Enter the start value: ")).re
    end = int(input("Enter the end value: "))
    step = int(input("Enter the step value: "))
    
    if step:
        values = custom_range(start, end, step)
    else:
        values = custom_range(start, end)
    
    print("Resulting range:", values)
    
    

if __name__ ==  "__main__":
    main()