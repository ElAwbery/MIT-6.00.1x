#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 15:26:45 2018

@author: ElAwbery
"""


balance = 3926
annualInterestRate = 0.2

lowGuess = balance/12

highGuess = (balance * (1 + annualInterestRate)**12) / 12.0

result = (highGuess + lowGuess)/2


guess = something intelligent                            #pick a guess
monthCount = 12
newBalance = balance

this is a loop: 

test the guess: 
if the guess is too low:
    do this thing
    reset some variables
    must reset the guess
    
elif the guess is too high:
    do this other thing
    reset different variables
    reset the guess
    
else break
print result
    
    

    
    newBalance = balance
    fixedMonthlyPayment +=10
    monthCount = 12

    # This gives the end of year balance: 

    while monthCount > 0 and newBalance > 0:               
          
        unpaidMonthlyBalance = newBalance - fixedMonthlyPayment
        
        monthInterest = annualInterestRate/12 * unpaidMonthlyBalance
        
        newBalance = unpaidMonthlyBalance + monthInterest
        
        monthCount -= 1
        

print  ("Lowest payment:", round (fixedMonthlyPayment, 2))
