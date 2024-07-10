"""
Author: Andrei Benea
Date written: 7/7/24
Assignment: M07 Programming Assignment Part 1
This program is an example of using a class and sub-class.
"""


# create person class
class Person:
    # define class methods (constructor)
    def __init__(self, name, address, phone_number) -> None:
        self.name = name
        self.address = address
        self.phone_number = phone_number

    # define class methods
    def getName(self):
        return self.name

    # define class methods
    def getAddress(self):
        return self.address

    # define class methods
    def getPhoneNumber(self):
        return self.phone_number

    # define class methods
    def __str__(self) -> str:
        return (
            "Name: "
            + self.name
            + "\nAddress: "
            + self.address
            + "\nPhone Nr.: "
            + self.phone_number
        )


# create customer sub-class
class Customer(Person):
    # define class methods (constructor)
    def __init__(
        self, name, address, phone_number, customer_number, wants_mailing_list
    ) -> None:
        super().__init__(name, address, phone_number)
        self.customer_number = customer_number
        self.wants_mailing_list = wants_mailing_list

    # define class methods
    def getCustomerNr(self):
        return self.customer_number

    # define class methods
    def determineMailingList(self):
        return self.wants_mailing_list

    # define class methods
    def __str__(self) -> str:
        return (
            super().__str__()
            + "\nCustomer Nr.: "
            + str(self.customer_number)
            + "\nMailing List: "
            + str(self.wants_mailing_list)
        )


# create object based on customer class
person_one = Customer("John Doe", "New York, NY", "(123) 456 7890", 1, True)


# define main
def main():
    # print object method
    print(person_one.getName())
    # print object
    print(person_one)


# call main
if __name__ == "__main__":
    main()
