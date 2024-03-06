#this is how a dict can be used with map function.

dict1={'Name':'Alice','Age': 20,'Name2':'Bob', 'Age2': 45}

list1=list(map(lambda x : dict1[x], dict1))
print(list1)

#x represents the key.
