import csv
import matplotlib.pyplot as plt


library13={} #2013 library dictionary
library14={} #2014 library dictionary
namelist=[]  #list of library names
liblist13=[] #2013 total yearly visitors library list
liblist14=[] #2014 total yearly visitors library list
perdifDict = {} # % differences dictionary

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

def percentChange(str1, str2):
    change = (int(str2)-int(str1))*(100/int(str1))
    return change


testlist = []
for index in range(len(liblist13)):
    x = percentChange(liblist13[index],liblist14[index])
    testlist.append(x)
    perdifDict[namelist[index]]= float(x)
    print(namelist[index], "2013: ",
          liblist13[index],"2014: ",liblist14[index],"  % change: ",
          x)

del perdifDict['Albany Park  ']  # remove outlier

plt.bar(range(len(perdifDict)),  perdifDict.values())
plt.xticks(range(len(perdifDict)), perdifDict.keys(),rotation = 45)
plt.show()