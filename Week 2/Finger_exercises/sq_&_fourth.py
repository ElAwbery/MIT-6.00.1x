#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:01:50 2018

@author: ElAwbery
"""

def square (int):
    '''
    input an integer
    returns sqaure of the integer
    '''
    return (int**2)

def fourthPower (int):
    """
    input any integer
    returns that integer to the power of 4
    """
    return (square (square (int)))

