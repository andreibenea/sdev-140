"""
Author: Andrei Benea
Date written: 6/22/24
Assignment: M04 Programming Assignment Part 2
This program returns the top 3 items with the highest
prices from a provided shop (dataset).
    Sample data: {'Apple': 0.50, 'Banana': 0.20, 'Mango': 0.99, \
        'Coconut': 2.99, 'Pineapple': 3.99}
    Expected Output:
    Pineapple 3.99
    Coconut 2.99
    Mango 0.99
"""

# created mock data for testing
mock_data = {
    "Apple": 0.50,
    "Banana": 0.20,
    "Mango": 0.99,
    "Coconut": 2.99,
    "Pineapple": 3.99,
}

# created mock data for testing
mock_data2 = {
    "Onion": 1.50,
    "Cucumber": 4.20,
    "Potato": 0.99,
    "Cabbage": 2.99,
    "Tomato": 3.99,
}

# created mock data for testing
mock_data3 = {
    "Hammer": 0.20,
    "Nails": 0.10,
    "Wood": 2.99,
    "Brick": 5.99,
    "Stone": 1.45,
}


def sortItems(
    data,
):  # function that returns a sorted dictionary after processing received data
    sortedData = {}
    for key in sorted(data, key=data.get, reverse=True):
        sortedData[key] = data[key]
    return sortedData


def printResults(
    data,
):  # function that loops through a sorted dictionary and returns the first 3 item pairs
    i = 0
    for key in data:
        print(key, data[key])
        i += 1
        if i == 3:
            break


sorted_items = sortItems(mock_data)  # store returned value in variable
sorted_items2 = sortItems(mock_data2)  # store returned value in variable
sorted_items3 = sortItems(mock_data3)  # store returned value in variable

# testing three different scenarios in a single run
printResults(sorted_items)  # print value
print("")  # print blank for readability
printResults(sorted_items2)  # print value
print("")  # print blank for readability
printResults(sorted_items3)  # print value
