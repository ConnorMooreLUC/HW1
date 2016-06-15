import csv

library13={}
library14={}
namelist=[]
liblist13=[]
liblist14=[]

f = open('Library_2013.csv')

csv_f = csv.DictReader(f)

#f.readline()  #skips firstline,  not neccessary with DictReader

for row in csv_f:
    print(row['LOCATION'],row['YTD'])
    library13[row['LOCATION']] = row['YTD']
    liblist13.append(row['YTD'])
    namelist.append(row['LOCATION'])
    
f.close()
print("\n\n\n")




g = open('Library_2014.csv')

csv_g = csv.DictReader(g)

#g.readline()  #skips firstline, not neccessary with DictReader

for row in csv_g:
    print(row['LOCATION'],row['YTD'])
    library14[row['LOCATION']] = row['YTD']
    liblist14.append(row['YTD'])

g.close()

for index in range(len(liblist13)):
    print(namelist[index], "2013: ",
          liblist13[index],"2014: ",liblist14[index],"  % change: "
          ,100*(int(liblist14[index]) - int(liblist13[index]))/int(liblist13[index]))

#print(library13.items(),"\n\n\n")
#print(library14.items())
