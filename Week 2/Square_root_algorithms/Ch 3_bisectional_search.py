#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 14:09:57 2018

@author: ElAwbery
"""

# finger exercise for negative root code: I predict it will print 'numGuesses = 1' and '0 is close to square root of -25;
# I was wrong, because I failed to take the abs value into account in the while loop. 
    
# This code goes into an infinite loop, with low, high and ans all = 0.0
'''
x = -25
epsilon = 0.01
numGuesses = 0
low = 0
high = max(1.0, x)
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print ("low =", low, "high =", high, "ans =", ans)
    
    numGuesses += 1
    if ans**2 < x :
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
    
print ("numGuesses =", numGuesses)
print (ans, "is close to square root of", x) 
'''

# "Exercise pg. 34 in the course textbook: adjust the code to find the cube root of both negative and positive numbers.
# Make sure the answer lies in the region searched: to do this, change low"

# That was not my solution 

programX = 0.5

x = abs(programX)

epsilon = 0.001

numGuesses = 0

low = 0

high = max(1.0, x)

ans = (high + low)/2.0

while abs(ans**3 - x) >= epsilon:
    print ("low =", low, "high =", high, "ans =", ans)
    
    numGuesses += 1
    
    if ans**3 < x:
        low = ans
        
    else:
        high = ans
    ans = (high + low)/2.0

if programX < 0:
    ans = -ans
    
print ("numGuesses =", numGuesses)
print (ans, "is close to cube root of", x) 

