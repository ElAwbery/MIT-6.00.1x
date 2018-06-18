#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 14:07:41 2018

@author: Charlie
"""

# Let s be a string that contains a sequence of decimal numbers separated by commas
# e.g: s = '1.23, 2.4, 3.123'
# Write a program that prints the sum of the numbers in s

total = 0

for num in ('1.23','2.4','4'):  # took a while to figure out the syntax that would work. Each float has to be a separate list literal. 
    total = total + float(num)
print (total)
'''
'''
total = 0

for num in range (1, 7):
    total = total + num
print (total)
   
''' 
'''
num = 5
if num > 2:
    print(num)
    num -= 1
print(num)


num = 5
for num in range (0, 3):
    print (num)

print (num)






