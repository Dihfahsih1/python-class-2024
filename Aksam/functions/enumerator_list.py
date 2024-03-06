
# # enumerate on a list



# my_list = ['apples', 'bananas', 'cherry','Dates']
# for index, value in enumerate(my_list):
#     print(index, value)
    

# Word_Str = 'Python'
# for index,word in enumerate(Word_Str):
#     print(index, word)
    
    
# dict_fold = {
#     'name': 'Aksam',
#     'Age': 17,
#     'gender': 'Male'
# }

# for index,key in enumerate(dict_fold):
#     print(index,key, dict_fold[key])
    
    

names = ['Aksam', 'Cyrus', 'John', 'Doe', 'Kratos']
names_dict = {index:name for index, name in enumerate(names)}
for index,key in enumerate(names_dict):
    print(index,key, names_dict[key])
