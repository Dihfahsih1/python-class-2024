# Lines to write to the file
lines_to_write = [
    "First line",
    "Second line",
    "Third line"
]

# Open the file in write mode ('w' mode will overwrite existing file or create a new one)
with open('output.txt', 'w') as file:
    # Write each line from the list to the file
    for line in lines_to_write:
        file.write(line + '\n')  # Add a newline character to separate lines