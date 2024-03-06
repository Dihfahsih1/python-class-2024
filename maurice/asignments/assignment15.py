# writing to a file
fw=open('music.txt','w')
fw.write('I like music\n')
fw.write('But my favorite artist is Selena Gomez')
fw.close()

# reading from a file
fr=open('music.txt','r')
music=fr.read()
print(music)
fr.close()

