# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 18:21:54 2016
Pulls the location name and yearly totals for analysis and returns it in a list of dictionaries
@author: Connor Moore
"""
import csv
import re




def csvScope(filename, nameString='LOCATION', monthString='YTD'):
    if nameString == '':
        nameString = 'LOCATION'
    elif monthString == '':
        nameString = 'YTD'
    returnList = []
    f = open(filename)
    regex = re.compile('[^a-zA-Z]')
    nameString = regex.sub('',nameString)
    monthString = regex.sub('',monthString)
    csv_f = csv.DictReader(f)    
    
    for row in csv_f:
        orary = ''
        temp= {}
        #will contain both the name and yearly totals.
        orary = (regex.sub('',row['LOCATION'])).lower()
        if orary == (nameString).lower():
            temp = dict({nameString.upper() :  int(row[monthString.upper()])})
            returnList.append(temp)
      
    f.close()
    return returnList