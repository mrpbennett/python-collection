import datetime

""" Python OOP - I will crack classes if it kills me """


class Employee:

    # class variables are avaiable through out the whole class with self.
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com".lower()

        Employee.num_of_emps += 1

    # method to create full name
    def fullname(self):
        return f"{self.first} {self.last}"

    # method to apply a raise to pay
    def apply_rasie(self):

        self.pay = int(self.pay * self.raise_amount)

    # sets raise amount for the whole class
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # creates an emp from a string eg: Fiona-Bennett-50000
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    # checks if day is a work day
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


""" Developer Class - inherits from Employee """


class Developer(Employee):
    pass


# create an instance of Employee
emp_1 = Employee("Paul", "Bennett", 60000)
print(emp_1.email)

# prints full name from the instance
fullname = emp_1.fullname()
print(fullname)

# applys a 4% raise from the apply_raise method
emp_1.apply_rasie()
print(emp_1.pay)

# creating a new emp from a string
emp_str = "Fiona-Bennett-50000"
emp_2 = Employee.from_string(emp_str)
print(emp_2.fullname())

# outputs number of Employee instances
print(f"Our company has {Employee.num_of_emps} members of staff.")

# outputs to see if today is a work day
my_date = datetime.date.today()
print(Employee.is_workday(my_date))
