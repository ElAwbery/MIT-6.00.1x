#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:13:20 2018

@author: Charlie
"""

def square (num):
    '''
    Input: int or float
    Returns square of num
    '''
    
    return num**2


def evalQuadratic (a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*x**2+b*x+c

def d(x, y):
    return x > y


def a(x, y, z):
    if x:
        return y
    else:
        return z


