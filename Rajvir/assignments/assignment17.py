def wr_file():

    file=open("data.txt","w") 
    file.write(input("Enter any text here: "))
    print(file.write)
    file.close()

    file=open("data.txt","r")
    content =file.read()
    print(content)
    file.close()

    text = input("enter the text to append: ")
    file=open("data.txt","a")
    file.write(textg)
    file.close()
wr_file()