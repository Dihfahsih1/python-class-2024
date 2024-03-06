#FileNotFoundError: This error occurs when a file does not exist at the specified path


try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")