#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 12:09:59 2018

@author: Charlie
"""

def gcdIter(a, b):
    
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if a > b:
        smallest = b
    else:
        smallest = a
    
    while smallest > 1: 
        if a%smallest == 0 and b%smallest == 0:
            return smallest
        else: 
            smallest -= 1
    
    return 1
    
    
        