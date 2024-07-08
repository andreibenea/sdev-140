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
from tkinter.font import Font


# create main page
class MainPage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.set_fonts()
        self.create_widgets()
        
    def set_fonts(self):
        self.titleFont = Font(weight="bold", size=22)

    def create_widgets(self):
        self.mainFrame = ttk.Frame(self, padding=10)
        self.mainFrame.grid()

        self.menuButton = tk.Menubutton(self.mainFrame, text="Menu", relief=RAISED, width=3)
        self.menuButton.grid(row=0, column=0)
        self.menuButton.menu = tk.Menu(self.menuButton, tearoff=0)
        self.menuButton["menu"] = self.menuButton.menu

        self.activeList = tk.IntVar()
        self.allLists = tk.IntVar()
        self.menuButton.menu.add_checkbutton(
            label="Active List", variable=self.activeList
        )
        self.menuButton.menu.add_checkbutton(label="All Lists", variable=self.allLists)

        self.pageTitle = ttk.Label(self.mainFrame, text="Shopping Manager")
        self.pageTitle.grid(row=1, column=1)
        self.pageTitle["font"] = self.titleFont

        self.button = ttk.Button(
            self.mainFrame, text="Quit", command=self.quitApplication, width=3
        )
        self.button.grid(row=0, column=2)

        self.searchBar = ttk.Entry(self.mainFrame)
        self.searchBar.grid(row=2, column=1, sticky="NWES")

        self.addToCartImage = tk.PhotoImage(
            file="project_shopping/icons/icons8-cart-16.png"
        )
        self.addButton = ttk.Button(
            self.mainFrame,
            text="Add",
            width=2.5,
            image=self.addToCartImage,
            compound=RIGHT,
        )
        self.addButton.grid(row=2, column=1, sticky="NES")

        self.allListsImage = tk.PhotoImage(
            file="project_shopping/icons/icons8-task-lists-100.png"
        )
        self.allListsImageLabel = ttk.Label(self.mainFrame, image=self.allListsImage)
        self.allListsImageLabel.grid(row=3, column=1)

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
