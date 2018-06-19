#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 12:05:59 2018

@author: ElAwbery
"""

balance = 320000
annualInterestRate = 0.2
epsilon = 0.01

monthInterest = annualInterestRate/12

low = balance/12
high = balance * ((1 + monthInterest)**12)/12

monthlyGuess = (high + low)/2

print ("start1", balance - monthlyGuess*12)
print ("start2", abs (epsilon))

while abs (balance - monthlyGuess*12) > epsilon:

    # This gives the end of year balance: 
          
    newBalance = balance
    monthCount = 12
    
    while monthCount > 0:
        print ("monthcount while loop start, variables, newBalance, monthlyGuess, monthCount:", newBalance, monthlyGuess, monthCount)               
          
        unpaidBalance = newBalance - monthlyGuess
        
        monthInterest = annualInterestRate/12 * unpaidBalance
        
        newBalance = unpaidBalance + monthInterest
        
        monthCount -= 1
        
        
    if abs (balance - monthlyGuess*12) < epsilon:
        print  ("Lowest payment first print place:", round (monthlyGuess, 2))
        
        break
    
    elif balance - monthlyGuess*12 > epsilon:      # guess was too low, raise lower boundary
        low = monthlyGuess
        print ("firstelif low, high, monthlyGuess:", low, high, monthlyGuess)
        monthlyGuess = (high + low)/2
        monthCount = 12
            
    elif balance - monthlyGuess*12 < -epsilon:     # guess was too high, lower upper boundary
        high = monthlyGuess
        monthlyGuess = (high + low)/2
        print ("secondelif low, high, monthlyGuess:", low, high, monthlyGuess)
        monthCount = 12
    
print  ("Lowest payment second print place:", round (monthlyGuess, 2))
