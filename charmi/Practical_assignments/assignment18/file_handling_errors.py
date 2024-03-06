import os

file_path = 'data.txt'

try:
    file = open(file_path, 'r')
    print(file.read())

except FileNotFoundError:
    print("This file doesnot exist.")

except PermissionError:
    print("You have no permission.")

except IOError:
    print("An error has occured.")

except EOFError:
    print("An error has occured.")

except OSError:
    print("An error has occured.")

except RuntimeError:
    print("An error has occured.")

except MemoryError:
    print("An error has occured.")

except NameError:
    print("An error has occured.")

except KeyError:
    print("An error has occured.")
