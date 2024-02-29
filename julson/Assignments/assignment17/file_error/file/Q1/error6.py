#NotADirectoryError: This error occurs when trying to perform a directory operation on a file
import os

try:
    os.listdir('file.txt')
except NotADirectoryError:
    print("Not a directory.")