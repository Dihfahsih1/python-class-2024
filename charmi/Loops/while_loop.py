# while 0<10:
#     print("infinite loop")     #this prints infintely wihtout terminating

count =3       #this startes counting from 3
while count <= 10:
    print(count)
    count +=1 #this will increament the number by 1
print('*'*20)


#summing numbers from 1 to 10
sum=0
count=1
while count<=10:
    sum += count #This increaments the current sum ie triangular numbers
    count += 1
print("The sum of numbers1 to 10 is:", sum)  #printing outside the while loop will only print the final answer when the limit of the loop had been reached
print('*'*20)

# printing even numbers between 1 and 20
num=2
while num<= 20:
    print(num)  #printing in the while loop will print every answer until terminated
    num+=2
print('*'*20)

y=1
while y<=5:
    print("Hello World")
    y += 1

# looping through strings

string= "Python"
index = 1
while index <= len(string):
    print(str(string))
    index += 1

print('*'*20)

# counting down from a specified number
num= int(input("Enter a number to count down from: "))
while num > 0:
    print(num)
    num -= 1
print ("Happy New Year")

print('*'*20)
numbers=[1,2,3,4,5]
total=0
index=0

while total < 10:
    total += numbers[index]
    index += 1

print("Total: ", total)
print(f"Total: {total} for the list {numbers}")
print('*'*20)

