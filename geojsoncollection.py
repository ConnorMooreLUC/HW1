# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 02:08:37 2016

@author: galli_000
"""
from geopy.geocoders import GoogleV3, Nominatim
from shapely.geometry import Point, shape, MultiPolygon
import os
import pygeoj

os.chdir('C:\\Users\\galli_000\\Desktop\\gitfolder\\HW1')
#geolocator = GoogleV3()
geolocator = Nominatim()


def toPoint(string):
    temp = geolocator.geocode(string)
    point=Point(temp.longitude,temp.latitude)
    return point
    
#point = toPoint('1032 N Sheridan Ave Chicago')
#
#testfile = pygeoj.load("bounds.geojson")
#for feature in testfile:
#    multipoly = shape(feature.geometry)
#    if multipoly.contains(point):
#        print('Woo! it\'s in: ',feature.properties['pri_neigh'])

        
def neighborList(filename):
    testfile = pygeoj.load(filename)
    neighborList = []
    for feature in testfile:
        multipoly = shape(feature.geometry)
        name = feature.properties['pri_neigh']
        temp = {'Name':name, 'Geometry':multipoly}
        neighborList.append(temp)
    #print('done')
    return neighborList  
    
def addressGIS(list):
    for item in list:
        point = toPoint(item.get('Address'))
        temp = {'Point': point}
        item.update(temp)
        #print(item.get('Library Name'))
    print('Address >> Point\n')
    return list
    
   
def containmentZipper(neighborList, libList):
    for item in libList:
        point = shape(item.get('Point'))
        for hood in neighborList:
            multipoly = shape(hood.get('Geometry'))
            if multipoly.contains(point):
                temp = {'Neighborhood': hood.get('Name')}
                item.update(temp)
            
            
        
        
    
    
    
    
    
    
neighborList('bounds.geojson')

