#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 13:54:32 2018

@author: Charlie
"""

balance = 3926
annualInterestRate = 0.2


lowestPossiblePcmPayment = balance/12
highestPossiblePcmPayment = (balance * (1 + annualInterestRate)**12) / 12.0

guessMonthly = (highestPossiblePcmPayment + lowestPossiblePcmPayment) / 2.0

print ("balance minus abs =", balance - abs (guessMonthly * 12))

while (balance - abs(guessMonthly * 12)) > 0.01: 
    
   guessMonthly = (highestPossiblePcmPayment + lowestPossiblePcmPayment) / 2.0
   print ("low =", lowestPossiblePcmPayment, "high=", highestPossiblePcmPayment, "guess=", guessMonthly)
    
   if balance - (guessMonthly * 12) > 0:         #guess is too high, new guess should be lower
       highestPossiblePcmPayment = guessMonthly
       
   elif balance - (guessMonthly * 12) < 0: 
       lowestPossiblePcmPayment = guessMonthly
       
   else:
       break

print ("Lowest Payment:", round (guessMonthly, 2))
