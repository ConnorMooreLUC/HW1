# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 18:21:54 2016
Pulls the location name and yearly totals for analysis and returns it in a dictionary
@author: Connor Moore
"""
import csv
returnList = []

def csvScope(filename, mod):
  if mod!=0:
      print( "adding month implementation soon.")
      return
    

  f = open(filename)

  csv_f = csv.DictReader(f)
  for row in csv_f:
      temp= {}
      #will contain both the name and yearly totals.
      #print(row['LOCATION'],row['YTD'])
      temp[row['LOCATION']] = int(row['YTD'])
      returnList.append(temp)
    
  f.close()
  return returnList