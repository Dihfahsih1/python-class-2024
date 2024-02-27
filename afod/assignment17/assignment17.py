#implement a basic file handling application that has read, write, append
class FileHandling:
    try:
        def write(self):
            file = open(input("enter file  name and end with.txt"), "w")
            content = file.write(input("enter what you want the file to have: \n"))
            print(content, "\n")
            file.close()
    except FileNotFoundError:
        print("file doesnot exist")

    try:
        def read(self):
            file = open(input("enter file name"), "r")
            content = file.read()
            print(content, "\n")
            file.close()
    except FileNotFoundError:
        print("file doesn't exist")

    try:
        def append(self):
            file = open(input("enter file name"), "a")
            content = file.write(input(" \n , enter what you want to add to the file: "), )
            print(content, "\n")
            file.close()
    except FileNotFoundError:
        print("file doesn't exist")

if __name__ == "__main__":
    FileHandling()

