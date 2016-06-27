#import matplotlib.pyplot as plt
from geojsoncollection import addressGIS, containmentZipper, neighborList
from CSVanalytics import csvScope

import time
import os
import re

wd = os.getcwd()
csvfiles = [os.path.join(wd, name)
             for wd, dirs, files in os.walk(wd)
             for name in files
             if name.endswith(".csv")]
                 
                 
regex = re.compile(r'\\')                 
for i in range(len(csvfiles)):
    temp = regex.split(csvfiles[i])
    csvfiles[i] = temp[len(temp)-1]    
    
def percentChange(str1, str2):
    change = (int(str2)-int(str1))*(100/int(str1))
    return change





def Main():
    orig = time.clock()
    #print('WD: ',wd,'\n')
    #print(csvfiles)
    testlist = []
    testlist = csvScope(csvfiles,testlist,'','')
    os.chdir('C:\\Users\\galli_000\\Desktop\\gitfolder\\HW1')
    #for item in testlist:
        #print(item,'\n')
    #print(os.getcwd())
    addressGIS(testlist)
    neighborlist = neighborList('bounds.geojson')
    containmentZipper(neighborlist, testlist)
    for item in testlist:
        print(item,'\n')
    final = time.clock()
    print('Method Calls lasted: ', final-orig)
    
Main()

