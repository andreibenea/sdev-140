"""
Author: Andrei Benea
Date written: 7/6/24
Assignment: M06 Programming Assignment
This program is a game in which the computer is the one guessing
a number, while the user is responding with either "Too small",
"Too large", or "Correct". Depending on the user's response, the
computer will generate a new number (trying to guess correctly),
or will consider the game over. The game starts (again) using a
"New Game" button.
"""

# import modules
from tkinter import *
from tkinter import ttk
import tkinter as tk
import random

# create widgets
root = tk.Tk()  # create root object
frm_play_area = ttk.Frame(root, padding=10)  # create frame
frm_buttons = ttk.Frame(root, padding=10)  # create frame
frm_play_area.grid()  # setup as grid
frm_buttons.grid()  # setup as grid

# define global variables
generated_number = None  # generated number
highest_generated = None  # highest value during one game
lowest_generated = None  # lowest value during one game


# define functions
def generateNumber(lowest: int = 1, highest: int = 100):  # default values are 1 and 100
    global generated_number  # access global variable
    generated_number = random.randint(lowest, highest)  # generate random number
    print(generated_number)  # print value for debugging purposes
    updateDisplay(
        generated_number
    )  # call function to update display with generated value
    too_low_btn["state"] = NORMAL  # reset button states
    too_high_btn["state"] = NORMAL  # reset button states
    if generated_number == 100:
        too_low_btn["state"] = DISABLED  # disable button if max value
    if generated_number == 1:
        too_high_btn["state"] = DISABLED  # disable button if min value


def numberTooLow():
    global lowest_generated  # access global variable
    lowest_generated = generated_number  # save lowest value
    print(
        f"Lowest generated is: {lowest_generated}"
    )  # print value for debugging purposes
    print(
        f"Highest generated is: {highest_generated}"
    )  # print value for debugging purposes
    print(f"Button clicked is: 'Too low'!")  # print value for debugging purposes
    if highest_generated != None:  # case for both values being different from None
        if (
            highest_generated - lowest_generated == 1
        ):  # case if user tries to trick the computer player
            print(
                f"The difference between the Highest and Lowest is '1'"
            )  # print value for debugging purposes
            displayVariable.set(
                f"I hope you're not trying to fool me! The number must be either {int(lowest_generated)} or {int(highest_generated)}."
            )  # display only possible values
            too_low_btn["state"] = DISABLED  # disable buttons due to game over
            too_high_btn["state"] = DISABLED  # disable buttons due to game over
        elif highest_generated - lowest_generated == 2:  # case for final possibility
            displayVariable.set(
                f"Hmm.. the only remaining option is {int((highest_generated + lowest_generated) / 2)}"
            )  # display only possible value
            too_low_btn["state"] = DISABLED  # disable buttons due to game over
            too_high_btn["state"] = DISABLED  # disable buttons due to game over
        else:
            generateNumber(
                lowest_generated + 1, highest_generated - 1
            )  # generate number while considering previous limits
    else:  # case for one value being None
        if lowest_generated == 99:  # case for final possibility
            displayVariable.set(
                f"Ok, in that case the only remaining option is {int(100)}."
            )  # display only possible value
            too_low_btn["state"] = DISABLED  # disable buttons due to game over
            too_high_btn["state"] = DISABLED  # disable buttons due to game over
        else:
            generateNumber(
                lowest_generated + 1, 100
            )  # generate number while considering previous limit


