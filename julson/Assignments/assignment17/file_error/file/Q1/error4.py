#UnicodeDecodeError: This error occurs when trying to decode a file with an unsupported encoding

try:
    with open('file.txt', 'r', encoding='utf-8') as file:
        content = file.read()
except UnicodeDecodeError:
    print("Unable to decode the file with the specified encoding.")