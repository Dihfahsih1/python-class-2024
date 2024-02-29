try:
    with open('/root/sensitive_file.txt', 'w') as file:
        file.write("Top secret information")
except PermissionError:
    print("Permission denied.")

#PermissionError: This error occurs when you do not have the necessary permissions to access or modify a file