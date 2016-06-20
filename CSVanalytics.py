# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 18:21:54 2016
Pulls the location name and yearly totals for analysis and returns it in a dictionary
@author: Connor Moore
"""
import csv
import re

returnList = []

def csvScope(filename, mod):
  if mod!=0:
      print( "adding month implementation soon.")
      return
    

  f = open(filename)

  csv_f = csv.DictReader(f)
  for row in csv_f:
      orary = ''
      temp= {}
      #will contain both the name and yearly totals.
      #print(row['LOCATION'],row['YTD'])
      orary = re.sub(r'(\*)','',row['LOCATION'])
      #print(orary)
      #print(isinstance(orary, str))
      temp = dict({orary :  int(row['YTD'])})
      returnList.append(temp)
      
  f.close()
  return returnList