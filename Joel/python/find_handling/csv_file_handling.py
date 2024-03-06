import csv

with open('files/csv_file.csv', 'r') as file:
    csv reader = csv.reader(file)
    for row in csv_reader:
        print(row)