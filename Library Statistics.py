import csv

library13={}
library14={}

f = open('Library_2013.csv')

csv_f = csv.DictReader(f)

#f.readline()  #skips firstline,  not neccessary with DictReader

for row in csv_f:
    #print(row[0],"   ",row[1],"   ",row[16],"\n")
    print(row['LOCATION'],row['YTD'])
    library13[row['LOCATION']] = row['YTD']

f.close()




g = open('Library_2014.csv')

csv_g = csv.DictReader(g)

#g.readline()  #skips firstline, not neccessary with DictReader

for row in csv_g:
    print(row['LOCATION'],row['YTD'])
    library14[row['LOCATION']] = row['YTD']

g.close()


#print(library13.items(),"\n\n\n")
#print(library14.items())
