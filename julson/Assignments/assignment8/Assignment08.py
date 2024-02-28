numbers = [1, 2, 3,4 ,5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)

#Pop
element = numbers.pop(3)
print("This is a Pop number :", element)
print("This are numbers after pop :",numbers)