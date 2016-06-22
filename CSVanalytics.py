# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 18:21:54 2016
Pulls the location name and yearly totals for analysis and returns it in a list of dictionaries
@author: Connor Moore
"""
import csv
import re

def csvScope(filename, nameString='LOCATION', monthString='YTD',returnList = []):

    if nameString == '':
            nameString = "LOCATION"
    if monthString == '':
            monthString = "YTD"
    f = open(filename)
    regex = re.compile('[^a-zA-Z]')
    nameString = regex.sub('',nameString)
    monthString = regex.sub('',monthString)
    csv_f = csv.DictReader(f)    
    if nameString == 'LOCATION':
        for row in csv_f:
            value = []
            temp= {}
            value.append(int(row[monthString.upper()]))
            temp = dict({row[nameString] : value})
            returnList.append(temp)     
    else:
        for row in csv_f:
            orary = ''
            value = []
            temp= {}
            value.append(int(row[monthString.upper()]))
            #will contain both the name and yearly totals.
            orary = (regex.sub('',row['LOCATION'])).lower()
            if orary == (nameString).lower():
                temp = dict({nameString.upper() : value})
                returnList.append(temp)
          
        f.close()
    return returnList
    
    
def listMod(listL):
    for i  in range(len(listL)-1):
        for k, v in lista[i].items():
            m = list(listb[i].values())
            print(k,v[0],m[0][0])
            lista[i][k] = v[0]-m[0][0]
            print(lista)
                
lista = [{'Sam':[1]}]
listb = [{'Ple':[-1]}] 
listL =[lista, listb]      
listMod(listL)