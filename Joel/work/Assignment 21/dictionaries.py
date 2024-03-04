def double_value(dictionary, key):
    if key in dictionary:
        dictionary[key] *= 2
    return dictionary


#List of dictionaries
list_of_dicts = [
    {'a': 1, 'b': 2}
    {'c': 3, 'd': 4}
    {'e': 5, 'f': 6}
]


# Map the function to each dictionary in the list
mapped_result = map(lambda d: double_value(d, 'a'), list_of_dicts)

# Convert the mapped result to a list
mapped_list = list(mapped_result)

print(mapped_list)