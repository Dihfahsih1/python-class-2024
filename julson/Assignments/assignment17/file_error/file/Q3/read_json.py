import json

# Specify the file path
file_path = 'data.json'

# Open the JSON file and load the data
with open(file_path, 'r') as file:
    data = json.load(file)

# Access and print the data
print(data)