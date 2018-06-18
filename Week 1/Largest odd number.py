#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Exercise: write a program that examines three variables, x y and z, and prints the largest odd number among them. 
#If none of them are odd, it should print a message to that effect
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
        
        
    