# file writting and reading...
# write()... this function writes a fixed sequence of characters to a file.. 
# read()... this fuction reads the entire file and returns a string..
def wr_file():
    file =open("test.txt","w")
    file.write("this is data inside a file..")
    file.close()

    file= open("test.txt","r")
    print(file.read())
    file.close()
start= int(input("Enter the range you want to begin with: "))
end= int(input("Enter the range with a number u want to stop: "))
step = int(input("Enter the step u want it to follow: "))
for i in range(start,end,step):

    def main():
        print(i)

    if __name__ =="__main__":
        main()
        wr_file()