import os
file_dir = 'files/newfile.txt'

try:
    file = open(file_dir, 'r')
    print(file.read())

except FileNotFoundError:
    print("file not found")

except PermissionError:
    print("file not found")

except IOError :
    print("file not found")

except EOFError:
    print("file not found")

except OSError:
    print("file not found")

except RuntimeError:
    print("file not found")

except MemoryError:
    print("file not found")

except NameError:
    print("file not found")

except KeyError:
    print("file not found")

except Exception:
    print("file not found")
