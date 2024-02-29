import os

def rename_directory(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"Directory '{old_name}' renamed to '{new_name}' successfully.")
    except FileNotFoundError:
        print(f"Directory '{old_name}' not found.")
    except FileExistsError:
        print(f"Directory '{new_name}' already exists.")