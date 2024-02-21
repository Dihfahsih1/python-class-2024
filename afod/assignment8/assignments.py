# how to use list comprehension
#They allow you to generate a new list by applying an expression to each item in an existing list.
#also optionally filter the items based on a condition. 

list1= [1,2,3,4,5,'x,' 'jh','r']
numeric_elements = [x for x in list1 if isinstance(x, int) or isinstance(x, float)]
print(numeric_elements) 

# how do you remove an element from a list using a pop method or function?
#To remove an element from a list using the pop() method,
#  you specify the index of the element you want to remove. 
# The pop() method not only removes the element but also returns it. 
# If you don't provide an index, it will remove and return the last element by default.
my_list = [1, 2, 3, 4, 5]

# Removing the element at index 2 (which is 3)
removed_element = my_list.pop(2)
print("Removed element:", removed_element)  # Output: Removed element: 3
print("List after removal:", my_list)       # Output: List after removal: [1, 2, 4, 5]

# Removing the last element without specifying an index
removed_element = my_list.pop()
print("Removed element:", removed_element) 
print("List after removal:", my_list)    

# how to delete in a dictionary
#  you can delete items from a dictionary using the del keyword or the pop()
#Using del keyword:

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Deleting the item with key 'b'
del my_dict['b']
print(my_dict)  # Output: {'a': 1, 'c': 3}

#Using pop() method:

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Deleting the item with key 'b' and returning its value
removed_value = my_dict.pop('b')
print("Removed value:", removed_value)  # Output: Removed value: 2
print("Dictionary after deletion:", my_dict)  # Output: Dictionary after

#how to use logical operators
# logical operators are used to perform logical operations on boolean values or expressions. 
# The three main logical operators are and, or, and not.
#'and': Returns True if both operands are True, otherwise returns False
x = 5
y = 10
z = 15

# Check if x is greater than 0 AND y is greater than 0
result = (x > 0) and (y > 0)
print(result)  # Output: True

# Check if x is greater than 0 AND y is greater than 0 AND z is greater than 0
result = (x > 0) and (y > 0) and (z > 0)
print(result)  # Output: True

#'or': Returns True if at least one operand is True, otherwise returns False.
x = 5
y = -2

# Check if x is greater than 0 OR y is greater than 0
result = (x > 0) or (y > 0)
print(result)  # Output: True

# Check if x is greater than 0 OR y is greater than 0 OR both
result = (x > 0) or (y > 0) or (x == y)
print(result)  # Output: True

#not: Returns the negation of the operand, i.e., 
# True becomes False and False becomes True
x = True
y = False

# Negate the value of x
result = not x
print(result)  # Output: False

# Negate the value of y
result = not y
print(result)  # Output: True

#how to use precidence
# operator precedence determines the order in which operators are evaluated when an
#  expression contains multiple operators.
# Parentheses () - Highest precedence, expressions within parentheses are evaluated first.
# Exponentiation ** - Second highest precedence.
# Unary arithmetic operations: -x, +x, ~x - Unary minus, unary plus, and bitwise NOT.
# Multiplication *, Division /, Floor division //, Modulus % - Multiplication, 
# division, integer division, and modulus have the same precedence and are evaluated from left to right.
# Addition +, Subtraction - - Addition and subtraction have the same precedence 
# and are evaluated from left to right.
# Bitwise shifting <<, >> - Bitwise left shift and bitwise right shift have
#  the same precedence and are evaluated from left to right.
# Bitwise AND & - Bitwise AND.
# Bitwise XOR ^ - Bitwise exclusive OR.
# Bitwise OR | - Bitwise OR.
# Comparison operators: <, <=, >, >=, ==, !=, is, is not, in, not in -
#  Comparison operators have the same precedence and are evaluated from left to right.
# Boolean NOT not - Unary logical NOT.
# Boolean AND and - Logical AND.
# Boolean OR or - Logical OR.
result = 2 + 3 * 4  # Multiplication has higher precedence, so 3 * 4 is evaluated first
print(result)  # Output: 14

result = (2 + 3) * 4  # Parentheses have highest precedence, so 2 + 3 is evaluated first
print(result)  # Output: 20

#assignment operators
#Assignment operators in Python are used to assign values to variables.
# = : Assigns the value on the right side to the variable on the left side
# += : Adds the value on the right side to the variable's current value and assigns the result to the variable.
# -= : Subtracts the value on the right side from the variable's
#  current value and assigns the result to the variable.
# *= : Multiplies the variable's current value by the value on the 
# right side and assigns the result to the variable.
# /= : Divides the variable's current value by the value on the right side and assigns the result
#  to the variable.
# //= : Performs integer division of the variable's current value by the value on the right side and assigns the
#  result to the variable.
# %= : Computes the modulus of the variable's current value divided by the value on the right side and assigns the
#  result to the variable.
#  **= : Raises the variable's current value to the power of the value on the right side and assigns the result
#  to the variable.
# &=, |= , ^= : Performs bitwise AND, OR, and XOR respectively on the variable's current value and the value on the right side, 
# and assigns the result to the variable.

# how to use comparisions 
# comparison operators are used to compare two values or expressions. 
# == : Equal to - Returns True if the values of the two operands are equal, otherwise returns False.
# != : Not equal to - Returns True if the values of the two operands are not equal, otherwise returns False.
# > : Greater than - Returns True if the value of the left operand is greater than the value of the right operand,
#  otherwise returns False.
# < : Less than - Returns True if the value of the left operand is less than the value of the right operand,
#  otherwise returns False.
# >= : Greater than or equal to - Returns True if the value of the left operand is greater than or equal to the value of the right operand,
#  otherwise returns False.
# <= : Less than or equal to - Returns True if the value of the left operand is less than or equal to the 
# value of the right operand, otherwise returns False.
#
# how to use bitwise
#  bitwise operators are used to perform bitwise operations on integers. These operators treat integers as 
# sequences of binary digits (bits) and perform operations on corresponding bits of the operands.
# & : Bitwise AND - Sets each bit to 1 if both bits are 1.

x = 5  # 101 in binary
y = 3  # 011 in binary

result = x & y  # 001 in binary
print(result)   # Output: 1
# | : Bitwise OR - Sets each bit to 1 if at least one of the bits is 1.

x = 5  # 101 in binary
y = 3  # 011 in binary

result = x | y  # 111 in binary
print(result)   # Output: 7
# ^ : Bitwise XOR - Sets each bit to 1 if only one of the bits is 1.

x = 5  # 101 in binary
y = 3  # 011 in binary

result = x ^ y  # 110 in binary
print(result)   # Output: 6
#  : Bitwise NOT - Inverts all the bits.

x = 5  # 101 in binary
result = ~x  # -(x+1) in binary
print(result)   # Output: -6
# << : Left shift - Shifts the bits of the left operand to the left by the number of positions specified
#  by the right operand.

x = 5  # 101 in binary
result = x << 1  # 1010 in binary, equivalent to multiplying x by 2
print(result)    # Output: 10
#>> : Right shift - Shifts the bits of the left operand to the right by the number of positions specified by the right operand.

x = 5  # 101 in binary
result = x >> 1  # 10 in binary, equivalent to dividing x by 2
print(result)    # Output: 2

