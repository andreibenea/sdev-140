"""
Author: Andrei Benea
Date written: 7/7/24
Assignment: M07 Programming Assignment Part 2
This program creates an object of the ProductionWorker class and
prompts the user to enter data for each of the object's data attributes.
It stores the data in the object and then uses the object's accessor methods
to retrieve it and display it on the screen.
"""


# create employee class
class Employee:
    num_of_employees = 0

    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
        self.fullname = first + " " + last

        Employee.num_of_employees += 1
        self.emp_number = Employee.num_of_employees

    def getName(self):
        return self.fullname

    def getEmployeeNumber(self):
        return self.emp_number

    def __str__(self) -> str:
        return (
            "Full Name: "
            + self.fullname
            + "\nEmp. Nr.: "
            + "{}".format(self.emp_number).zfill(4)
        )


# create production worker sub-class
class ProductionWorker(Employee):
    def __init__(self, first, last, hourly_pay_rate, shift_number) -> None:
        super().__init__(first, last)
        self.hourly_pay_rate = hourly_pay_rate
        self.shift_number = shift_number

    def getRatePerHour(self):
        return self.hourly_pay_rate

    def getShift(self):
        if self.shift_number == 1 or self.shift_number == None:
            return "Day"
        elif self.shift_number == 2:
            return "Night"
        else:
            return "Invalid shift number!"

    def __str__(self) -> str:
        return (
            super().__str__()
            + "\nHourly Rate: $"
            + str(self.hourly_pay_rate)
            + "\nShift: "
            + self.getShift()
        )


# create default objects (workers)
worker_one = ProductionWorker("John", "Doe", 40, 1)
worker_two = ProductionWorker("Jane", "Doe", 50, 2)

# print default objects (workers)
print(worker_one, "\n")
print(worker_two, "\n")


# define main function
def main():
    first_name = input("Type in the employee's first name: ")
    last_name = input("Type in the employee's last name: ")
    pay_rate = requestPayRate()
    shift = requestShiftInfo()

    worker_three = ProductionWorker(first_name, last_name, pay_rate, shift)

    print(f"\n{worker_three}", "\n")


# define pay rate input function
def requestPayRate():
    while True:
        pay_rate = input("Type in hourly rate: $")
        if pay_rate.isnumeric():
            if int(pay_rate) > 0:
                return int(pay_rate)
            else:
                print("Invalid input. Please try again!")
        else:
            print("Invalid input. Please try again!")


# define shift info input function
def requestShiftInfo():
    while True:
        shift = input(
            "Type in the employee's shift code (1 for day, 2 for night or leave blank if unknown): "
        )
        if shift == "1" or shift == "2":
            return int(shift)
        elif shift == "":
            return None
        else:
            print("Invalid input. Please try again!")


# call main
if __name__ == "__main__":
    main()
