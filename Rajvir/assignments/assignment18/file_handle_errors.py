# An exception is a condition that arises during the execution of a program. 
# It is a signal that something unexpected happened. 
# Python represents exceptions by an object of a specific type.

import os

file_path = 'text.txt'

try:
    file = open(file_path, 'r')
    print(file.read())

except FileNotFoundError:
    print("This file doesnot exist.")

except ZeroDivisionError:
    print("You can't divide by zero!")

# if you try to open a file with Python, but that file doesn’t exist, you will get an IOError exception.

except IOError as e:
    print("An error occurred:", e)

# The finally block is executed regardless of whether an exception occurs or not. 
# Finally blocks are useful, for example, when you want to close a 
# file or a network connection regardless of what happens.
#  After all, you want to clean up resources to prevent memory leaks.

except IOError as e:
    print("An error occurred:", e)
finally:
    print("Closing the file now")
    f.close()

except KeyError as e:
    print("There are missing fields in the user object: ", e)
# this is used when a key is missing in the dictionary..

except IndexError as e:
    print("first check your index man.")

except PermissionError:
    print("You have no permission.")

except SyntaxError as e:
    print("An error occured.")

except TypeError:
    print("The answer should be a number.")
# this is used to indicate when the user puts in a wrong argument type. 

except MemoryError:
    print("An error has occured.")

except NameError:
    print("An error has occured.")