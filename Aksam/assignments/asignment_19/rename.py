import os 

def rename_function(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"Directory `{old_name}` has been renamed to `{new_name}` successfuly. ")
    except OSError as e:
        print(f"Error: {e}")
     

old_directory = input("Enter the directory you want to rename: ")
new_directory = input("Enter the new name for the directory: ")       
rename_function(old_directory, new_directory)