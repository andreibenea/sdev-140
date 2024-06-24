"""
Author: Andrei Benea
Date written: 6/5/2024
Assignment: Module 01 Programming Assignment Part 2
This program calculates the total cost of a meal at a restaurant.
It starts by prompting the user to type in the cost of the meal (initial_cost[float]),
then adds to that an 18% tip plus a 7% sales tax. Resulting amounts and the 
total cost are displayed as floating point numbers with two decimal points.
"""

STATE_TAX = 0.07  # tax constant

while True:  # Loop to ensure number entered by user is positive
    initial_cost = float(input("Type in the cost of the meal: "))
    if initial_cost < 0:
        print("Please enter a positive amount.")
        continue
    if initial_cost >= 0:
        break

tip = initial_cost * 0.18  # calculates tip amount

tax = (initial_cost + tip) * STATE_TAX  # calculates tax amount

total = initial_cost + tip + tax  # calculates total cost

print(f"Initial cost is ${initial_cost:.2f}")  # displays initial cost
print(f"18% tip is ${tip:.2f}")  # displays tip amount
print(f"7% tax is ${tax:.2f}")  # displays tax amount
print(f"Your total cost is ${total:.2f}")  # displays total cost