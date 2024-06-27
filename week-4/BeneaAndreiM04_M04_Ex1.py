"""
Author: Andrei Benea
Date written: 6/22/24
Assignment: M04 Programming Assignment Part 1
This program prompts the user to enter an integer number greater
than 1, then displays all the prime numbers that are less or
equal to the number provided.
A positive integer greater than 1 is prime if it has no divisors
other than 1 and itself. A positive integer greater than 1 is
composite if not prime.
    After a number was provided, the program should populate a
    list with all of the integers from 2 up through the value
    provided.
    The program should then loop through the list. The loop
    should pass each element to a function that displays the
    element if it is a prime number.
"""


def getInput():  # loop to ensure input is numeric and greater than 1
    while True:
        userInput = input("Type in a number whole number greater than 1: ")
        if userInput.isnumeric():
            if int(userInput) > 1:
                return userInput
        print("Invalid input. Please try again!")


def cleanUpInput():  # remove any leading zeroes
    for i in range(len(user_input)):
        if user_input[i] != "0":
            result = user_input[i::]
            return result


def createRangeList():  # create list of integers from 2 up to number provided
    integerList = []
    for i in range(2, int(user_input_clean) + 1):
        integerList.append(i)
    return integerList


def isPrime(number):  # function that returns true if number is prime
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def loopThroughList():  # loop through list, printing prime numbers
    for each in list_of_integers:
        if isPrime(each):
            print(f"This is a PRIME number: {each}")


user_input = getInput()  # store returned value in variable
user_input_clean = cleanUpInput()  # store returned value in variable
list_of_integers = createRangeList()  # store returned value in variable
loopThroughList()  # call loop function
