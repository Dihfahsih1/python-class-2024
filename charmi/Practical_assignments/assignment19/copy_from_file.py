import shutil

def copy_file():

    source_file = 'C:/Users/Dell/Desktop/python-class-2024/charmi/Practical_assignments/assignment19/assignment_files'
    destination_file = "C:/Users/Dell/Desktop/python-class-2024/charmi/file_handling/files"

    try:
        shutil.copy(source_file, destination_file)
        print("File has been copied")

    except Exception as e:
        print(F"{e}")

copy_file()