import csv

data_to_add = [
    ['Clark','kenya','clark@gmail.com'],
    ['Peter','Egypt','Peter@gmail.com']
]


file = open('files/csv.csv','a', newline='')
writer = csv.writer(file)


writer.writerows(data_to_add)

file.close()

