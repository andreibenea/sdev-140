"""
Author: Andrei Benea
Date written: 6/20/24
Assignment: M03 Programming Assignment Part 2
This program writes a series of random numbers to a file while
also displaying all those numbers in the console. Each random
number will be in the range of 1 through 500. The program will
first ask the user how many numbers the file should contain,
then it will prompt for the name of the file to store those numbers in.
"""

import random  # import module for random number generation


def setLimit():
    while True:  # loop to ensure input is valid
        limit = input("Type in how many numbers should be generated: ")
        if limit.isnumeric():  # check for numeric input
            for i in range(len(limit)):  # loop checking each digit for starting zeroes
                if limit[i] != "0":
                    result = limit[i::]  # new string starts at first position not zero
                    return result
            return "0"  # if only zeroes, returns single zero
        print("Invalid input. Please try again!")


def generateNumbers(times):
    result = ""  # initialize recepient string as empty
    for i in range(int(times)):  # loop through each character/digit
        random_number = random.randrange(1, 500)  # generate number on each iteration
        print(random_number)  # print number to console
        result += str(random_number) + " "  # add each generated number to result string
    return result


def writeToFile():
    if int(limit) > 0: # if zero numbers, file not generated
        fileName = input(
            "Type in the receiving file name (incl. path): "
        )  # prompts user for file name (path optional)
        file = open(f"{fileName}.txt", "a")  # open file in "append" mode
        file.write(
            f"{generateNumbers(limit)}\n"
        )  # write values returned by function to file
        file.close()  # close file after processing


limit = setLimit()  # store returned value inside variable

writeToFile()  # start program
