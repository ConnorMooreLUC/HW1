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

def slimHood(slim):
    num = 1
    sorry = "Sorry not a neighborhood name. Please Try again\n"
    while num == 1:
        temp = ''
        if len(slim)==0:
            temp = (input("Enter First Neighborhood Name: \nOr quit by entering the number 0\n\n:"))
        else:
            temp = (input("Enter Next Neighborhood Name: \nOr quit by entering the number 0\n\n:"))
        try:
            temp = int(temp)
            if temp == 0:
                num = 0
                #print("Thanks")
            else:
                print(sorry)
        except:
            slim.append(str(temp))
    
def consoleComp(stringList,b):
    retNeigh = []
    for item in stringList:
        i = 0
        for i in range(len(b)):
            temp = b[i].get('Name')
            if item.lower() in temp.lower():
                retNeigh.append(b[i])
                print('Matched ', item, 'to ', temp)
                break
            i=i+1
            
    return retNeigh


#%%
def Main():
    printMenu =  "\nGreetings!  Choose functionality:\
          \n1: Display Neighborhood's Library Circulation Rates\
          \n2: Display Neighborhood's Library Visitation Rates\
          \n3: Display both Circulation and Visitation Rates\n4: Exit Console Menu, goodbye!\
          \nenter choice here...\t:"
#    orig = time.clock()
#    testlist = []
#    testlist = csvScope(csvfiles,testlist,'','')
#    os.chdir('C:\\Users\\galli_000\\Desktop\\gitfolder\\HW1')
#    addressGIS(testlist)
#    neighborlist = neighborList('bounds.geojson')
#    containmentZipper(neighborlist, testlist)
#    final = time.clock()
#    print('Method Calls lasted: ', final-orig)
#    slim = []
    choice = 1
    while choice == 1:
        In = input(printMenu)
        try:
            In = int(In)
        except:
            In = 5
        if In == 1:
            print('Specify Neighboroods of Interest\n\n')
            slim = []
            slimHood(slim)
            for item in slim:
                print(item)
            neighborlist = neighborList('bounds.geojson')
            print('\nBeginning matching')
            slim = consoleComp(slim,neighborlist)
            print(slim)
        elif In == 2:
            print('Specify Neighboroods of Interest\n\n')
            slim = []
            slimHood(slim)
            for item in slim:
                print(item)
            neighborlist = neighborList('bounds.geojson')
            print('\nBeginning matching')
            slim = consoleComp(slim,neighborlist)
            print(slim)
        elif In == 3:
            print('Specify Neighboroods of Interest\n\n')
            slim = []
            slimHood(slim)
            for item in slim:
                print(item)
            neighborlist = neighborList('bounds.geojson')
            print('\nBeginning matching')
            slim = consoleComp(slim,neighborlist)
            print(slim)
        elif In == 4:
            choice = 0
        else:
            print('Console read error, be sure you specified one of the correct choices (1-4)\n')
Main()
#%%
