"""
Author: Andrei Benea
Date written: 6/29/24
Assignment: M06 Practice Programming Exercise 9-5
This program uses a GUI to allow the user to type in a temperature value
inside an input field. This value can represent either degrees Celsius or 
degrees Fahrenheit. Two additional buttons will allow the user to trigger
the conversion of the previously typed in value in the desired counterpart:
degrees C or F.
The program uses the following formula to make the conversion:
F = 9/5 * C + 32
F is the Fahrenheit temperature, and C is the Celsius temperature.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font


class TemperatureConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")
        self.setResizable(False)
        self.addLabel(text="Temperature Converter", row=0, column=1, sticky="N")
        self.addFloatField(0, row=1, column=1, precision=2, sticky="NSEW").setNumber(
            0.00
        )
        self.addButton(text="Celsius", row=1, column=0)
        self.addButton(text="Fahrenheit", row=1, column=2)
        self.addLabel(
            text="Type in value above, then click either buttons to convert",
            row=2,
            column=1,
            sticky="S",
        )


def main():
    TemperatureConverter().mainloop()


if __name__ == "__main__":
    main()
