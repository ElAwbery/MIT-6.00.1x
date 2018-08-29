#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 12:52:31 2018

@author: Charlie
"""

# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 
# 2, 3, 5, 7, 11, ...
# Have the generator keep a list of the primes it's generated. 
# A candidate number x is prime if (x % p) != 0 for all earlier primes p.
    
def genPrimes():
    
    primeList = []
    x = 2
    
    while True: 
        if isxPrime (x, primeList):  #if x is prime:
            primeList.append(x)
            yield x
        x += 1 
    
def isxPrime(x, primeList):
    for p in primeList:
        if x%p == 0:
            return False
    return True


fup = genPrimes()

