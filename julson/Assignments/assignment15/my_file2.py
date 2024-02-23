# Open the file
with open('my_text.txt', 'r') as file:
    # Read line by line
    for line in file:
        # Process each line
        print(line.strip())  # strip() removes any trailing whitespace like '\n'