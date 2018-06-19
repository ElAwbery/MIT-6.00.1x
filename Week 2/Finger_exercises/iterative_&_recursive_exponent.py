#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 09:02:15 2018

@author: ElAwbery
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
   '''
    baseExp = 1
    
    while exp > 0:
        baseExp *= base
        exp -= 1
    
    return (baseExp)


def recurPower(base, exp):
    
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''    
    if exp == 1:
       return base
   
    if exp == 0:
        return 1
   
    else: 
        return base * (recurPower (base, exp - 1))
    
    print (base)
    
   
            
        
        
