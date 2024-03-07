import shutil

openfile = open('files/text1.txt','w')
openfile.write("Chesse and soda")

source = 'files/test1.txt'
destination = 'files/text2.txt'

shutil.copy(source,destination)