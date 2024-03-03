my_list=['apples', 'banana', 'cherry', 'orange']

for index, value in enumerate(my_list): #enumerate keeps track of the index
    print(f" [{index}, {value}]")


# enumerating in a dictionary

my_dict = {'Name': 'Charmi', 'Age': '19', 'Gender': "Female"}

for index, key in enumerate(my_dict):
    print(index, key, my_dict[key])         #for accessing a value we use square brackets using its key


#For starting from a specified number(using start index)

students= ('Charmi', 'Rajvir')
for index, student in enumerate(students, start=1):
    print(index, student)


#using enumerate to create a dict from a list

names = ['Charmi', 'Rajvir','Mary', 'John', 'Sarah']
new_dict = {index : name for index, name in enumerate(names, start=-1)}

print(new_dict)

for index, name in enumerate(new_dict):
    print(index, name, new_dict[-1])