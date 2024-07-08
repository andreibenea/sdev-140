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
from tkinter.font import Font
import tkinter as tk


# create main page
class MainPage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.set_fonts()  # init fonts
        self.create_widgets()  # init widgets

    # define page fonts
    def set_fonts(self):
        self.titleFont = Font(weight="bold", size=22)

    # define page widgets
    def create_widgets(self):
        # main window
        self.mainFrame = ttk.Frame(self, padding=10)
        self.mainFrame.grid()

        # menu/nav button
        self.menuButton = tk.Menubutton(
            self.mainFrame, text="Menu", relief=RAISED, width=3
        )
        self.menuButton.grid(row=0, column=0)
        self.menuButton.menu = tk.Menu(self.menuButton, tearoff=0)
        self.menuButton["menu"] = self.menuButton.menu
        self.activeList = tk.IntVar()
        self.allLists = tk.IntVar()
        self.menuButton.menu.add_checkbutton(
            label="Active List", variable=self.activeList
        )
        self.menuButton.menu.add_checkbutton(label="All Lists", variable=self.allLists)

        # page title
        self.pageTitle = ttk.Label(self.mainFrame, text="Shopping Manager")
        self.pageTitle.grid(row=1, column=1)
        self.pageTitle["font"] = self.titleFont

        # quit button
        self.quitButton = ttk.Button(
            self.mainFrame, text="Quit", command=self.quitApplication, width=3
        )
        self.quitButton.grid(row=0, column=2)

        # input box
        self.entryBar = ttk.Entry(self.mainFrame)
        self.entryBar.grid(row=2, column=1, sticky="NWES")

        # add to list button and image
        self.addToListImage = tk.PhotoImage(
            file="project_shopping/icons/icons8-cart-16.png"
        )
        self.addToListButton = ttk.Button(
            self.mainFrame,
            text="Add",
            width=2.5,
            image=self.addToListImage,
            compound=RIGHT,
        )
        self.addToListButton.grid(row=2, column=1, sticky="NES")

        # all lists image (link)
        self.allListsImage = tk.PhotoImage(
            file="project_shopping/icons/icons8-task-lists-100.png"
        )
        self.allListsImageLabel = ttk.Label(self.mainFrame, image=self.allListsImage)
        self.allListsImageLabel.grid(row=3, column=1)

    # quit app function
    def quitApplication(self):
        self.master.quit()


# create active list page
class ActiveList(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.set_fonts()  # init fonts
        self.create_widgets()  # init widgets

    # define page fonts
    def set_fonts(self):
        self.titleFont = Font(weight="bold", size=20)

    # define page widgets
    def create_widgets(self):
        # main window
        self.mainFrame = ttk.Frame(self, padding=10)
        self.mainFrame.grid()

        # menu/nav button
        self.menuButton = tk.Menubutton(
            self.mainFrame, text="Menu", relief=RAISED, width=3
        )
        self.menuButton.grid(row=0, column=0)
        self.menuButton.menu = tk.Menu(self.menuButton, tearoff=0)
        self.menuButton["menu"] = self.menuButton.menu
        self.mainPage = tk.IntVar()
        self.allLists = tk.IntVar()
        self.menuButton.menu.add_checkbutton(label="Home", variable=self.mainPage)
        self.menuButton.menu.add_checkbutton(label="All Lists", variable=self.allLists)

        # page title
        self.pageTitle = ttk.Label(self.mainFrame, text="Active List")
        self.pageTitle.grid(row=1, column=1)
        self.pageTitle["font"] = self.titleFont

        # quit button
        self.quitButton = ttk.Button(
            self.mainFrame, text="Quit", command=self.quitApplication, width=3
        )
        self.quitButton.grid(row=0, column=2)

    # quit app function
    def quitApplication(self):
        self.master.quit()
    
    def toHome():
        pass


# create main application
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Shopping Manager")
        self.homePage = MainPage(self)
        self.homePage.grid()


# call main
if __name__ == "__main__":
    app = Application()
    app.resizable(width=False, height=False)
    app.mainloop()
