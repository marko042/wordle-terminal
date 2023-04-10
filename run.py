import random
# built-in module that you can use to make random numbers/elements

import sys
# It allows us to access parameters and functionalities specific to the terminal

from termcolor import colored
# Python library for color and formatting in terminal




def begin_game():

    """
    menu that appears when we start the game, including
    short instruction and a bit of graphic to be more
    user friendly and engaging for the player 
    """
    print("""


 __          __           _ _        _______                  _             _ 
 \ \        / /          | | |      |__   __|                (_)           | |
  \ \  /\  / /__  _ __ __| | | ___     | | ___ _ __ _ __ ___  _ _ __   __ _| |
   \ \/  \/ / _ \| '__/ _` | |/ _ \    | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
    \  /\  / (_) | | | (_| | |  __/    | |  __/ |  | | | | | | | | | | (_| | |
     \/  \/ \___/|_|  \__,_|_|\___|    |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|
                                                                              
                                                                              


    """)


    print('Green specifies the correct letter and position.')
    print('Yellow specifies the letter is in the word, but in the wrong position.')
    print('White indicates that the letter is not in the word.\n')

    print('Are you upto this challenge, I will give you SIX tries')
    print("try to guess my secret 5 letter word and hit enter \n")

def gen_random_word():
    """
    Using with function, open the file in read mode. 
    The with function takes care of closing the file automatically.
    Read all the text from the file and store in a string
    Split the string into words separated by space.
    Use random.choice() to pick a word or string.
    """
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)

begin_game()


def play_game():
    """
    putting the logic of word lenght and also the colored letters into one function
    so we can call it conveniently later when giving a player choice to play again
    """
    word = gen_random_word() # reading a random word from list 
    

    for attempt in range(1, 7):
        guess = input('Your 5 letter word of choice is:\n').lower()
        while len(guess) != 5:
            print('Invalid entry! Enter a five letter word.')
            guess = input('Your 5 letter word of choice is: ').lower()
            

    # overwrite the last line in the console
        sys.stdout.write("\x1b[1A")
        sys.stdout.write("\x1b[2K")

        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
                # guess is in word and correct position
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
                # guess is in word but diff. position
            else:
                print(guess[i], end="")
        print()

        if guess == word:
            print(colored(f"You guessed my secret word in {attempt} attempts", 'red'))
            break
        elif attempt == 6:
            print(f'You lose, the correct word was -> {word}')
            print()

play_game()   

replay = input("Do you want to play again (type yes or no): ")
if replay == 'yes' or replay == 'y':
    play_game()
else:
    sys.exit()
