# list comprehension is a way of writing a list with less syntax
numbers=[1,2,3,4]
new_numbers=[num*num for num in numbers]
print(new_numbers)

age=[20,50,40,30,13,16,18]
young=[age for age in age if age <= 20]
print(young)

# how to remove an item using pop
print(young.pop(0))

# how to delete in a dictionary
dict1={"mark":40, "Elizabeth":50}
del dict1["Elizabeth"]
print(dict1)
