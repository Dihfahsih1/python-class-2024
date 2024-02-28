def reverse_str(string):
    return string[::-1]

def lower_str(string):
    return string.lower()

def upper_str(string):
    return string.upper()

def strip_str(string):
    return string.strip()

def count_str(string):
    return len(string)

def main():
    input_str = input("Enter a string: ")
    
    reverse_string = reverse_str(input_str)
    print(f"Reversed string: {reverse_string }")
    
    lowercase = lower_str(input_str)
    print(f"Lowercase string: {lowercase }")
    
    uppercase = upper_str(input_str)
    print(f"Uppercase string: {uppercase }")
    
    strip_string = strip_str(input_str)
    print(f"Stripped string: {strip_string }")
    
    string_len = count_str(input_str)
    print(f"Counted string: {string_len }")
    

main()
    
    
    
    