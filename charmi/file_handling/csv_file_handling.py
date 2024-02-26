import csv

with open('files/csv_file.csv', 'r') as file:
    data= csv.reader(file)
    print(data)