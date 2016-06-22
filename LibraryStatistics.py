#import matplotlib.pyplot as plt
from CSVanalytics import csvScope
import numpy as np
import shapely

circbylib = ['Libraries_-_2011_Circulation_by_Location.csv','Libraries_-_2012_Circulation_by_Location.csv',
           'Libraries_-_2013_Circulation_by_Location.csv', 'Libraries_-_2014_Circulation_by_Location.csv',
           'Libraries_-__2015_Circulation_by_Location.csv']
visbylib = ['Libraries_-_2011_Visitors_by_Location.csv','Libraries_-_2012_Visitors_by_Location.csv',
           'Libraries_-_2013_Visitors_by_Location.csv', 'Libraries_-_2014_Visitors_by_Location.csv',
           'Libraries_-_2015_Visitors_by_Location.csv']
library13={} #2013 library dictionary
library14={} #2014 library dictionary
namelist=[]  #list of library names
liblist13=[] #2013 total yearly visitors library list
liblist14=[] #2014 total yearly visitors library list
perdifDict = {} # % differences dictionary

def percentChange(str1, str2):
    change = (int(str2)-int(str1))*(100/int(str1))
    return change


def Main():
    circ11=csvScope(circbylib[0])
    circ12=csvScope(circbylib[1])
    circ13=csvScope(circbylib[2])
    circ14=csvScope(circbylib[3])
    circ15=csvScope(circbylib[4])
    library11=csvScope(visbylib[0])
    library12=csvScope(visbylib[1])
    library13=csvScope(visbylib[2])
    library14=csvScope(visbylib[3])
    library15=csvScope(visbylib[4])
    for i in range(len(circ11)):
        print((circ11[i].keys()),'\n')
Main()

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