#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 09:26:07 2018

@author: ElAwbery
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    while aStr !='':
    
    #base cases:
       
        if len (aStr) == 1:
            if char == aStr:
                return True
            break
        
        middleLetter = aStr[len(aStr)//2]
        
        if char == middleLetter:
            return True
        
    # recursive call
        elif char < middleLetter:
            aStr = aStr[:aStr.index (middleLetter)]         # cut aStr above char
            isIn (char, aStr)                               # recurse to isIn

        else:
            aStr = aStr[aStr.index (middleLetter)+1:]       # cut string middle letter and below
            isIn (char, aStr)                               # recurse to isIn
        
 
            
        
    return False
        
        
        
        
        
        
