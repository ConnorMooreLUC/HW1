# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 02:08:37 2016

@author: galli_000
"""
from geopy.geocoders import GoogleV3
from shapely.geometry import Point, shape
import os
import pygeoj


os.chdir('C:\\Users\\galli_000\\Desktop\\gitfolder\\HW1')
geolocator = GoogleV3()
location = geolocator.geocode('1032 Sheridan Rd Chicago')
print(location.address)
print(location.latitude, location.longitude)

point = Point(location.longitude, location.latitude)
point2 = Point(location.latitude, location.longitude)

testfile = pygeoj.load("bounds.geojson")
for feature in testfile:
    #print(feature.geometry.type)
    #print(testfile.common_attributes)
    #print(feature.properties['pri_neigh'])
    #print(feature.geometry)
    #print(multipoly)
    #print('\nSuccess\n')
    multipoly = shape(feature.geometry)
    if multipoly.contains(point):
        print('woo',feature.properties['pri_neigh'])
        print(multipoly.bounds)
    elif multipoly.contains(point2):
        print('wippee')
    elif multipoly.bounds.__contains__(point):
        print('Succes; in neighborhood: ', feature.properties['pri_neigh'])
    elif multipoly.bounds.__contains__(point2):
        print('Yay', feature.properties['pri_neigh'])
             