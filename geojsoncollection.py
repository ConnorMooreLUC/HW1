# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 02:08:37 2016

@author: galli_000
"""
from geopy.geocoders import Nominatim
import json
from shapely.geometry import Point, MultiPolygon
import os
import pygeoj


os.chdir('C:\\Users\\galli_000\\Desktop\\gitfolder\\HW1')
geolocator = Nominatim()
location = geolocator.geocode("1210 W. Elmdale Avenue Chicago")
print(location.address)
print(location.latitude, location.longitude)

point = Point(location.latitude, location.longitude)
#with open('bounds.json') as f:
#    js = json.load(f)
#    print(js.keys())
#    for item in js['data']:
#        print(type(item))
#        item.sort()
#        for entry in item:
#            print(item)

testfile = pygeoj.load("bounds.geojson")
for feature in testfile:
    print(feature.geometry.type)
    print(feature.geometry.coordinates)
    #sample = MultiPolygon(feature.geometry.coordinates)
    #print(type(sample))
    #print(sample.contains(point))
    #print(sample)            

#js = pygeoj.load('bounds.geojson')
#for feature in js:
#    multipoly = shape(feature.geometry.coordinates)
#    if multipoly.contains(point):
#        print('Found containing polygon:', feature)
#    #print(feature,feature.geometry.coordinates)
        