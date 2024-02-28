import os

def rename():

    source_directory = 'C:/Users/Dell/Desktop/python-class-2024/charmi/file_handling/files'

    destination_directory = 'C:/Users/Dell\Desktop/python-class-2024/charmi/Practical_assignments/assignment19/assignment_files'

    try:
        os.rename(source_directory, destination_directory)
        print('Directory has been renamed.')

    except IsADirectoryError:
        print("This is a directory.") 

    except Exception as e:
        print(f"{e}")

rename()
