try:
    with open('corrupted_file.txt', 'r') as file:
        content = file.read()
except IOError:
    print("An I/O error occurred.")

#IOError: This is a generic input/output error that can occur when reading or writing to a file.