#example 1

tuple1=(1,2,3,4,5)
del tuple1
# print(tuple1) #this will bring a syntax error bacause the tuple is deleted

#example 2

list1= [1,2,3,4,5]

list1.remove(4)
print(list1)

print("------------------")

#example 3
dict={'Mango':'fruit', 'Rose':'Flower', 'Blue':'Color'} #using pop method to delete items in dictionaries
dict.pop('Blue')
print(dict)