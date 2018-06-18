#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 09:39:11 2018

@author: ElAwbery
"""

# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5

s = 'azcbobobegghakl'

countVowel = 0

for letter in s:
    
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        countVowel += 1
        
print ('Number of vowels:', countVowel)
    
# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2


s = 'azcbobobegghakl'


countVowel = 0

for letter in s:
    
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        countVowel += 1
        
print ('Number of vowels:', countVowel)

