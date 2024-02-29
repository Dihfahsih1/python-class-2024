#PermissionError: This error occurs when trying to access a file without the required permissions.


try:
    with open('/root/file.txt', 'r') as file:
        content = file.read()
except PermissionError:
    print("Permission denied.")