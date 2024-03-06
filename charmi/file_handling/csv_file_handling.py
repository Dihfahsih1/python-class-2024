import csv

with open('files/csv_file1.csv', 'r') as file:
    data= csv.reader(file)
    for row in data:
        print(data)