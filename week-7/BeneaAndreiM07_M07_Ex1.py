"""
Author: Andrei Benea
Date written: 7/6/24
Assignment: M07 Programming Assignment Part 1
This program is an example of using a class and sub-class.
"""


class Person:
    def __init__(self, name, address, phone_number) -> None:
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getPhoneNumber(self):
        return self.phone_number


class Customer(Person):
    def __init__(self, customer_number, wants_mailing_list) -> None:
        self.customer_number = customer_number
        self.wants_mailing_list = wants_mailing_list

    def getCustomerNumber(self):
        return self.customer_number

    def getWantsMailingList(self):
        return self.wants_mailing_list


customer_one = Customer()
