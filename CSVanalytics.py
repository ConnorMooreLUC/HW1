# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 18:21:54 2016
Pulls the location name and yearly totals for analysis and returns it in a list of dictionaries
@author: Connor Moore
"""
import csv
import re

def csvScope(filename, returnList=[], nameString='LOCATION', monthString='YTD'):
    regex = re.compile('[^a-zA-Z]')
    nameString = regex.sub('',nameString)
    monthString = regex.sub('',monthString)
    if nameString == '':
        nameString = "LOCATION"
    if monthString == '':
       monthString = "YTD"
    for i in range(len(filename)):
        print(filename[i])
        numpat = re.compile('[^0-9]')
        year = numpat.sub('',filename[i])
        print(year)
        f = open(filename[i])
        csv_f = csv.DictReader(f)    
        if nameString == 'LOCATION':
           for row in csv_f:
                if row['ADDRESS'] == '':
                    row['ADDRESS']= 'no address found'
                temp= {}
                value = row[monthString.upper()]
                if  value.isdigit():
                    temp = dict({row[nameString] : row['ADDRESS'], monthString+', '+ year: value})
                else:
                    temp = dict({row[nameString] : row['ADDRESS'], monthString+', '+ year: 0})
                returnList.append(temp)     
        else:
            for row in csv_f:
                if row['ADDRESS'] == '':
                    row['ADDRESS']= 'no address found'
                orary = ''
                value = 0
                temp= {}
                if row[monthString.upper()].isdigit():
                   value = (int(row[monthString.upper()]))
                #will contain both the name and yearly totals.
                orary = (regex.sub('',row['LOCATION'])).lower()
                if orary == (nameString).lower():
                    temp = dict({nameString.upper() : row['ADDRESS'],
                                monthString+', '+ year: value})
                returnList.append(temp)
          
        f.close()
    return returnList
    
    
def listMod(listL):
    for i  in range(len(listL)-1):
        for k, v in listL[i].items():
            m = list(listL[i+1].values())
            print(k,v[0],m[0][0])
            lista[i][k] = v[0]-m[0][0]
            print(lista)
                
#lista = [{'Sam':[1]}]
#listb = [{'Ple':[-1]}] 
#listL =[lista, listb]      
#listMod(listL)