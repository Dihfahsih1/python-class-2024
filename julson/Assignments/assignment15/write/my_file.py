# Open the file in write mode ('w' mode will overwrite existing file or create a new one)
with open('output.txt', 'w') as file:
    # Write a single string to the file
    file.write("This is a line written to the file.")