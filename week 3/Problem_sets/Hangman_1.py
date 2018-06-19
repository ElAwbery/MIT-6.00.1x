# Hangman game
#

# -----------------------------------
# Helper code provided by the course
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    noneWrong = True
   
    for letter in secretWord: 
        
        if letter not in lettersGuessed:
            noneWrong = False
            return noneWrong
        
    return noneWrong 
            

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    wordSoFar = ''
    
    for letter in secretWord:
        
        if letter not in lettersGuessed:
            wordSoFar += ' _ '
            
        else: 
            wordSoFar += letter
            
    return wordSoFar



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    import string
    
    notGuessedYet = list(string.ascii_lowercase)
    
    for letter in lettersGuessed: 
        
        notGuessedYet.remove(letter)
        
    return ''.join(notGuessedYet)
    
    
 
    
secretWord = chooseWord(wordlist).lower()



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    
    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word that is", len(secretWord),  "letters long")
    
    countdown = 8
    lettersGuessed = []
    
    while countdown > 0:
        print('-----------')
        
        if isWordGuessed (secretWord, lettersGuessed) == True:
            return print('Congratulations, you won!')
        
        else: 
    
            print ("You have", countdown, "guesses left")
            print ("Available letters:", getAvailableLetters(lettersGuessed))
            
            guessAnyCase = input("Please guess a letter: ")
            guess = guessAnyCase.lower ()

            if guess in ''.join(lettersGuessed):
                print ("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))

            elif guess in secretWord:
                lettersGuessed += guess
                print ("Good guess:", getGuessedWord(secretWord, lettersGuessed))

            else: 
                countdown -= 1
                lettersGuessed += guess
                print ("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                
    print('-----------')
    return print ("Sorry, you ran out of guesses. The word was", secretWord +'.')

        

            
    
    
    




