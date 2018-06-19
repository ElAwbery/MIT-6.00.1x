#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 10:53:25 2018

@author: ElAwbery
"""

balance = 3926
annualInterestRate = 0.2
epsilon = 0.01

monthInterest = annualInterestRate/12 * balance

monthCount = 12

low = balance/12
high = balance * (1 + monthInterest**12)/12 #this sum was wrong for a long time, due to a typo I did not notice. Missing paren. 
newBalance = balance
monthlyGuess = (high + low)/2


while abs (newBalance) > epsilon:

    # This gives the end of year balance: 

    while monthCount > 0:               
          
        unpaidBalance = newBalance - monthlyGuess
        
        monthInterest = annualInterestRate/12 * unpaidBalance
        
        newBalance = unpaidBalance + monthInterest
        print ("newbal=", newBalance)
        
        monthCount -= 1
        
    if abs (newBalance) < epsilon:
        break
    
    elif newBalance > epsilon:      # guess was too low, raise lower boundary
        low = monthlyGuess
        newBalance = balance
        monthCount = 12
            
    elif newBalance < -epsilon:     # guess was too high, lower upper boundary
        high = monthlyGuess
        newBalance = balance
        monthCount = 12
    
print  ("Lowest payment:", round (monthlyGuess, 2))
