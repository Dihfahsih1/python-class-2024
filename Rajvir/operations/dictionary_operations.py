dict1={"a":1, "b":2}
dict2={"b":3, "c":4}

#updating Dictionary
dict1.update(dict2)
print(dict2)

#comparison
dict3={"a":1, 'b':4}
dict4={"a":2, 'b':5}
print(dict3==dict4)

#length of a dict
print (len(dict1))

#sorting items in dict
dict5={"b":2, "a": 1, "c":3}
sorted_dict=dict(sorted(dict5.items()))
print(sorted_dict)