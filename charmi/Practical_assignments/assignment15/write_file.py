#writing a file

#example 1

text1= "Hello World \nMy name is Charmi\nI love python\n"

with open("text1.txt", "w") as file:
    file.write(text1)

#example 2
#appending to a file

text2= "I am 19 years old\nI am a female"

with open("text1.txt", "a") as file:
    file.write(text2)
