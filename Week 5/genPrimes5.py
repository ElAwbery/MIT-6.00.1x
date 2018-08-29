#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 13:25:12 2018

@author: Charlie
"""

def genPrimes():
    """yields an infinite sequence of prime numbers"""
    primeList = []
    x = 2
    
    while True: 
        isPrime = True
        for p in primeList:
            if x%p == 0:  
                isPrime = False
                x += 1
        if isPrime:
            primeList.append(x) 
            yield x
            x += 1

fip = genPrimes()
