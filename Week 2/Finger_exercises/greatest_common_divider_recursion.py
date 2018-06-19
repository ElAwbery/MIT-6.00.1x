#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 12:55:05 2018

@author: ElAwbery

First attempt, used a helper function when I did not need to:
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:
        smallest = b
        largest = a
        
    else:
        smallest = a
        largest = b
    
    return eucAlg (largest, smallest, largest%smallest)

    
def eucAlg (largest, smallest, remainder):
    '''
    passed largest, smallest and remainder from gcdRecur, all integers
    returns greatest common divisor to gcdRecur
    
    if remainder == 1:
        return 1
    '''   
    if remainder == 0:
        return smallest
        
    else:
        largest = smallest
        smallest = remainder
        remainder = largest%smallest
        return eucAlg (largest, smallest, remainder)
 

# second attempt, didn't take so long to write!
  
def gcdRecur(a, b):
     
    if a > b:
        largest = a
        smallest = b
        
    else:
        largest = b
        smallest = a
        
    remainder = largest%smallest
        
    while largest%smallest > 0:
        largest = smallest
        smallest = remainder
        return gcdRecur (largest, smallest)
    
    return smallest    
        
    
