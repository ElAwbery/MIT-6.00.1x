#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 17:39:02 2018

@author: ElAwbery
"""

  
    userInput = input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
    
    if userInput == 'n':
        newHand = dealHand(HAND_SIZE)
        playHand(newHand, wordList, HAND_SIZE)
        
    elif userInput == 'r':
        
        try:
            playHand(newHand, wordList, HAND_SIZE)
        except:
            print("You have not played a hand yet. Please play a new hand first!")
            playGame(wordList)
    
    elif userInput == 'e':
        return ()
    
    else:
        print("Invalid command.")
        playGame(wordList)

    
   
    
