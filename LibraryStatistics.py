#import matplotlib.pyplot as plt
from CSVanalytics import csvScope
import numpy as np
import shapely
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
    csvfiles[i] = 'CSV//' + temp[len(temp)-1]    
    
def percentChange(str1, str2):
    change = (int(str2)-int(str1))*(100/int(str1))
    return change


def Main():
    print('WD: ',os.getcwd(),'\n')
    testlist = []
    testlist = csvScope(csvfiles[0],testlist,'','')
    print(testlist)
    
    
Main()

