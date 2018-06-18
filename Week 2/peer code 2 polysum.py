#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 12:56:46 2018

@author: Charlie
"""


from math import *

def polysum2(n,s):
   '''
   n is the number of sides
   s is the length of each side
   This function will return sum of the area and square of the perimiter of the above specified polygon
   '''
   
   perimiter = n*s    #calculate perimiter
   area = (0.25*n*(s**2)) / (tan(pi/n))    # calculate area
   total = (perimiter**2) + area    # sum area and perimiter squared
   roundedtotal = round(total,4)    # round total to 4 dp
   return roundedtotal