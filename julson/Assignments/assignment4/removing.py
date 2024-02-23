# Adding elements using append()
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Adding elements using extend()
new_elements = [5, 6]
my_list.extend(new_elements)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]




# Removing elements using pop()
popped_element = my_list.pop()
print("Popped element:", popped_element)  # Output: 6
print("Updated list after pop:", my_list)  # Output: [1, 2, 3, 4, 5]

# Removing elements using remove()
my_list.remove(3)
print("Updated list after remove:", my_list)  # Output: [1, 2, 4, 5]

# Removing elements using del
del my_list[1]
print("Updated list after del:", my_list)  # Output: [1, 4, 5]