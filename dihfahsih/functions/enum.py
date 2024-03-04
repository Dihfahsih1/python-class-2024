# Enumerate on a list

fruits=['apple','banana','cherry']

for index,fruit in enumerate(fruits):
    print(index,fruit)
    
word_string = 'Python'
for index,word in enumerate(word_string):
    print(index,word)
    
    
#enumerate on a dict
person={'name':'john','age':20, 'gender':'male'}
for index,key in enumerate(person):
    print(index, key, person[key])

#enumerating with a start index
letters=['a','b','c','d']
for index,letter in enumerate(letters,start=10):
    print(index,letter)
    
    
#using enumerate to create a dict out of a list

names=['Alice','Bob','Charlie']
name_dict={index:name for index, name in enumerate(names)}
for index, key in enumerate(name_dict, start=1):
    print(index,key,name_dict[1])
