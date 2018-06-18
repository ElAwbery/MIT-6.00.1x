#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:33:33 2018

@author: ElAwbery
"""

#Exercise: write a program that examines three variables, x y and z, and prints the largest odd number among them. 
#If none of them are odd, it should print a message to that effect
'''
def largest_odd_number (x,y,z):
    if x>y and x>z:
        if x%2 != 0:
            print (x)
    elif y>z and y%2 != 0:
        print (y)
    elif z%2 != 0:
        print (z)
    elif y%2 != 0:
        print (y)
    elif x%2 != 0:
        print (x)
    else:
        print ('there are no odd numbers')
 '''       
        
numX = int(input('How many times should I print the letter X?'))
toPrint = ''
#concatenate x to print numXs times
num =(numX)
while numX < 0:
    print ("I can't print anything less than 0 times. Please try again.")
    numX = int(input('How many times should I print the letter X?'))
num = (numX)
while num > 0:
    num += -1
    toPrint = toPrint + 'X'
print (toPrint)
