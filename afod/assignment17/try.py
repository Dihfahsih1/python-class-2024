class FileHandling:
    try:
        def write(self):
            file = open(input("enter file  name and end with.txt"), "w")
            content = file.write(input("enter what you want the file to have: \n"))
            print("content has been written sucessfully")
            print(content , "\n")
            file.close()
    except FileNotFoundError:
        print("File not found")

    try:    
        def read(self):
            file = open(input("enter file name"), "r")
            content = file.read()
            print(content, "\n")
            file.close()
    except FileNotFoundError:
        print("File not found")

    try:
        def append(self):
            file = open(input("enter file name"), "a")
            content = file.write(input("enter what you want to add to the file: " "\n"), )
            print("content has been appended")
            print( content, "\n")
            file.close()
    except FileNotFoundError:
        print("File not found")

file1 = FileHandling()
file1.append()



