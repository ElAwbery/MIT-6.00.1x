#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:33:33 2018

@author: Charlie
"""

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
        
        
#Exercise: Replace the comment in the following code with a while loop:
     
numX = int(input('How many times should I print the letter X?'))
toPrint = ''
#concatenate x to print numXs times
print (toPrint)

#Answer:

numX = int(input('How many times should I print the letter X?'))

toPrint = ''

print (toPrint)

num =(numX)

while numX < 0:
    print ("I can't print anything less than 0 times, you wally. Please try harder.")
    numX = int(input('How many times should I print the letter X?'))
    
num = (numX)

while num > 0:
    num += -1
    toPrint = toPrint + 'X'
    
print (toPrint)

'''
#Write a program that asks the user to inut 10 integers, and then prints the largest odd number that was entered. 
#If no odd number was entered, it should print a message to that effect. 

userInts = input("write three integers, all less than 10, each separated by a space")

stringNum = userInts[0]
while stringNum != ' ':
    val = stringNum + stringNum
    stringNum = stringNum[+1]
    



while sringNum != ' ':
    #concatenate an integer from srtingNums
    stingNum = stringNum + stringNum
int (stringNum)
print (int)



nextInteger = userIntsLength

#stops when there are no more integers


varA = 6
varB = 7


if type(varA)==str or type(varB)==str:
    print ("string involved")
elif varA > varB:
    print ("bigger")
elif varA == varB:
    print ("equal")
elif varA < varB:
    print ("smaller")










































