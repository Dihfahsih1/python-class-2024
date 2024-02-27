def main():
    Enter=input("Enter text : ")
    file=open('love.txt','w')
    file.write(Enter)
    file.close
    file=open('love.txt','r')
    content=file.read()
    print(content)
    file.close
    enter_2=input('Enter text to add: ')
    file=open('love.txt','a')
    content_2=file.write(enter_2)
    print(content_2)
    file.close
main()
# having trouble putting the text on diffrent lines