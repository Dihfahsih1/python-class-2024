#IsADirectoryError: This error occurs when you try to perform a file operation on a directory instead of a file

try:
    with open('/path/to/directory/', 'r') as file:
        content = file.read()
except IsADirectoryError:
    print("Is a directory, not a file.")