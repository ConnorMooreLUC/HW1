# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 02:08:37 2016

@author: galli_000
"""
from geopy.geocoders import Nominatim
import json
from shapely.geometry import shape, Point
os.chdir('C:\\Users\\galli_000\\Desktop\\gitfolder\\HW1')
geolocator = Nominatim()
location = geolocator.geocode("1210 W. Elmdale Avenue Chicago")
print(location.address)
print(location.latitude, location.longitude)

point = Point(location.latitude, location.longitude)
with open('bounds.json') as f:
    data = json.load(f)

for feature in data['features']:
    print( feature['geometry']['type'])
    print( feature['geometry']['coordinates'])


#js = pygeoj.load('bounds.geojson')
#for feature in js:
#    multipoly = shape(feature.geometry.coordinates)
#    if multipoly.contains(point):
#        print('Found containing polygon:', feature)
#    #print(feature,feature.geometry.coordinates)
#        