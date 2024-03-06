#Double numbers in a list
numbers = [1,2,3,4,5]

double numbers=map(lambda x:x*2, numbers)

print(list(double_numbers))

#mapping a function to convert strings to uppercase

words=['Hello', 'World']
upper_case=map(str.upper, words)
print(list(upper_case))