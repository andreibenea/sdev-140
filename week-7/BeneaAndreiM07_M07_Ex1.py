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

    def __str__(self) -> str:
        return (
            "Name: "
            + self.name
            + "\nAddress: "
            + self.address
            + "\nPhone Nr.: "
            + self.phone_number
        )


class Customer(Person):
    def __init__(
        self, name, address, phone_number, customer_number, wants_mailing_list
    ) -> None:
        super().__init__(name, address, phone_number)
        self.customer_number = customer_number
        self.wants_mailing_list = wants_mailing_list

    def getCustomerNr(self):
        return self.customer_number

    def determineMailingList(self):
        return self.wants_mailing_list

    def __str__(self) -> str:
        return (
            super().__str__()
            + "\nCustomer Nr.: "
            + str(self.customer_number)
            + "\nMailing List: "
            + str(self.wants_mailing_list)
        )


person_one = Customer("John Doe", "New York, NY", "(123) 456 7890", 1, True)

print(person_one)
