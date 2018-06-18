#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 12:08:24 2018

@author: Charlie
"""

def testReturn (arg1, arg2):
    if arg1 == arg2:
        print ("arg1 is the same as arg2")
        return True
    else:
        return False
    
def abstractTest (arg):
    return testReturn (arg, arg + 1)
    
abstractTest (3)

      