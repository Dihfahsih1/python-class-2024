import csv

# Specify the file path
file_path = 'data.csv'

# Data to append
data = ['John', 'Doe', 30]

# Open the CSV file in append mode
with open(file_path, 'a', newline='') as file:
    csv_writer = csv.writer(file)
    
    # Append the data to the CSV file
    csv_writer.writerow(data)
    
print('Data appended successfully.')