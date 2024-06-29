"""
Author: Andrei Benea
Date written: 6/23/24
Assignment: M05 Practice Programming Exercise 6-6
This program will act like the standard range() function
but will return a list instead of a class.
"""


def myRange(
    stop, start: int = 0, step: int = 1
):  # define function parameters (default first, then optional with default values)
    my_list = []  # initialize empty list
    if step > 0:  # count up case
        i = start  # initialize counter to start
        while i < stop:  # set stop condition
            my_list.append(int(i))  # populate list
            i += step  # increment counter
        return my_list
    else:  # count down case
        i = start  # initialize counter to start
        while i > stop:  # set stop condition
            my_list.append(int(i))  # populate list
            i += step  # increment counter
        return my_list

print("Custom myRange function output below:") # display results of custom function
print(myRange(10))
print(myRange(10, 1))
print(myRange(10, 1, 2))
print(myRange(1, 10, -1))
print(myRange(10, 1, -1))
print("\nStandard range function output (as list) below:") # display results of built-in range function for comparison
print(list(range(10)))
print(list(range(1, 10)))
print(list(range(1, 10, 2)))
print(list(range(10, 1, -1)))
print(list(range(1, 10, -1)))
