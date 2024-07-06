"""
Author: Andrei Benea
Date written: 7/6/24
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

# import modules (used easyframe for learning purposes)
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font


# define class
class TemperatureConverter(EasyFrame):
    def __init__(self):  # define init function
        EasyFrame.__init__(self, title="Temperature Converter")  # instantiate window
        self.setResizable(False)  # set fixed window size
        font = Font(weight="bold")  # set font variable
        title = self.addLabel(
            text="Temperature Converter", row=0, column=1, sticky="N"
        )  # set title
        title["font"] = font  # apply font to title
        self.valueField = self.addFloatField(
            0.0, row=2, column=1, precision=2, sticky="EW"
        )  # add input field
        self.celsiusButton = self.addButton(
            text="Celsius", row=1, column=2, command=self.convert_to_celsius
        )  # add convert to Celsius button
        self.fahrenheitButton = self.addButton(
            text="Fahrenheit", row=2, column=2, command=self.convert_to_fahrenheit
        )  # add convert to Fahrtenheit button
        self.addLabel(
            text="Type in value below\nthen click either buttons to convert",
            row=1,
            column=1,
            sticky="S",
        )  # add info message
        imageLabel = self.addLabel(
            text="thermometer", row=0, rowspan=3, column=0, sticky="NSEW"
        )  # add image container
        self.image = PhotoImage(file="week-6/thermometer_sm.gif")  # add image
        imageLabel["image"] = self.image  # add image to container

    def convert_to_celsius(self):
        value = self.valueField.getNumber()  # get input value
        result = 5 / 9 * (value - 32)  # calculate Celsius value based on existing input
        self.valueField.setNumber(result)  # display result

    def convert_to_fahrenheit(self):
        value = self.valueField.getNumber()  # get input value
        result = (
            9 / 5 * value + 32
        )  # calculate Fahrenheit value based on existing input
        self.valueField.setNumber(result)  # display result


def main():
    TemperatureConverter().mainloop()  # start mainloop


# call main
if __name__ == "__main__":
    main()
