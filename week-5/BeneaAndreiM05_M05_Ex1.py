"""
Author: Andrei Benea
Date written: 6/23/24
Assignment: M05 Programming Assignment Part 1
This program prompts the user for total monthly sales.
It then proceeds to calculate the amount of county sales tax,
state sales tax and total sales tax (county + state).
"""

import re # import regex module for proper input validation

COUNTY_TAX_RATE = 0.025  # county tax rate constant
STATE_TAX_RATE = 0.05  # state tax rate constant


def get_monthly_sales():  
    while True: # loop to ensure input is valid
        result = input("Type in monthly sales amount: $")
        if result.isalpha() or result == "": # check for alpha or empty string
            print("Invalid input. Please try again!")
            continue
        reg = re.search("[^.\\s\\d][\\\\^]?", result) # define regex
        if reg: # check regex match
            print("Invalid input. Please try again!")
            continue
        return result


def clean_up_input(data):  # remove any leading zeroes
    for i in range(len(data)):
        if data[i] != "0":
            result = data[i::] # return new string from first non-zero character
            return result
    return "0" # return 0 if only 0


def calculate_county_tax(data):  # calculate county tax amount
    tax_amount = float(data) * COUNTY_TAX_RATE
    return tax_amount


def calculate_state_tax(data):  # calculate state tax amount
    tax_amount = float(data) * STATE_TAX_RATE
    return tax_amount


def calculate_total_tax(data, data_two):  # calculate total tax amount
    total_tax_amount = data + data_two
    return total_tax_amount


monthly_sales = clean_up_input(get_monthly_sales())  # store input

print(
    f"County tax amount: ${calculate_county_tax(monthly_sales):.2f}"
)  # display county tax amount
print(
    f"State tax amount: ${calculate_state_tax(monthly_sales):.2f}"
)  # display state tax amount
print(
    f"Total tax amount: ${calculate_total_tax(
        calculate_county_tax(monthly_sales), calculate_state_tax(monthly_sales)
    ):.2f}"
)  # display total tax amount
