import os
# file_path = "asignment_17/data.txt"
file_path = "data.txt"
if os.path.exists(file_path):
    # print("File exists")
    new_content = input("Please enter new content to append: ")
    
    with open(file_path, "r") as file:

        content_2 = file.read()
        print(content_2)
else:
    print("file doesnot exist")