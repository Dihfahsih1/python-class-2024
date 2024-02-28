# how do we read a file and write a file in python
# You can use the built-in open() function to open a file and then use methods like read(), readline(), 
# readlines() for reading, and write() for writing.
with open('newfile.txt',) as file:
    data = file.read()
    print(data)

# # Writing to a file
# with open('newfile.txt', 'w') as file:
#     file.write('Hello, world!')

try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("that file was not found")

text = "yooooooooooooooo\ngotchu"
with open('test.txt', 'w') as file:
    file.write(text)

def main():
    
    step = int(input("Enter the step: "))
    start = int(input("Enter the start value: "))
    end = int(input("Enter the end value: "))

    
    generated_range = list(range(start, end, step))
    print("Generated range:", generated_range)

if __name__ == "__main__":
    main()