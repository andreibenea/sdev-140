"""
Author: Andrei Benea
Date written: 6/5/24
Assignment: M02 Practice Programming Exercise 3-9
This program continuously prompts the user for numbers which it
then adds to an accumulator. If the user presses the "Enter" key
without also having typed in a value, the program ends with displaying
the sum of all previously provided numbers and their average.
"""

theSum = 0  # initialized accumulator
count = 0  # initialized counter

while True: # loop to ensure continuous input of numbers
    user_input = input("Type in a number or press Enter to quit: ")
    if user_input == "": # break condition is an empty string
        break
    else: # if number is provided, it is added to accumulator and count is increased by 1
        theSum += float(user_input)
        count += 1

print("The sum is", theSum) # prints out the value stored in the accumulator
if count > 0:
    print("The average is", theSum / count) # prints out the average if any numbers were provided