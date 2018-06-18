#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:21:48 2018

@author: Charlie
"""
#It turned out this code is fucked in more than one way and the explanation in the book is both wrong and bad. 

def f(x):
    def g(x):
        x = 'abc'
        print ("within g x = ", x)
    def h():
        z = x
        print ("within h z = ", z)
    x = x + 1
    print ("within f x =", x)
    h ()
    g (237)        #when I run this code I get "TypeError: g() missing 1 required positional argument: 'x'" for this line
    print ("second within f x =", x)
    return g    #sic


x = 3
z = f(x)
print ("global x =", x)
print ("global z =", z)
z()

# The book says this code should print as follows: 
'''
x = 4
z = 4
x = abc
x = 4
x = 3
z = <function f.<locals>.g at 0x1092a7510>
x = abc
'''

# When I try to predict what I think it will print, I get stuck on print ("z = ", z) because I can't see what the return value for 
# f(x) would be in this situation. 



