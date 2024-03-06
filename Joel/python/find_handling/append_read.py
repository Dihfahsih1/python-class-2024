import os
def append_read_file():
    file_path ='files/data.txt'

    if os.path.exists(file_path):
    content_to_append=input("Enter content to append: ")
    with open(file_)