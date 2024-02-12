dict1={'a':1,'b':2}
dict2={'a':3, 'b':4,'c':10}

#updating Dictionary
dict1.update(dict2)
print(dict1)

#comparison
dict3={'a':1,'b':2}
dict4={'a':3, 'b':4}
print(dict3==dict4)

#length of a dict
print(len(dict1))

#sorting items in dict
dict5={'b':2, 'a':1, "c":3}
sorted_dict=dict(sorted(dict5.items()))
print(sorted_dict)

 

