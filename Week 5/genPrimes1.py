#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 10:18:49 2018

@author: ElAwbery
"""

def foo ():
    yield 1
    
    
def gentest ():
    yield 1
    yield 'hi'
    yield 'yup'
    yield 7.8
    
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
                print("p=", p)
                
                if x%p == 0:
                    x += 1
                    xIsPrime = False

            yield x
            primeList.append (x)
            
            x += 1
        
