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

from tkinter import *
from tkinter import ttk
import random

root = Tk()
frm_play_area = ttk.Frame(root, padding=10)
frm_buttons = ttk.Frame(root, padding=10)
frm_play_area.grid()
frm_buttons.grid()


def generateNumber():
    result = random.randint(1, 500)
    print(result)
    updateDisplay(result)


def updateDisplay(string_value):
    displayVariable.set(string_value)


def playGame():
    print(generateNumber())


def main():
    root.title("Guessing Game")
    root.mainloop()


displayVariable = StringVar()
ttk.Label(frm_play_area, text="Hello Friend!").grid(column=0, row=0)
play_area = ttk.Label(
    frm_play_area,
    text="Think of a number between 1 and 500 then click 'New Game' to start the guessing game!",
    textvariable=displayVariable,
).grid(column=0, row=1)
new_game_btn = ttk.Button(frm_buttons, text="New Game", command=playGame).grid(
    column=0, row=0
)
quit_game_btn = ttk.Button(frm_buttons, text="Quit", command=root.destroy).grid(
    column=2, row=0
)


if __name__ == "__main__":
    main()
