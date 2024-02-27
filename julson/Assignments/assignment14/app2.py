
phone_input = []

# Taking input from three variables
input_var1 = input("Enter first Phone: ")
input_var2 = input("Enter second Phone: ")
input_var3 = input("Enter third Phone: ")

# Adding inputs to the list
phone_input.append(input_var1)
phone_input.append(input_var2)
phone_input.append(input_var3)

print(phone_input)

#reverse list
phones_reverse = phone_input[::-1]
print("Reversed :" , phones_reverse) 

#To Uppercase
phone_toUppercase = [word.upper() for word in phone_input]
print("To uppercase : " , phone_toUppercase)

#To Lowercase
phone_toLowercase = [word.lower() for word in phone_input]
print("To Lowercase : " , phone_toLowercase)

#Strip : The strip() method removes any leading and trailing whitespaces from a string
phone_strip = [word.strip() for word in phone_input]
print("Striped : " , phone_strip)

#Count
element = input("Which phone do you wanna count : ")
phone_count = phone_input.count(element)
print("Counted : " , phone_count)