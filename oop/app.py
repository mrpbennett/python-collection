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

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

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
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # allows to inherit args from the parent
        self.prog_lang = prog_lang


""" Manager Class - inherits from Employee """


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("---> ", emp.fullname())


# create an instance of Employee
emp_1 = Employee("Paul", "Bennett", 60000)
print(emp_1)

# prints full name from the instance
fullname = emp_1.fullname()
print(fullname)

# applys a 4% raise from the apply_raise method
emp_1.apply_rasie()
print(f"£{emp_1.pay}")

# creating a new emp from a string
emp_str = "Fiona-Bennett-50000"
emp_2 = Employee.from_string(emp_str)
print(emp_2.fullname())

# outputs number of Employee instances
print(f"Our company has {Employee.num_of_emps} members of staff.")

# outputs to see if today is a work day
my_date = datetime.date.today()
print(Employee.is_workday(my_date))

print("----- DEVELOPERS ------")

dev_1 = Developer("Paul", "Bennett", 120000, "python, javascript")
dev_2 = Developer("Chalie", "Pup", 10, "pug")

print(dev_1.email)
print(dev_1.prog_lang)


print("----- Manager ------")

mgr_1 = Manager("Fiona", "Bennett", 90000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

