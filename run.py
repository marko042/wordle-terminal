import random


print("Welcome to Wordle, let's play\n")
print('Please type  a 5 letter word and hit return')

def gen_rand_word()
"""
Generates random word by opening and reading from a file using a split delimiter function 
previously createdcontaining a number of 5 letter words.
"""
    with open("words.txt", "r") as w:
        allText = w.read()
        words = list(map(str, allText.split()))
  
    

