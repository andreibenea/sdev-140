"""
Author: Andrei Benea
Date written: 7/7/24
Assignment: Final Project
The goal of this application is to act as a simple tool
for managing weekly shopping needs. It allows the quick
and easy adding of new items that need to be bought,
storing these for when it's time to go shopping. Items
on the list can be checked off as bought, marked as
required for another shopping event, edited or deleted
if needed.
"""

# import modules
from tkinter import *
from tkinter import ttk
import tkinter as tk


# create main page
class MainPage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text="Hello World")
        self.label.grid(column=0, row=0)

        self.button = ttk.Button(self, text="Quit", command=self.quitApplication)
        self.button.grid(column=1, row=1)

    def quitApplication(self):
        self.master.quit()


# create main application
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Shopping Manager")

        self.page = MainPage(self)
        self.page.grid()


# call main
if __name__ == "__main__":
    app = Application()
    app.resizable(width=False, height=False)
    app.mainloop()
