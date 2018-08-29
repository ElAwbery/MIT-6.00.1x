#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 14:09:29 2018

@author: Charlie
"""
#Code with mistakes in. Got part right in the grader, but not all. 


# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 
# 2, 3, 5, 7, 11, ...
# Have the generator keep a list of the primes it's generated. 
# A candidate number x is prime if (x % p) != 0 for all earlier primes p.
    
def genPrimes ():
    
    x = 2
    primeList = []
    
    while True: 
        
        xIsPrime = True
        
        while xIsPrime:
            
            for p in primeList:
                
                if x%p == 0:
                    x += 1
                    xIsPrime = False 
                    
            yield x
            primeList.append (x)
            x += 1
            xIsPrime = False
            
            
            
            
        