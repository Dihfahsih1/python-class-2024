# Python abs() built-in function is used to return an absolute
#  value of any numeric value input as an argument to the function.

# The absolute value of a number is its distance 
# from zero on the number line, without considering its direction.

num = -4
num_abs = abs(num)
print(num_abs)

# see here it may be negative but the outcome is positive beacuse -4 is 4 units away from 0.returning 
# hence answer wil be positive 

    #''''using on complex number''''
# An integer, such as 4, -15, or 10.
# A floating-point number, such as 4.1, -15.06, or 2.13.
# A complex number. A complex number is made up of two parts -
#  a real part which consists of a real number such as 1 or 4, 
#  and an imaginary part. In Python, the imaginary part is created 
#  by adding the letter j as a suffix – not the letter i like it is in Mathematics. 
#  You add j to the end of a real number, 
# like so: 1j or 4j.So, an example of a complex number in Python is 2 + 4j or 1 + 2j.

num2 = 2+ 3j
abs_num2 = abs(num2)
print(abs_num2)
# using a square with abs function..

num3 = float(input("Enter any number: "))
abs_num3 = abs((lambda x : x**2)(num3))
print(abs_num3)
