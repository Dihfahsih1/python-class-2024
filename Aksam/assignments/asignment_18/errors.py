# Error 1: Forgetting to import the necessary module
import os

# Error 2: Providing an incorrect file path
file_path = "non_existent_file.txt"

# Error 3: Forgetting to open the file in the appropriate mode
try:
    with open(file_path) as f:
        data = f.read()
except FileNotFoundError:
    print("Error 3: File not found.")

# Error 4: Attempting to write to a file opened in read mode
try:
    with open(file_path, "r") as f:
        f.write("This will raise an error.")
except IOError:
    print("Error 4: Cannot write to a file opened in read mode.")

# Error 5: Not handling file closing properly
f = open(file_path, "w")
try:
    f.write("Some data")
finally:
    f.close()

# Error 6: Using a file object after closing it
f.close()
f.write("Some data")

# Error 7: Incorrectly specifying file encoding
try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read().decode('utf-8')
except UnicodeDecodeError:
    print("Error 7: Unable to decode file with specified encoding.")

# Error 8: Writing to a read-only file
try:
    with open(file_path, "r") as f:
        f.write("Attempting to write to a read-only file.")
except IOError:
    print("Error 8: Cannot write to a read-only file.")

# Error 9: File path contains illegal characters
invalid_file_path = "C:/Users/John/Documents:file.txt"
try:
    with open(invalid_file_path) as f:
        data = f.read()
except OSError:
    print("Error 9: Invalid characters in file path.")

# Error 10: Insufficient permissions to access the file
protected_file_path = "/root/protected_file.txt"
try:
    with open(protected_file_path) as f:
        data = f.read()
except PermissionError:
    print("Error 10: Insufficient permissions to access the file.")
