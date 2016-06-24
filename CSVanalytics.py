# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 18:21:54 2016
Pulls the location name and yearly totals for analysis and returns it in a list of dictionaries
@author: Connor Moore
"""
import csv
import re

def csvScope(filename, returnList=[], nameString='LOCATION', monthString='YTD'):
    print(filename)
    if nameString == '':
        nameString = "LOCATION"
    if monthString == '':
        monthString = "YTD"
    numpat = re.compile('[^0-9]')
    year = numpat.sub('',filename)
    print(year)
    f = open(filename)
    regex = re.compile('[^a-zA-Z]')
    nameString = regex.sub('',nameString)
    monthString = regex.sub('',monthString)
    csv_f = csv.DictReader(f)    
    if nameString == 'LOCATION':
        for row in csv_f:
            if row['ADDRESS'] == '':
                row['ADDRESS']= 'no address found'
            temp= {}
            if row[monthString.upper()].isdigit():
                temp = dict({row[nameString] : row['ADDRESS'], monthString+', '+ year: row[monthString.upper()]})
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
                             monthString+', '+ year: row[monthString.upper()]})
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