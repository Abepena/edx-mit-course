# Hangman game
#

# -----------------------------------

import random, string

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
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
      if letter not in lettersGuessed:
        return False
    return True
  
        


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    for letter in secretWord:
      if letter in lettersGuessed:
        result += letter.upper()
      else:
        result += '_'
    return result.upper()

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters_available = list(string.ascii_lowercase)
    for letter in lettersGuessed:
      if letter in letters_available:
        letters_available.remove(letter)
    
    return "".join(letters_available)

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
  
  lettersGuessed = []
  tries = 8
  word = getGuessedWord(secretWord, lettersGuessed)

  print("Welcome to the game, Hangman!")
  print(f"I'm thinking of a word that is {len(secretWord)} letters long.")
  
  while not isWordGuessed(secretWord, lettersGuessed) and tries > 0:
    print("---------------")
    print(f"You have {tries} guesses left")
    print(f"Letters available: {getAvailableLetters(lettersGuessed).upper()}")
    guess = input("Please guess a letter: ")
    
    if guess in lettersGuessed:
      print(f"Oops! You've already guessed that letter: {word}")
    elif guess in secretWord:
      lettersGuessed.append(guess)
      word = getGuessedWord(secretWord, lettersGuessed)
      print(f"Good guess: {word}")
    else:
      tries -= 1
      print(f"Oops! That letter is not in my word: {word}")
      lettersGuessed.append(guess)

    
    
    
  if isWordGuessed(secretWord, lettersGuessed):
    print("\nGreat job you got it!\n ")
  else:
    print("\nSorry, you didnt guess the word in under 8 guesses. Better luck next time.\n")
  
  print(f"The secret word was '{secretWord.upper()}'")


    
 




  







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

