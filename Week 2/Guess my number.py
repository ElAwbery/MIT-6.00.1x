#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:20:25 2018

@author: Charlie
"""

print ("Please think of a number between 0 and 100!")

print ("Is your secret number 50?")

secretNumber = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

guess = 50
high = 100
low = 0

while secretNumber != 'c':
    
    if secretNumber == 'h':
        high = guess
        
    elif secretNumber == 'l':
        low = guess
   
    else:
        print ("Sorry, I did not understand your input.")
        
    newGuess = low + (high - low)/2
    guess = int(newGuess)
    
    print ("Is your secret number", guess, "?")
    secretNumber = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
print("Game over. Your secret number was:", guess)
      
 
         
 


