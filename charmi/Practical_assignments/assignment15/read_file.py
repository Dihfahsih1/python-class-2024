#opening and reading a text file in the same folder
#example 1

with open("text.txt", "r") as file:
    print(file.read())

print(file.close())
print("------------------------")

#example 2
# reading an printing lines using thier index numbers
file= open("text.txt", "r")

line= file.readlines()

print(line[0])
print(line[1])
print(line[3])