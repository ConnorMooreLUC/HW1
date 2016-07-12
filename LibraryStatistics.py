#import matplotlib.pyplot as plt
from geojsoncollection import addressGIS, containmentZipper, neighborList
from CSVanalytics import csvScope

import pygal
from pygal.style import CleanStyle
import copy
import time
import os
import re
from collections import OrderedDict

def prelim(string):
    os.chdir('CSV')
    os.chdir(string)
    print(os.listdir())
    wd = os.getcwd()
    filenames = [os.path.join(wd, name)
             for wd, dirs, files in os.walk(wd)
             for name in files
             if name.endswith(".csv")]
    regex = re.compile(r'\\')
    for i in range(len(filenames)):
        temp = regex.split(filenames[i])
        filenames[i] = temp[len(temp)-1] 
               
    return filenames
    
def percentChange(str1, str2):
    change = (int(str2)-int(str1))*(100/int(str1))
    return change

def slimHood(slim):
    num = 1
    sorry = "Sorry not a neighborhood name. Please Try again\n"
    while num == 1:
        temp = ''
        if len(slim)==0:
            temp = (input("Enter First Neighborhood Name: \nOr quit by entering the number 0\n\n>> "))
        else:
            temp = (input("Enter Next Neighborhood Name: \nOr quit by entering the number 0\n\n>> "))
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
def plotter(library, i, string):
    d = copy.deepcopy(library)
    del d['Point']
    chart = pygal.Line(style=CleanStyle)
    chart.title = d['Library Name']
    del d['Library Name']
    del d['Address']
    del d['Neighborhood']
    od = OrderedDict(sorted(d.items()))
    #print(d)
    chart.add(string, list(od.values()))
    chart.x_labels = (list(od.keys()))
    chart.render_to_file('sample' + str(i)+ '.svg')
    del d
    del od
#%%
#%%
def Main():
    printMenu =  "\nGreetings!  Choose functionality:\
          \n1: Display Neighborhood's Library Circulation Rates\
          \n2: Display Neighborhood's Library Visitation Rates\
          \n3: Display both Circulation and Visitation Rates\n4: Exit Console Menu, goodbye!\
          \nenter choice here...\n>> "
#    orig = time.clock()
#    containmentZipper(neighborlist, testlist)
#    final = time.clock()
#    print('Method Calls lasted: ', final-orig)
#    slim = []
#    liblist = []
    choice = 1
    while choice == 1:
        In = input(printMenu)
        try:
            In = int(In)
        except:
            In = 5
        if In == 1:
            string = 'Circulation'
            csvfiles = prelim(string)
            print('Specify Neighboroods of Interest\n\n')
            slim = []
            slimHood(slim)
            for item in slim:
                print(item)
            neighborlist = neighborList('bounds.geojson')
            print('\nBeginning matching')
            slim = consoleComp(slim,neighborlist)
            orig = time.clock()
            liblist = csvScope(csvfiles,slim,string)
            final = time.clock()
            print("Adding locations to library list, lasted: ", final - orig)
            orig = time.clock()
            addressGIS(liblist)            
            final =  time.clock()
            print("\ntime to add points: ",final - orig,'\n')
            print("Matching to Neighborhood\n")
            slimlist = []
            orig = time.clock()
            slimlist = containmentZipper(slim,liblist)
            final  = time.clock()
            print('\nCrosslisting Lasted: ', final - orig)
#            for item in slimlist:
#                try:
#                    print(item)
#                except:
#                    print('None')
            i = 0       
            for item in slimlist:
                plotter(item,i,string)
                i = i+1
        elif In == 2:
            string = 'Visitors'
            csvfiles = prelim(string)
            print('Specify Neighboroods of Interest\n\n')
            slim = []
            slimHood(slim)
            for item in slim:
                print(item)
            neighborlist = neighborList('bounds.geojson')
            print('\nBeginning matching')
            slim = consoleComp(slim,neighborlist)
            orig = time.clock()
            liblist = csvScope(csvfiles,slim,string)
            final = time.clock()
            print("Adding locations to library list, lasted: ", final - orig)
            orig = time.clock()
            addressGIS(liblist)            
            final =  time.clock()
            print("\ntime to add points: ",final - orig,'\n')
            print("Matching to Neighborhood\n")
            slimlist = []
            orig = time.clock()
            slimlist = containmentZipper(slim,liblist)
            final  = time.clock()
            print('\nCrosslisting Lasted: ', final - orig)
#            for item in slimlist:
#                try:
#                    print(item)
#                except:
#                    print('None')
            i = 0       
            for item in slimlist:
                plotter(item,i,string)
                i = i+1
            

        elif In == 3:
            print('Specify Neighboroods of Interest\n\n')
            slim = []
            slimHood(slim)
            for item in slim:
                print(item)
            neighborlist = neighborList('bounds.geojson')
            print('\nBeginning matching')
            slim = consoleComp(slim,neighborlist)



        elif In == 4:
            choice = 0
        else:
            print('\nConsole read error, be sure you specified one of the correct choices (1-4)\n')
Main()
#%%
