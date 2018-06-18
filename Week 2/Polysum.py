#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 10:30:14 2018

@author: ElAwbery
"""


# This function sums the area and the square of the perimeter of a polygon. 
# The function returns the sum, rounded to 4 decimal places.

# The area of a polygon is (0.25 * π * s^2)/ tan (π/n)

# assuming that n = number of sides and s = side length

import math

def polysum (n, s):
    '''
    input: two variables, integer or float
    returns the sum of the polygon area, and perimeter length squared, rounded to 4 decimal places.
    '''
    
    def polygonArea (n, s):
        return (0.25 * n * math.pow (s, 2))/(math.tan (math.pi/n))
    
    def perimeterSquare (n, s):
        return (math.pow ((n * s), 2))          # pow (x, y) from the math module returns x raised to the power y
    
    polyArea = polygonArea (n, s)
    perimSquare = perimeterSquare (n, s)
    polySum = polyArea + perimSquare
    
    return round (polySum, 4)
    

