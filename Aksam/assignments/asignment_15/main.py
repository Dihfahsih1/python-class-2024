# READING FROM  A FILE
with open("helloWorld.txt", "r") as file:
    file_data = file.read()
    print(file_data)
    
# READING FROM A FILE EXAMPLE 2
with open("helloWorld.txt", "r") as file:
    file_lines = file.readlines()
    for line in file_lines:
        print(line.strip())