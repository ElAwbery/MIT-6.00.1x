#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 13:14:12 2018

@author: ElAwbery
"""
#Final solution

balance = 999999
annualInterestRate = 0.18

epsilon = 0.01

monthInterest = annualInterestRate/12

low = balance/12
high = balance * ((1 + monthInterest)**12)/12

monthlyGuess = (high + low)/2
          
newBalance = balance
monthCount = 12

    
while abs (newBalance) > epsilon:
    

    newBalance = balance
    monthCount = 12
     
    while monthCount > 0:                   # This gives the end of year balance: 
         
        unpaidBalance = newBalance - monthlyGuess
        
        monthInterest = annualInterestRate/12 * unpaidBalance
        
        newBalance = unpaidBalance + monthInterest
        
        monthCount -= 1
        
    
    if newBalance < -epsilon:               # guess was too high, lower upper boundary
        high = monthlyGuess
        monthlyGuess = (high + low)/2
        
    
    elif newBalance > epsilon:              # guess was too low, raise lower boundary
        low = monthlyGuess
        monthlyGuess = (high + low)/2
        
    
print  ("Lowest payment", round (monthlyGuess, 2))
    
        








