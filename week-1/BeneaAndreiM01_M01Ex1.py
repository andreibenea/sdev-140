"""
Author: Andrei Benea
Date written: 6/5/2024
Assignment: Module 01 Programming Assignment Part 1
This program prompts the user for a number (celsius[float]) representing
temperature in degrees Celsius. It then converts that input to degrees
Fahrenheit (fahrenheit[float]) and displays the result as an integer.
"""

celsius = float(
    input("Type in a number representing degrees Celsius: ")
)  # gets user input and transforms to float

fahrenheit = 9 / 5 * celsius + 32  # converts from celsius to fahrenheit

print(
    "Provided temperature in degrees Fahrenheit is", int(fahrenheit)
)  # prints conversion result as int