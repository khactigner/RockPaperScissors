# Python Rock Paper Scissors Game
import random
from enum import IntEnum

# enum class to assign attributes to rock, paper, and scissors
class Hand(IntEnum):
    rock = 1
    paper = 2
    scissors = 3


# while-if block to determine the winner of the game.
play_again = False
while not play_again:
    # gets the player choice
    player_choice = int(input("Please enter a number:\nrock (1)\npaper (2)\nscissors (3)\n\n"))
    player_choice = Hand(player_choice)
    # gets the computer choice from a list of choices
    cpu_choice = Hand(random.randint(1, 3))
    if cpu_choice == player_choice:
        print("Tie! Go again!")
        # rock choice
    elif player_choice == 1:
        if cpu_choice == 2:
            print("The Computer chose: " + Hand(2).name + "\nSorry paper beats rock!")
            repeat = input("Would you like to play again (Please pick a number)?:\n yes[0]\nno[1]")
            if repeat == 0:
                play_again = True
            else:
                play_again = False
        elif cpu_choice == 3:
            print("The Computer chose: " + Hand(3).name + "\nRock beats scissors CONGRATULATIONS!!! YOU WIN!")
            repeat = input("Would you like to play again (Please pick a number)?:\n yes[0]\nno[1]")
            if repeat == 0:
                play_again = True
            else:
                play_again = False

print("Thanks for playing!")
