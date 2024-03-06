import csv
import nOptions


# Function to append data to a CSV file
def append_to_csv(file_name, data):
    with open(file_name, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

# Example data to append
data_to_append = ['John', 'Doe', 30]

# Append data to an existing CSV file
append_to_csv('example.csv', data_to_append)


# Function to join multiple CSV files into one
def join_csv_files(output_file, *input_files):
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        # Write headers
        writer.writerow(['Name', 'Surname', 'Age'])
        # Iterate through input files
        for input_file in input_files:
            with open(input_file, 'r') as infile:
                reader = csv.reader