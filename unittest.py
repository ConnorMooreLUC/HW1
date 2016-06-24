# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 22:37:34 2016
@title Unit Testing Framework. WIP
@author: Connor Moore
"""
import re

monthString = 'YTD'
bool = monthString.upper()=="YTD"
print(bool)
stringArray = []
nameString = '1234455\5\\\est23434er'
regex = re.compile(r'\\')
stringArray = regex.split(nameString)
nameString = stringArray[len(stringArray)-1]
print(stringArray)
print(nameString)