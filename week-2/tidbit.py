"""
Author: Andrei Benea
Date written: 6/5/24
Assignment: M02 Practice Programming Exercise 3-10
This program calculates various values resulting from purchasing
an item on credit. At an annual interest rate of 12%, a down payment
of 10% and monthly payments of 5% of the listed purchase price,
minus the down payment, the program takes the purchase price as
input. After processing the values, it displays them in tabular
format with corresponding headers.
"""

ANNUAL_RATE = 0.12  # annual constant
MONTHLY_RATE = ANNUAL_RATE / 12  # monthly constant
DOWNPAYMENT_RATE = 0.10  # downpayment constant
TABLEFORMATSTRING = (
    "%2d%15.2f%15.2f%17.2f%17.2f%17.2f"  # used to format table correctly
)

fltPurchasePrice = float(
    input("Type in purchase price: ")
)  # stores purchase price as float

monthlyPayment = 0.05 * fltPurchasePrice  # calculate monthly payment

month = 1  # initialize months to "1"
balance = fltPurchasePrice - (fltPurchasePrice * DOWNPAYMENT_RATE)  # calculate balance

print(
    "Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance"
)  # print table header

while balance > 0:  # loop that prints rows for each month until balance reaches 0
    if monthlyPayment > balance:
        monthlyPayment = balance
        interest = 0
    else:
        interest = balance * MONTHLY_RATE
    principal = monthlyPayment - interest
    remaining = balance - monthlyPayment

    print(
        TABLEFORMATSTRING
        % (month, balance, interest, principal, monthlyPayment, remaining)
    )  # prints row as per format string

    balance = remaining
    month += 1  # increment month to create new row