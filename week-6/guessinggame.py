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
import tkinter as tk
import random


# print(tk.TkVersion)
# print(tk.TclVersion)

root = tk.Tk()
frm_play_area = ttk.Frame(root, padding=10)
frm_buttons = ttk.Frame(root, padding=10)
frm_play_area.grid()
frm_buttons.grid()


def generateNumber():
    result = random.randint(1, 500)
    print(result)
    updateDisplay(result)


def numberTooLow():
    pass


def numberTooHigh():
    pass


def exactMatch():
    new_game_btn["state"] = "normal"
    pass


def updateDisplay(string_value):
    displayVariable.set(f"Is {string_value} the number you had in mind?")


def playGame():
    new_game_btn["state"] = "disabled"
    generateNumber()


def main():
    root.title("Guessing Game")
    root.mainloop()


displayVariable = StringVar()

greeting_area = ttk.Label(frm_play_area, text="Hello Friend!").grid(column=0, row=0)
play_area = ttk.Label(
    frm_play_area,
    text="Think of a number between 1 and 500 then click 'New Game' to start the guessing game!",
)
play_area.grid(column=0, row=1)
number_area = ttk.Label(
    frm_play_area,
    textvariable=displayVariable,
)
number_area.grid(column=0, row=2)

new_game_btn = ttk.Button(frm_buttons, text="New Game", command=lambda: [playGame()])
new_game_btn.grid(column=0, row=0)
too_low_btn = ttk.Button(frm_buttons, text="Too low!", command=lambda: [numberTooLow()])
too_low_btn.grid(column=1, row=0)
too_high_btn = ttk.Button(
    frm_buttons, text="Too high!", command=lambda: [numberTooHigh()]
)
too_high_btn.grid(column=2, row=0)
exact_match_btn = ttk.Button(
    frm_buttons, text="That's correct!", command=lambda: [exactMatch()]
)
exact_match_btn.grid(column=3, row=0)
quit_game_btn = ttk.Button(frm_buttons, text="Quit", command=root.destroy)
quit_game_btn.grid(column=4, row=0)


if __name__ == "__main__":
    main()
