import os

file_path = 'data.txt'

try:
    file = open(file_path, 'r')
    print(file.read())

except FileNotFoundError:
    print("")

except PermissionError:
    print("")

except IOError:
    print("")

except EOFError:
    print('')

except OSError:

except RuntimeError:

except MemoryError:

except NameError:

except KeyError:
