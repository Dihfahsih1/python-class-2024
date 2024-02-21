Adams_info=['Adam', 89, 10.3, True]
Chris_info=['Chris', 90, 9.8, False]

# original lists
print('Original Adam list :', Adams_info)
print('Original Chris list :',Chris_info)

# item removed list

Adams_info.remove(89)
print('Adam List after modification :', Adams_info)

# using the pop method

Chris_info.pop(1)

print('Chris list after modification :', Chris_info)


# deleting an items from a list
del Adams_info[0:2]
print(Adams_info)

