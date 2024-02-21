dict1={'a':1, 'b':2}
dict2={'b':3, 'c':4}

#updating a dictionary
dict1.update(dict2)       #updating will update and as well add the other existing keys and thier values.     
print(dict1)

#comparison
dict3={'a':1, 'b':2}
dict4={'a':3, 'b':4}
print(dict3==dict4)

#length of a dictionary
print(len(dict1))

#sorting items ina dictionary
dict5={'b':2, 'a':1, 'c':3}
sorted_dict= dict(sorted(dict5.items()))
print(sorted_dict)
