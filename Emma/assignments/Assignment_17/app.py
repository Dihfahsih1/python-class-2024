

def write_to_file():
    new_file = open('files/newfile.txt' ,'w')
    new_text =input("what would you like to write in your file ? \n:")
    new_file.write(new_text)
    

def append_file():
    file = open('files/newfile.txt','a')
    append_text = input("what would you like to add to your text file? \n:")
    file.write(append_text)

def read_file():
    File = open('files/newfile.txt','r')
    print(File.read())
    
        


print("what would you like to do to your text file?")
print("1. write to it")
print("2. read the content")
print("3. append the content")
user_input = input("put in your answer from the numbered list above : ")

if user_input == "1":
    write_to_file()
elif user_input == "2":
    read_file()
elif user_input == "3":
    append_file()

else:
    print("There is no such option")



