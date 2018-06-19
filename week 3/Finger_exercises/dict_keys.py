#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:27:04 2018

@author: ElAwbery
"""

# This time, write a procedure, called biggest, which returns the key corresponding to the entry 
# with the largest number of values associated with it. 
# If there is more than one such entry, return any one of the matching keys

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    highest = 0
   
    for key in aDict:
           
       listLength = len (aDict [key])
       
       if listLength >= highest:
           highest = listLength
           largestSoFar = key
       
    return largestSoFar

# this worked.

# Their solution: 

def largest (aDict):
    
    result = None
    biggestValue = 0
    
    for key in aDict.keys():
        
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
            
    return result
