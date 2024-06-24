"""
Author: Andrei Benea
Date written: 6/22/24
Assignment: M04 Practice Programming Exercise 5-8
This program prompts the user for a file name. It then proceeds to
process that file extracting unique words, sorts them alphabetically
and finally prints them, and their frequency, in the console.
"""

import os  # import module for checking file path


def getFileName():
    fileName = input("Enter the input file name: ")  # prompt user for file name
    return fileName


def checkFilePathExists(file):
    if os.path.isfile(file) == False:  # check for path before accessing file
        print(
            "Invalid filename or path. Please check your input and try again!"
        )  # display message if path/name is wrong
        dir_list = os.listdir(
            os.getcwd()
        )  # store folders and files of current working directory
        print(
            f"The current working directory contains the following:\n{dir_list}"
        )  # print contents of current working directory
        return False
    else:
        return True


def readFile():
    if checkFilePathExists(name_of_file):  # check for path before accessing file
        inputFile = open(f"{name_of_file}", "r")  # open file in read mode
        fileContents = inputFile.read()  # read file
        return fileContents


def processUniques():
    if os.path.isfile(name_of_file):  # check for path
        uniqueWords = {}  # initialize empty dictionary
        for word in text.split():  # loop through each word from file
            frequency = text.split().count(
                word
            )  # set frequency to how many occurences found
            uniqueWords.update(
                {word: frequency}
            )  # add word and frequency to dictionary
        sortedKeys = sorted(uniqueWords.keys())  # sort dictionary keys
        return sortedKeys, uniqueWords
    else:
        return None, None  # return tuple of None to prevent error


def printResults():
    if os.path.isfile(name_of_file):  # check for path
        for each in sorted_keys:
            print(
                f"{each}: {unique_words[each]}"
            )  # loop through each word from sorted list and print


name_of_file = getFileName()  # store file name
text = readFile()  # store text
sorted_keys, unique_words = (
    processUniques()
)  # store sorted dictionary keys and dictionary
printResults()  # print results
