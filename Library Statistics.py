import csv

f = open('Library_2013.csv')

csv_f = csv.reader(f)

f.readline()  #skips firstline

for row in csv_f:
    print(row[0],"   ",row[1],"   ",row[16],"\n")

f.close()



g = open('Library_2014.csv')

csv_g = csv.reader(g)

g.readline()  #skips firstline

for row in csv_g:
    print(row[0],"   ",row[1],"   ",row[16],"\n")

g.close()
