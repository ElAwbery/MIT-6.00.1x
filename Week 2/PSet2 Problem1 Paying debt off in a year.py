#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 12:08:24 2018

@author: Charlie
"""

'''
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
The following variables contain values as described below:

    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

    monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. 
At the end of 12 months, print out the remaining balance. 
Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of
Remaining balance: 813.4141998135 

So your program only prints out one thing: the remaining balance at the end of the year in the format:

Remaining balance: 4784.0

'''

def annualCardStatement (balance, annualInterestRate, monthlyPaymentRate):
    '''
    input integer or float for all arguments
    returns remaining balance at the end of one year
    '''
    
    monthCount = 12
    
    while monthCount > 0:               #calculates monthly payment
    
        minMonthlyPayment = round ((balance * monthlyPaymentRate), 2)
        
        unpaidMonthlyBalance = round ((balance - minMonthlyPayment), 2)
         
        monthInterest = annualInterestRate/12 * unpaidMonthlyBalance
        
        balance = round ((unpaidMonthlyBalance + monthInterest), 2)
        
        monthCount -= 1

    return print ("Remaining balance:", balance)  


# This failed the grader test. Came back with "make sure you don't define a function! "
# Maybe they might have said that in the first place. They've been fucking teaching us to define functions, then they
    # randomly set a problem where they don't want a function definition, but don't bother to mention it. 
    # fucking waste of time. 





