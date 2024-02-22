# WRITING A FILE IN PYTHON EXAMPLE 1
with open("output.txt", "w") as file:
    file.write("Hello, world this is a file created by python \n")
    file.write("writing to a file in Python is easy")
    
# WRITING A FILE IN PYTHON EXAMPLE 2
with open("output.txt", "a") as file:
    file.write("This is example 2 appending \n")
    file.write("Appending to a file in Python is easy")
    
    