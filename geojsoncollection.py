# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 02:08:37 2016

@author: galli_000
"""
from geopy.geocoders import GoogleV3
from shapely.geometry import Point, shape, MultiPolygon
import os
import pygeoj


os.chdir('C:\\Users\\galli_000\\Desktop\\gitfolder\\HW1')
geolocator = GoogleV3()
location = geolocator.geocode('1032 Sheridan Rd Chicago')
print(location.address)
print(location.latitude, location.longitude)

point = Point(location.longitude, location.latitude)

testfile = pygeoj.load("bounds.geojson")
for feature in testfile:
    multipoly = shape(feature.geometry)
    if multipoly.contains(point):
        print('Woo! it\'s in: ',feature.properties['pri_neigh'])

        
def neighborList(point):
    testfile = pygeoj.load('bounds.geojson')
    neighborList = []
    for feature in testfile:
        multipoly = shape(feature.geometry)
        name = feature.properties['pri_neigh']
        temp = {name:multipoly}
        neighborList.append(temp)
    for item in neighborList:
        if 'Rogers Park' in list(item.keys()):
            print('Woo, again!')
            multipoly = (item.get('Rogers Park'))
            print(multipoly.contains(point))
    return neighborList  
    
neighborList(point)