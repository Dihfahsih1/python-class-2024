import csv

with open('files/new_csv.csv','r') as open_file:
    csv_reader = csv.reader(open_file)
    for line in csv_reader:
        print(line)