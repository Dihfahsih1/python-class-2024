import os

file_path = 'text.txt'

try:
    file = open(file_path, 'r')
    print(file.read())

except FileNotFoundError:
    print("This file doesnot exist.")

except 
