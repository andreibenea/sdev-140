"""
Program: textanalysis.py
Author: Ken (v1.0), Andrei Benea (v2.0; 6/20/24)
Assignment: M03 Practice Exercise - Debugging
Computes and displays the Flesch Index and the Grade
Level Equivalent for the readability of a text file.
"""

import os  # import module for checking file path

# Take the inputs
fileName = input("Enter the file name: ")
if os.path.isfile(f"{fileName}.txt") == False:  # check for path before accessing file
    print(
        "Invalid filename or path. Please check your input and try again!"
    )  # display message if path/name incorrect
else:
    inputFile = open(f"{fileName}.txt", "r")
    text = inputFile.read()

    # Count the sentences
    sentences = (
        text.count(".")
        + text.count("?")
        + text.count(":")
        + text.count(";")
        + text.count("!")
    )

    # Count the words
    words = len(text.split())

    # Count the syllables
    syllables = 0
    vowels = "aeiouAEIOU"
    for word in text.split():
        previous_letter_is_vowel = False  # initialize flag for duplicate vowel check
        for letter in word:  # loop through each letter
            if (
                letter in vowels and previous_letter_is_vowel == False
            ):  # check if letter is vowel and if previous letter is not
                syllables += 1  # increase syllable count by 1
                previous_letter_is_vowel = True  # set flag to true
            else:
                previous_letter_is_vowel = False  # set flag to false
        for ending in ["es", "ed", "e"]:
            if word.endswith(ending):
                syllables -= 1
        if word.endswith("le"):
            syllables += 1

    # Compute the Flesch Index and Grade Level
    index = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
    level = int(round(0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59))

    # Output the results
    print("The Flesch Index is", index)
    print("The Grade Level Equivalent is", level)
    print(sentences, "sentences")
    print(words, "words")
    print(syllables, "syllables")
