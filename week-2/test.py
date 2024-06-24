"""
Author: Andrei Benea
Date written: 6/6/24
Assignment: M02 Programming Assignment Part 1
This program prompts the user to type in the names of two of
the primary colors. If the input is anything but a primary color, 
an error message will be displayed. Otherwise, the program will
display the name of the secondaryh color that results from mixing
the two primary ones.
Mixing red and blue, results in purple.
Mixing red and yellow, results in orange.
Mixing blue and yellow, results in green.
"""


def getInputs():
    while True:  # loop to ensure correct primary color input
        firstColor = input("Type in a primary color name: ")
        firstColor = (
            firstColor.lower()
        )  # convert to lower case for readability and easier matching
        if firstColor == "red":
            break
        elif firstColor == "blue":
            break
        elif firstColor == "yellow":
            break
        else:
            print("Invalid input! Primary colors are: red, blue and yellow.")

    while True:  # loop to ensure correct primary color input
        secondColor = input("Type in another primary color name: ")
        secondColor = (
            secondColor.lower()
        )  # convert to lower case for readability and easier matching
        if secondColor == "red":
            break
        elif secondColor == "blue":
            break
        elif secondColor == "yellow":
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

# old code with list below
"""

colors = []  # initialize empty list


def getInputs():
    while True:  # loop to ensure correct primary color input
        firstColor = input("Type in a primary color name: ")
        firstColor = (
            firstColor.lower()
        )  # convert to lower case for readability and easier matching
        if firstColor == "red":
            colors.append(firstColor)
            break
        elif firstColor == "blue":
            colors.append(firstColor)
            break
        elif firstColor == "yellow":
            colors.append(firstColor)
            break
        else:
            print("Invalid input! Primary colors are: red, blue and yellow.")

    while True:  # loop to ensure correct primary color input
        secondColor = input("Type in another primary color name: ")
        secondColor = (
            secondColor.lower()
        )  # convert to lower case for readability and easier matching
        if secondColor == "red":
            colors.append(secondColor)
            break
        elif secondColor == "blue":
            colors.append(secondColor)
            break
        elif secondColor == "yellow":
            colors.append(secondColor)
            break
        else:
            print("Invalid input! Primary colors are: red, blue and yellow.")


def mixColors():
    getInputs()  # call function to get needed input values
    if colors[0] == colors[1]:  # case for colors being the same
        print(f"Resulting mixture is: {colors[0]}.")
    else:
        match colors[0], colors[1]:  # case structure for better readability
            case "red", "blue":
                print("Resulting mixture is purple")
            case "blue", "red":
                print("Resulting mixture is purple")
            case "red", "yellow":
                print("Resulting mixture is orange")
            case "yellow", "red":
                print("Resulting mixture is orange")
            case "blue", "yellow":
                print("Resulting mixture is green")
            case "yellow", "blue":
                print("Resulting mixture is green")


mixColors()  # call function to start mixing program
"""