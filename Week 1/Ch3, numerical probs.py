#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 13:13:54 2018

@author: Charlie
"""

#find the cube root of an integer:


userInt = int(input("enter an integer"))

ans = 0

while ans**3 < abs(userInt):
    ans += 1
if  ans**3 != abs(userInt):
    print (userInt, " has no integer cube root.")  
else:
    if userInt < 0:
        ans = -ans
    print ("the cube root of ", userInt, "is ", ans)
    
              
maxVal = int(input("enter a positive integer: "))
i = 0
while i < maxVal:
    i = i + 1
print (i)




# Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 
# 0 < pwr < 6, and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, 
# it should print a message to that effect

# This was my first attempt: 

userInt = int(input("enter an integer: "))
pwr = 2
root = 0


# loop 1: start with root 1. test, root to the power. If it works, exit with details. increment root up to max value. exit. 
# add one to power. go back to top. 

# outside all of this, the condition is power less than 6.  


while pwr < 6:
    
    while root < abs(userInt):
        
        if root**pwr == abs(userInt):
            break
        else:
            root += 1
    
    if root**pwr == abs(userInt):
        break
    else:
        pwr = pwr + 1
        root = 0
    
if root**pwr == abs(userInt):
    
    if userInt < 0:
        root = -root
        print (userInt, "=", root, "to the power of", pwr)
    else:
        print (userInt, "=", root, "to the power of", pwr)
    
else:       
    print ("There are no integers such that", userInt, "has an integer root to the power of another integer less than or equal to 6.")
    

# I wasn't happy with the nested if statements. This is David's suggested code: 

userInt = int(input("Enter an integer: "))

pwr = 2
root = 0
notFound = True

while pwr < 6 and notFound: #is there a reason to include notFound here? 
   
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
    


# My re-write, using the absolute value function:


userInt = int(input("Enter an integer: "))
absUserInt = abs(userInt)
pwr = 2
root = 0
notFound = True

while pwr < 6:
    
    while root <= absUserInt and notFound:
        if root**pwr == absUserInt:
            notFound = False
            if userInt < 0:
                root = -root
            print (userInt, "=", root, "^", pwr)
        else:
            root = root + 1
       
    pwr = pwr + 1
    root = 0

if notFound:
    print ("There are no integers such that", userInt, "has an integer root to the power of another integer less than or equal to 6.")














