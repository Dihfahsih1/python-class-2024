dict1={'a':1, 'b':2}
dict2={'b':3, 'c':4}

# updating Dictionary it will add the two dicts but if there are two same keys in the two dicts it will replace the value in old list with the value in the updated list
dict1.update(dict2)
print(dict1)

# comparison
dict3={'a':1, 'b':2}
dict4={'d':4, 'c':3}
print(dict3==dict4)
# length (same as in lists)  len

# sorting items in a dictionary  (its different from lists ) items()is a function of a dictionary
dict5={'b':2, 'a':1, 'c':3}
sorted_dict=dict(sorted(dict5.items()))
print(sorted_dict)