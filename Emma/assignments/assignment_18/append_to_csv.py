import csv

data_to_add = [
    ['Clark','kenya','clark@gmail.com'],
    ['Peter','Egypt','Peter@gmail.com']
]


with open('files/csv.csv','a', newline='') as file:
    writer = csv.writer(file)


writer.writerows(data_to_add)



