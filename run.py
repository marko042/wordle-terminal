import random

# built-in module that you can use to make random numbers/elements
import sys

# It allows us to access parameters and functionalities specific to the terminal
from termcolor import colored

# Python library for color and formatting in terminal


def start_menu():

    print("Welcome to wordle Terminal")
    print("try to guess my secret 5 letter word and hit enter: \n")


def gen_rand_word():
    """
    reads random word by opening and reading from a file using a split delimiter function
    previously created containing a number of 5 letter words.
    """
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
        return random.choice(words)


start_menu()
word = gen_rand_word()  # assigning a variable to a word user is trying to guess

go_again = ""
while go_again != "q":
    for attempt in range(1, 7):
        guess = input().lower()

        # overwrite the last line in the console
        sys.stdout.write("\x1b[1A")
        sys.stdout.write("\x1b[2K")

        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                print(colored(guess[i], "green"), end="")
            elif guess[i] in word:
                print(colored(guess[i], "yellow"), end="")
            else:
                print(guess[i], end="")
        print()

        if guess == word:
            print(f"You win! The word was, {word} and it took you {attempt} times")
            break
        elif attempt == 6:
            print(f"wrong the correct word  was {word}")
    go_again = input("Want to play again?\n Type q to exit.\n")
