my_list =["apples", "bananas","cherry","dates"]

for index, value in enumerate(my_list):
   # print(f"index: {index}, value: {value}")
   print (f"[{index}, {value}]")

#on a dict

student_info={'name':'Rajvir','age':19,'gender':'Female'}
for index, key in enumerate(student_info):
   print(index,key,student_info[key])

#enumerating with a start index
letters=['a','b','c','d']
for index,letter in enumerate(letters, start=10):
   print(index,letter)

names =["raj","charm","kaur","panc","jk"]
name_dict= {index:name for index, name in enumerate(names, start=-2)}

print(index,name_dict)