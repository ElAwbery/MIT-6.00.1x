#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 11:25:41 2018

@author: ElAwbery
"""

# Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 
# 0 < pwr < 6, and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, 
# it should print a message to that effect

# my first attempt:

userInt = int(input("Enter an integer: "))

absUserInt = abs(userInt)
pwr = 2
root = 0
notFound = True

while pwr < 6:
    
    while root <= absUserInt and notFound:
        if root**pwr == absUserInt:
            notFound = False
            if userInt < 0 and root%2 == 0:
                print ("No perfect root")
                break
            elif userInt < 0: 
                root = -root
            print (userInt, "=", root, "^", pwr)
        else:
            root = root + 1
       
    pwr = pwr + 1
    root = 0

if notFound:
    print ("There are no integers such that", userInt, "has an integer root to the power of another integer less than or equal to 6.")


# A later attempt with better code:

userInt = int(input("Enter an integer: "))

pwr = 2
root = 0
notFound = True

while pwr < 6 and notFound: 
    
    while root <= userInt and notFound:
        if root**pwr == userInt:
            print(userInt, "=", root, "^", pwr)
            notFound = False
        else:
            root = root + 1
    pwr = pwr + 1
    root = 0
    
           
if notFound:
    print (userInt, "has no natural roots with 1 < power < 6")
    
