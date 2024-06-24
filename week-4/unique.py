"""
Author: Andrei Benea
Date written: 6/22/24
Assignment: M04 Practice Programming Exercise 5-7
This program prompts the user for a file name. It then proceeds to
process that file extracting unique words, sorts them alphabetically
and finally prints them in the console. 
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
    if checkFilePathExists(fileName):
        inputFile = open(
            f"{fileName}", "r"
        )  # open file in read mode, adding .txt extension
        fileContents = inputFile.read()  # read file / store in "text" variable
        return fileContents


def getUniques():
    if os.path.isfile(fileName):  # check for path
        uniqueWords = []  # initialize empty list
        for word in text.split():  # loop through each word from file
            if word not in uniqueWords:  # if word not found in list
                uniqueWords.append(str(word))  # add word to list
        uniqueWords.sort()
        return uniqueWords


def printResults(sorted_list):
    if os.path.isfile(fileName):  # check for path
        for each in sorted_list:
            print(each)  # loop through each word from sorted list and print


fileName = getFileName()
text = readFile()  # store file content in variable
unique_words = getUniques()  # store identified unique words in variable

printResults(unique_words)  # print results
