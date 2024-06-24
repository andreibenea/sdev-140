"""
Author: Andrei Benea
Date written: 6/13/24
Assignment: M02 Programming Assignment Part 1
This program prompts the user to type in the names of two of
the primary colors. If the input is anything but a primary color, 
an error message will be displayed. Otherwise, the program will
display the name of the secondary color that results from mixing
the two primary ones.
Mixing red and blue, results in purple.
Mixing red and yellow, results in orange.
Mixing blue and yellow, results in green.
"""


def getInputs():
    while True:  # loop to ensure correct primary color input
        firstColor = input("Type in a primary color name: ")
        firstColor = firstColor.lower()  # convert to lower case for easier matching
        if firstColor == "red":  # loop exit condition
            break
        elif firstColor == "blue":  # loop exit condition
            break
        elif firstColor == "yellow":  # loop exit condition
            break
        else:
            print("Invalid input! Primary colors are: red, blue and yellow.")

    while True:  # loop to ensure correct primary color input
        secondColor = input("Type in another primary color name: ")
        secondColor = secondColor.lower()  # convert to lower case for easier matching
        if secondColor == "red":  # loop exit condition
            break
        elif secondColor == "blue":  # loop exit condition
            break
        elif secondColor == "yellow":  # loop exit condition
            break
        else:
            print("Invalid input! Primary colors are: red, blue and yellow.")
    return firstColor, secondColor


firstColor, secondColor = getInputs()  # store returned values in separate variables


def mixColors(firstColor, secondColor):
    if firstColor == secondColor:  # case for colors being the same
        print(f"Resulting mixture is: {firstColor}.")
    else:
        match firstColor, secondColor:  # case structure for better readability
            case "red", "blue":
                print("Resulting mixture is purple.")
            case "blue", "red":
                print("Resulting mixture is purple.")
            case "red", "yellow":
                print("Resulting mixture is orange.")
            case "yellow", "red":
                print("Resulting mixture is orange.")
            case "blue", "yellow":
                print("Resulting mixture is green.")
            case "yellow", "blue":
                print("Resulting mixture is green.")


mixColors(
    firstColor, secondColor
)  # call function while passing values to start mixing program