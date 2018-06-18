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

sLetterCounter = s

countBobs = 0

for letter in sLetterCounter:
    
    if s[:3] == 'bob':
        countBobs += 1
    s = s[1:]
      
print ('Number of times bob occurs is:', countBobs)



# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh

# Note: This problem may be challenging. We encourage you to work smart. 
# If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. 
# If you have time, come back to this problem after you've had a break and cleared your head.

    
s = 'mcnnkfjm'

index = 0

subString = ''

tempSubString = s[0]

sLetterCounter = range(0,(len(s)-1))

for letter in sLetterCounter: 
       
        if s[index] <= s[index + 1]: # if the letter is in order
            tempSubString = tempSubString + s[index + 1]
            
        else: # if the letter isn't in order:
            if len(subString) >= len(tempSubString):
                tempSubString = s[index + 1]
                
            else: 
                subString = tempSubString
                tempSubString = s[index + 1] 
             
        index += 1
        
if len(tempSubString) > len(subString):
    subString = tempSubString
    
print ("Longest substring in alphabetical order is:", subString)

 





































