import random # built-in module that you can use to make random numbers/elements
import sys # It allows us to access parameters and functionalities specific to the system
from termcolor import colored # Python library for color and formatting in terminal



def start_menu():
    """
    Prints every time game is started
    """
    print("Welcome to Wordle, let's play\n")
    print('Please type  a 5 letter word and hit return!\n')


def gen_rand_word():
    """
    Generates random word by opening and reading from a file using a split delimiter function 
    previously created containing a number of 5 letter words.
    """
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
        return random.choice(words)
        

start_menu()
word = gen_rand_word() # assigning a variable to a function to catch a random word from the list

for attempt in range(1,7):
    guess = input().lower()

    for i in range( min(len(guess), 5)):# checks only the input of first five letters in case user chooses to insert a longer word that would give up to much of an answer
        if guess[i] == word[i]:
            print(colored(guess[i], 'green'), end = "")
        elif guess[i] in word:
            print(colored(guess[i], 'yellow'), end ="")
        else:
            print(guess[i], end = "" )
    print()

    if guess == word:
        print(colored(f"Good job! you guessed the Wordle in {attempt}", 'red'))
        break
            


    

