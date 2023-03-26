import random # built-in module that you can use to make random numbers/elements
import sys # It allows us to access parameters and functionalities specific to the system
from termcolo import colored # Python library for color and formatting in terminal



def start_menu():
    """
    Prints every time game is started
    """
    print("Welcome to Wordle, let's play\n")
    print('Please type  a 5 letter word and hit return')


def gen_rand_word():
    """
    Generates random word by opening and reading from a file using a split delimiter function 
    previously created containing a number of 5 letter words.
    """
    with open("words.txt", "r") as w:
        allText = w.read()
        words = list(map(str, allText.split()))
        return random.choice(words)
        print(words)


start_menu()
word = gen_rand_word() # assigning a variable to a function to catch a random word from the list




    

