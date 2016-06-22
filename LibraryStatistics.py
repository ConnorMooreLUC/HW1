import matplotlib.pyplot as plt
from CSVanalytics import csvScope


library13={} #2013 library dictionary
library14={} #2014 library dictionary
namelist=[]  #list of library names
liblist13=[] #2013 total yearly visitors library list
liblist14=[] #2014 total yearly visitors library list
perdifDict = {} # % differences dictionary


liblista = csvScope('Libraries_-_2013_Circulation_by_Location.csv','','April')
print(liblista)
liblistb = csvScope('Libraries_-_2013_Circulation_by_Location.csv','Edgewater','')
print(liblistb)
liblistc = csvScope('Libraries_-_2013_Circulation_by_Location.csv','Rogers Park','June')
print(liblistc)
liblistd = csvScope('Libraries_-_2013_Circulation_by_Location.csv','Altgeld','June')
print(liblistd)


def percentChange(str1, str2):
    change = (int(str2)-int(str1))*(100/int(str1))
    return change


#testlist = []
#for index in range(len(liblist13)):
#    x = percentChange(liblist13[index],liblist14[index])
#    testlist.append(x)
#    perdifDict[namelist[index]]= float(x)
#    print(namelist[index], "2013: ",
#          liblist13[index],"2014: ",liblist14[index],"  % change: ",
#          x)
#
#del perdifDict['Albany Park  ']  # remove outlier
#
#plt.bar(range(len(perdifDict)),  perdifDict.values())
#plt.xticks(range(len(perdifDict)), perdifDict.keys(),rotation = 45)
#plt.show()