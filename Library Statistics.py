import csv

f = open('Library_2013.csv')

csv_f = csv.reader(f)

for row in csv_f:
    print(row[16])

f.close()
