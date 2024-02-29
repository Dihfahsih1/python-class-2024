import csv 

with open('files/csv_file.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('files/new_csv.csv','w') as new_file:
        csv_writer = csv.writer(new_file, delimiter = '\t')



        for line in csv_reader:
            csv_writer.writerow(line)
            
