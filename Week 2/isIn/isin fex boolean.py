#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:28:16 2018

@author: Charlie
"""

def isIn (char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    Found = True
    
    
    if len(aStr) == 0:
        print ("clause 1 print")
        Found = False
        return print (Found)
    
    
    middleLetter = aStr[len(aStr)//2]                   # redefine middle letter
    print ("redefining midlet as", middleLetter)
    
    
    if len(aStr) == 1:
        
        if char == aStr:
            print ("clause 2 aStr =", aStr)
            Found = True
            return print (Found)
        
        else:
            print ("clause 2 false, astr =", aStr)
            Found = False
            return print (Found)
   
    
    if char == middleLetter:
        print ("char == middleLetter")
        return print (Found) 
    
    
    # recursive calls
    
    elif char < middleLetter:                           # char is lower than middle letter
        aStr = aStr[:aStr.index (middleLetter)]         # cut aStr above char
        print ("elif clause, aStr = ", aStr)
        isIn (char, aStr)                               # recurse to isIn
        
        
    else:
        aStr = aStr[aStr.index (middleLetter)+1:]       # cut string middle letter and below
        print ("else clause, aStr = ", aStr)
        isIn (char, aStr)                               # recurse to isIn
        
 