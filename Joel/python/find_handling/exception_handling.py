import os
try:
    file=open'files/data.tx', 'r')
    print(file.read())
except FileNotFoundError:
    print("File Does not exist")

except PermissionError:
    print("You have no permission to access this file")

finally:
    if os.path.exists(file_path):
      file.close()
    else:
        print("File can't be closed cos it was never opened")

