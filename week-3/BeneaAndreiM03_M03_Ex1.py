"""
Author: Andrei Benea
Date written: 6/15/24
Assignment: M03 Programming Assignment Part 1
This program prompts the user to enter a series of single-digit
numbers with nothing separating them. The program then displays
the sum of all the single-digit numbers in the provided string.
For example, if the user enters 2514, the method should return 12,
which is the sum of 2, 5, 1, and 4.
"""


def getInput():
    while True:  # loop to ensure input is valid
        user_input = input("Type in a series of single-digit numbers (e.g. 4526): ")
        if user_input.isnumeric():  # check for numeric input
            for i in range(
                len(user_input)
            ):  # loop checking each digit for starting zeroes
                if user_input[i] != "0":
                    result = user_input[
                        i::
                    ]  # new string starts at first position not zero
                    return result
            return "0"  # if only zeroes, returns single zero
        print("Invalid input. Please try again!")


user_input = getInput()  # store returned value inside variable


def calculateSum():
    sum = 0  # initialize accumulator
    for char in user_input:  # loop through each character/digit
        sum += int(char)  # add each value to accumulator
    return sum


print(
    f"The sum of all the single-digit numbers in the provided string is: {calculateSum()}"
)  # display result
