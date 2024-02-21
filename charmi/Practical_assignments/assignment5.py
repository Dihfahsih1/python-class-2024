#list comprehension

students=['Charmi', 'Rajvir', 'Joel', 'Mumbere', 'Emma', 'Morris', 'Aksam']
index=0

new_list= [student for student in students if 'a' in student]

print(new_list)



# removing from list using pop method

list1=[1,2,3,4,5,6]
list1.pop(3)
print(list1)

#deleting from dictionary using pop method
dict={'Mango':'fruit', 'Rose':'Flower', 'Blue':'Color'}
dict.pop('Blue')
print(dict)