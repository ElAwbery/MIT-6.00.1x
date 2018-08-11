#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 19:11:25 2018

@author: ElAwbery
"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    
    userInput = input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
    hand = {}
    
    while userInput != 'r':
        newHand = dealHand(HAND_SIZE)
        hand = newHand
        if userInput == 'n':
            playHand(newHand, wordList, HAND_SIZE)
        elif userInput == 'e':
            return ()
        else:
            print("Invalid command.")
            playGame(wordList)
    
    
    print ("hand =", hand, "n = ", HAND_SIZE)
    try:
        playHand(hand, wordList, HAND_SIZE)
    except:
        print("You have not played a hand yet. Please play a new hand first!")
        playGame(wordList)

    
