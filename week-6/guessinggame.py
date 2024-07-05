"""
Author: Andrei Benea
Date written: 7/1/24
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
root = tk.Tk()
frm_play_area = ttk.Frame(root, padding=10)
frm_buttons = ttk.Frame(root, padding=10)
frm_play_area.grid()
frm_buttons.grid()

# define global variable to store number
generated_number = None
highest_generated = None
lowest_generated = None


# define functions
def generateNumber(lowest: int = 1, highest: int = 100):
    global generated_number
    generated_number = random.randint(lowest, highest)
    print(generated_number)
    updateDisplay(generated_number)


def numberTooLow():
    global lowest_generated
    lowest_generated = generated_number
    if highest_generated != None:
        generateNumber(lowest_generated + 1, highest_generated - 1)
    else:
        generateNumber(lowest_generated, 100)


def numberTooHigh():
    global highest_generated
    highest_generated = generated_number
    if lowest_generated != None:
        generateNumber(lowest_generated + 1, highest_generated - 1)
    else:
        generateNumber(1, highest_generated)


def exactMatch():
    new_game_btn["state"] = "normal"
    displayVariable.set("Good guessing! Time for another round?")


def newGame():
    new_game_btn["state"] = DISABLED
    too_low_btn["state"] = NORMAL
    too_high_btn["state"] = NORMAL
    exact_match_btn["state"] = NORMAL
    result = generateNumber()
    return result


def updateDisplay(string_value):
    displayVariable.set(f"Is {string_value} the number you had in mind?")


def main():
    root.title("Guessing Game")
    root.mainloop()


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
too_low_btn = ttk.Button(frm_buttons, text="Too low!", command=lambda: [numberTooLow()], state=DISABLED)
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
