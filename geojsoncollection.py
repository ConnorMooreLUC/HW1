# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 02:08:37 2016

@author: galli_000
"""
from geopy.geocoders import GoogleV3, Nominatim
from shapely.geometry import Point, shape, MultiPolygon

import os
import time
import pygeoj

os.chdir('C:\\Users\\galli_000\\Desktop\\gitfolder\\HW1')
#geolocator = GoogleV3()
geolocator = Nominatim()


def toPoint(string):
    temp = geolocator.geocode(string,timeout = 25)
    point=Point(temp.longitude,temp.latitude)
    return point
    

def containCheck(point, neighborList):
    temp = {}
    for item in neighborList:
        multipoly = shape(item.get('Geometry'))
        if multipoly.contains(point):
            temp = {'Neighborhood':item.get('Name')}            
            return temp
    
        
def neighborList(filename):
    os.chdir('C:\\Users\\galli_000\\Desktop\\gitfolder\\HW1')
    testfile = pygeoj.load(filename)
    neighborList = []
    for feature in testfile:
        multipoly = shape(feature.geometry)
        name = feature.properties['pri_neigh']
        temp = {'Name':name, 'Geometry':multipoly}
        neighborList.append(temp)
    
    #print('Checking lasted: ', final - orig)
    #print('Data >> Neighborhood\n')
    return neighborList  
    
def addressGIS(list):
    #orig = time.clock()
    for item in list:
        point = toPoint(item.get('Address'))
        temp = {'Point': point}
        item.update(temp)
        #print(item.get('Library Name'))
    #final = time.clock()
    #print('Checking lasted: ', final - orig)    
    #print('Address >> Point\n')
    return list
    
   
def containmentZipper(neighborList, libList):
    returnlist = []
    #orig = time.clock()
    for item in libList:
        point = shape(item.get('Point'))
        for hood in neighborList:
            multipoly = shape(hood.get('Geometry'))
            #print(type(multipoly))
            if point.within(multipoly)==True:
                temp = {'Neighborhood': hood.get('Name')}
                item.update(temp)
                returnlist.append(item)
    return returnlist
    #final = time.clock()
    #print('Checking lasted: ', final - orig)
    #print('Neighborhood + Point >> Crosslisting\n')        
        

        

