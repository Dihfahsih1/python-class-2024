# create python files with 3 examples each.
1. #case.py
# "case" typically refers to the way strings are compared, specifically in terms of case sensitivity.
word1 = "Hello"
word2 = "hello"

print(word1 == word2) 

word1 = "Hello"
word2 = "hello"

print(word1.casefold() == word2.casefold())


2. #casting.py
#Casting in Python refers to the process of converting a variable from one data type to another. 

#Implicit Type Conversion:
# Python automatically converts data types when necessary during operations.
# For example, when you add an integer and a float, Python automatically converts the integer to a
#  float before performing the addition.
# Explicit Type Conversion:
# Explicit type conversion involves manually converting a variable from one data type to another using 
# built-in functions or methods.
# Converting a string to an integer
string_num = "123"
integer_num = int(string_num)

# Converting a float to an integer
float_num = 3.14
integer_part = int(float_num)

# Converting an integer to a float
integer_num = 42
float_num = float(integer_num)


3. #delete.py
my_list = [1, 2, 3, 4, 5]
del my_list[2]  
print(my_list)  

# Using remove() method
my_list.remove(4) 
print(my_list)     

my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['b']  
print(my_dict)    

popped_value = my_dict.pop('c')  
print(popped_value)               
print(my_dict)                   

4. #naming.py
total_count = 10
user_name = "John Doe"
is_active = True
5. #multiply.py
# Multiplying integers
result = 3 * 5
print(result)  

# Multiplying floats
result = 3.5 * 2.5
print(result) 

# Multiplying a string to repeat it
message = "Hello, "
repeated_message = message * 3
print(repeated_message)  

# Multiplying a list to repeat it
numbers = [1, 2, 3]
repeated_numbers = numbers * 2
print(repeated_numbers)  
6. #type.py

# Integer
x = 5
print(type(x)) 

# Float
y = 3.14
print(type(y)) 

# String
z = "Hello"
print(type(z))  

# List
my_list = [1, 2, 3]
print(type(my_list))  
