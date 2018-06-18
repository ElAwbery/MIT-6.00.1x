#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 11:26:58 2018

@author: Charlie
"""

balance = 3926
annualInterestRate = 0.2


fixedMonthlyPayment = 0
monthCount = 12
newBalance = balance

while newBalance > 0:
    
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
