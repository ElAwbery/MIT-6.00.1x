#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:04:46 2018

@author:ElAwbery
"""
#this attempt worked in my Python Shell but was not accepted by the course grader

def isIn (char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    
    if len(aStr) == 0:
        return False
    
    
    middleLetter = aStr[len(aStr)//2]                   # redefine middle letter
    
    if len(aStr) == 1:
        
        if char == aStr:
            return True
        
        else:
            return False
   
    
    if char == middleLetter:
        return True
    
    
    # recursive calls
    
    elif char < middleLetter:                           # char is lower than middle letter
        aStr = aStr[:aStr.index (middleLetter)]         # cut aStr above char
        isIn (char, aStr)                               # recurse to isIn
        
        
    else:
        aStr = aStr[aStr.index (middleLetter)+1:]       # cut string middle letter and below
        isIn (char, aStr)                               # recurse to isIn
        
 
