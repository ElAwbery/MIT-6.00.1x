#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 12:46:51 2018

@author: ElAwbery
"""

from math import pi, tan
def polysumPeer(n, s):
    '''
    this function sums the area and square of the perimeter of a regular polygon.
    n : int or float 
    s : int or float 
    returns : a float num rounded to 4 decimal places.
    '''
    perimeter = s * n 
    area = (0.25 * n * s**2) / (tan(pi/n))
    result = area + (perimeter**2)
    
    return round(result, 4)
