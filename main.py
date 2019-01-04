# Created by:   Patrick Archer
# Date:         21 December 2018
# Copyright to the above author. All rights reserved.

"""

Directions - COMPLETE, with operational bugs:
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether
they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras - INCOMPLETE:
(1 - COMPLETE) Keep the game going until the user types “exit”
(2 - INCOMPLETE) Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""

import random

# ################################################# start_funcs

def checkGuess(correctInt, userGuess):

    try:

        if (userGuess.lower() == "quit"):
            userGuess = 404

        correctInt = int(correctInt)
        userGuess = int(userGuess)

    except (ValueError):
        print("\n<CONSOLE>: An error has occurred when trying to convert values to integers.\n")
        return "err"

    if (correctInt == userGuess and userGuess != 404):
        #print("\nNice one, you guessed right!\n")
        return "="
    elif (correctInt < userGuess and userGuess != 404):
        #print("\nNot quite. your guess was smaller than the number I am thinking of. Try again!\n")
        return ">"
    elif (correctInt > userGuess and userGuess != 404):
        #print("\nNot quite. your guess was larger than the number I am thinking of. Try again!\n")
        return "<"
    elif (userGuess == 404):
        return "quit"
    else:
        print("\n<CONSOLE>: An error has occurred.\n")
        return "err"

def playGame(correctInt):

    # prompt user to enter # guess between 1 and 9
    userGuess = input("\n--> Please enter a digit between 1 and 9, then press \"Enter\".\n")

    # call checkGuess()
    response = checkGuess(correctInt, userGuess)

    if (response == "="):
        print("\nNice one, you guessed correctly.\n")
    elif (response == ">"):
        print("\nNot quite, your guess was higher than the value I have in my head. Try again.\n")
        playGame(correctInt)
    elif (response == "<"):
        print("\nNot quite, your guess was lower than the value I have in my head. Try again.\n")
        playGame(correctInt)
    elif (response == "err"):
        print("\n<CONSOLE>: An error has been returned from checkGuess().\n")
    elif (response == "quit"):
        print("\nOk, the game will now end.\n")
    else:
        print("\n<CONSOLE>: An error has occurred.\n")

# ################################################# end_funcs/start_main

flag_exitProgram = False

while (flag_exitProgram == False):

    pause_startGame = input("\n\n\nPlease press \"Enter\" when you are ready to begin the game.\n")

    # generate a random integer between 1 and 9
    randInt = random.randint(1, 9)

    #print(randInt)  # debug

    print("\nHmm...I am thinking of a number between 1 and 9."
          "\nCan you guess what it is?\n")

    playGame(randInt)

    pause_playAgain = str(input("\nWould you like to play again? Type y/n.\n")).lower()

    if (pause_playAgain == "y"):
        flag_exitProgram = False
    elif (pause_playAgain == "n"):
        flag_exitProgram = True
    else:
        print("\n<CONSOLE>: An error has occurred. Ending program to prevent catastrophe.\n")
        flag_exitProgram = True


# ################################################# end_main






