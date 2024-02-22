

string_input = input("Enter your string : ")
string_to_be_counted= str(input("put in the value to be counted : "))
string_Up=string_input.upper()
string_low=string_input.lower()
string_reversed = ''.join(reversed(string_low))
string_strip=string_input.strip()
string_count=string_input.count(string_to_be_counted)

# printed out
print(f"This is the input string : {string_input}")
print(f"This is the string to be counted : {string_to_be_counted}")
print(f"This is the string in uppercase : {string_Up}")
print(f"This is the string in lowercase : {string_low}")
print(f"This is the reversed version of the inputed string : {string_reversed}")
print(f"This is the string when stripped of spaces : {string_strip}")
print(f"This is the total of the string to be counted : {string_count}")
