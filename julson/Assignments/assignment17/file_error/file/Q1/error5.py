#FileExistsError: This error occurs when trying to create a file that already exists.

try:
    with open('existing_file.txt', 'x') as file:
        file.write("Data")
except FileExistsError:
    print("File already exists.")