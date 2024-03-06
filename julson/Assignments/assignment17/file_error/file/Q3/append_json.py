import json

# Specify the file path
file_path = 'data.json'

# Data to append
new_data = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# Load existing JSON data from the file
with open(file_path, 'r') as file:
    existing_data = json.load(file)

# Append new data to existing data
existing_data.append(new_data)

# Write the updated data back to the file
with open(file_path, 'w') as file:
    json.dump(existing_data, file, indent=4)

print('Data appended successfully.')