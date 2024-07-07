# import modules
from tkinter import *
from tkinter import ttk
import tkinter as tk

# create widgets
root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()


# define functions
def main():
    root.mainloop()


# create labels
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

# create buttons
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# call main
if __name__ == "__main__":
    main()
