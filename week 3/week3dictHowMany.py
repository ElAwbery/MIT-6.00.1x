#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 13:01:56 2018

@author: Charlie
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists of strings.

    returns: int, how many strings are in the dictionary.
    ''' 

 
    count = 0
    
    for key in aDict:
        count += len (aDict[key])
    
    return count
 
# You can walk down the dictionary key doing something to the value each time. 
 
    
    
    
    
    