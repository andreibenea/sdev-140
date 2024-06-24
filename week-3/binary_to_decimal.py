"""
This program converts a binary string to its decimal value
"""

binary_string = input("Type in a string of bits: ")
decimal = 0
exponent = len(binary_string) - 1

for each in binary_string:
    decimal = decimal + int(each) * 2 ** exponent
    exponent = exponent - 1

print(decimal)