fruits = ['apples','orange','cherry']

for index,fruit in enumerate(fruits):
    print(index,fruit)


# enumerate on a dict
dict1 = {"name":"Emma","age":2000,"gender":"male"}

for index,key in enumerate(dict1):
    print(index,key,dict1[key])


#enumerating with a start index
letters=['a','b','c','d']
for index,letter in enumerate(letters,start=1):
    print(index,letter)

#using enumerate to create a dict out of a list
names = ['alice','john','glass']
dict2 = {index:name for index,name in enumerate(names)}
print(dict2)