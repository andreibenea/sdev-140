"""
Author: Andrei Benea
Date written: 6/13/24
Assignment: M02 Programming Assignment Part 2
This program prompts the user to type in a number (num[int]), checks
the number to be greater than zero, and then calculates the factorial
of that number.
In mathematics, a number's factorial is the product of all the non-negative
(integer) numbers from 1 to the number in question (e.g. 4! = 1*2*3*4 = 24)
"""


def getNumber():
    while True:  # loop to ensure input is a number and higher than 0
        num = input("Type in a number greater than 0: ")
        if num.isnumeric():  # == True:  # check if input is numeric
            # break
            if int(num) > 0:  # convert input to int then compare
                break  # exit loop / input is valid
        else:
            continue
    return num


myNumber = getNumber()  # store returned value in a variable


def calculateFactorial():
    factorial = 1  # initialize base / starting point number
    for i in range(1, int(myNumber) + 1):
        factorial *= i  # loop to multiply each number in range with starting point
    return f"Factorial of provided number is: {factorial}"


print(
    calculateFactorial()
)  # call function inside print statement (instead of storing in another variable)
