"""
Author: Andrei Benea
Date written: 6/23/24
Assignment: M05 Programming Assignment Part 2
This program first generates a random number in the range of 1 through 100.
It then prompts the user to guess what the number is. If the guess is higher
than the randomly generated number, the program will display "Too high, try
again." If the guess is lower than the random number, the program should
display "Too low, try again." If the user guesses the number, the program
should congratulate the user and generate a new random number so the game
can start over. An empty input from the user will stop the game.
"""

import re  # import regex module for proper input validation
import random  # import module for random number generation


def get_user_input():
    while True:  # loop to ensure input is valid
        result = input("Type in a number to guess or press Enter to quit: ")
        if result == "":
            print("That's too bad.. Maybe another time!")
            break
        reg = re.search("[^\\-\\s\\d][\\\\^]?", result)  # define regex
        if reg:  # check for regex match
            print("Invalid input. Please try again!")
            continue
        return result


def generate_number():  # generate random number
    random_number = random.randrange(1, 100)
    return random_number


def play_game():  # define game function
    random_number = generate_number()  # generate number on function call
    while True:
        user_input = get_user_input()  # prompt user input on each iteration
        if user_input == None:  # break condition
            break
        elif random_number > int(user_input):  # number higher than input condition
            print("Too low, try again.")
            continue
        elif random_number < int(user_input):  # number lower than input condition
            print("Too high, try again.")
            continue
        else:  # match condition
            print("Congratulations, you have guessed correctly!")
            random_number = generate_number()  # generate new number for replay
            continue


def main():
    play_game()  # call game function


if __name__ == "__main__":
    main()