def numberTooHigh():
    global highest_generated  # access global variable
    highest_generated = generated_number  # save highest value
    print(
        f"Lowest generated is: {lowest_generated}"
    )  # print value for debugging purposes
    print(
        f"Highest generated is: {highest_generated}"
    )  # print value for debugging purposes
    print(f"Button clicked is: 'Too high'!")  # print value for debugging purposes

    if lowest_generated != None:  # case for both values being different from None
        if (
            highest_generated - lowest_generated == 1
        ):  # case if user tries to trick the computer player
            print(
                f"The difference between the Highest and Lowest is '1'"
            )  # print value for debugging purposes
            displayVariable.set(
                f"I hope you're not trying to fool me! The number must be either {int(lowest_generated)} or {int(highest_generated)}."
            )  # display only possible values
            too_low_btn["state"] = DISABLED  # disable buttons due to game over
            too_high_btn["state"] = DISABLED  # disable buttons due to game over
        elif highest_generated - lowest_generated == 2:  # case for final possibility
            displayVariable.set(
                f"Hmm.. the only remaining option is {int((highest_generated + lowest_generated) / 2)}"
            )  # display only possible value
            too_low_btn["state"] = DISABLED  # disable buttons due to game over
            too_high_btn["state"] = DISABLED  # disable buttons due to game over
        else:
            generateNumber(
                lowest_generated + 1, highest_generated - 1
            )  # generate number while considering previous limits
    else:  # case for one value being None
        if highest_generated == 2:  # case for final possibility
            displayVariable.set(
                f"Ok, in that case the only remaining option is {int(1)}."
            )  # display only possible value
            too_low_btn["state"] = DISABLED  # disable buttons due to game over
            too_high_btn["state"] = DISABLED  # disable buttons due to game over
        else:
            generateNumber(
                1, highest_generated - 1
            )  # generate number while considering previous limit


def exactMatch():
    new_game_btn["state"] = NORMAL  # enable New Game button due to game over
    too_low_btn["state"] = DISABLED  # disable buttons due to game over
    too_high_btn["state"] = DISABLED  # disable buttons due to game over
    exact_match_btn["state"] = DISABLED  # disable buttons due to game over
    displayVariable.set(
        "Good guessing! Time for another round?"
    )  # display congratulation message


def newGame():
    new_game_btn["state"] = (
        DISABLED  # disable New Game button for improved gaming experience
    )
    too_low_btn["state"] = NORMAL  # enable buttons for New Game
    too_high_btn["state"] = NORMAL  # enable buttons for New Game
    exact_match_btn["state"] = NORMAL  # enable buttons for New Game
    global generated_number  # access global variable
    global highest_generated  # access global variable
    global lowest_generated  # access global variable
    generated_number = None  # reset value for New Game
    highest_generated = None  # reset value for New Game
    lowest_generated = None  # reset value for New Game
    generateNumber()  # generate new number on each New Game


def updateDisplay(string_value):
    displayVariable.set(
        f"Is {string_value} the number you had in mind?"
    )  # display generated number


def main():
    root.title("Guessing Game")  # define title
    root.resizable(width=False, height=False)  # prevent window resizing
    root.mainloop()  # start mainloop


# display variable
displayVariable = StringVar()

# messages
greeting_area = ttk.Label(frm_play_area, text="Hello Friend!")
play_area = ttk.Label(
    frm_play_area,
    text="Think of a number between 1 and 500 then click 'New Game' to start the guessing game!",
)
number_area = ttk.Label(
    frm_play_area,
    textvariable=displayVariable,
)

# display grid setup
greeting_area.grid(column=0, row=0)
play_area.grid(column=0, row=1)
number_area.grid(column=0, row=2)

# buttons
new_game_btn = ttk.Button(frm_buttons, text="New Game", command=lambda: [newGame()])
too_low_btn = ttk.Button(
    frm_buttons, text="Too low!", command=lambda: [numberTooLow()], state=DISABLED
)
too_high_btn = ttk.Button(
    frm_buttons, text="Too high!", command=lambda: [numberTooHigh()], state=DISABLED
)
exact_match_btn = ttk.Button(
    frm_buttons, text="That's correct!", command=lambda: [exactMatch()], state=DISABLED
)
quit_game_btn = ttk.Button(frm_buttons, text="Quit", command=root.destroy)

# button grid setup
new_game_btn.grid(column=0, row=0)
too_low_btn.grid(column=1, row=0)
too_high_btn.grid(column=2, row=0)
exact_match_btn.grid(column=3, row=0)
quit_game_btn.grid(column=4, row=0)


# call main
if __name__ == "__main__":
    main()
