"""
Program OverridingClassMethodsAssignment.py

Author: Greg Wilhelm

Last date modified: 4/13/2020

The purpose of this program is to display the employee name, start date of their job, and their salary or hourly wage.
The Employee base class contains data members relative to the employee's personal details such as name, address, and
phone number. The SalariedEmployee and HourlyEmployee derived classes inherit the Employee data members and override the
display method in the Employee class. These classes give details on their employment start date and their pay with a
method to increase the pay.

"""

import datetime


class Employee:  # Base class
    """Employee class"""

    def __init__(self, last_name, first_name, addr='', phone_num=''):
        self._last_name = last_name
        self._first_name = first_name
        self._address = addr
        self._phone_number = phone_num

    def display(self):
        newline = '\n'
        return f"{self._first_name} {self._last_name} {newline}" \
               "" if self._address == "" else f"{self._address} {newline}" \
                                              "" if self._phone_number == "" else f"{self._phone_number} {newline}"


class SalariedEmployee(Employee):  # Base class is Employee
    """SalariedEmployee derived class of Employee base class"""

    def __init__(self, last_name, first_name, start_date, salary):
        super().__init__(last_name, first_name)  # calls the base constructor
        self._start_date = start_date
        self._salary = salary

    def give_raise(self, new_salary):
        self._salary = new_salary

    def display(self):
        newline = '\n'
        return f"{super().display()}" \
               f"Start date: {self._start_date.strftime('%m-%d-%Y')} {newline}" \
               f"Salary: ${self._salary:,.0f}"


class HourlyEmployee(Employee):
    """HourlyEmployee derived class of Employee base class"""

    def __init__(self, last_name, first_name, start_date, hourly_pay):
        super().__init__(last_name, first_name)  # calls the base constructor
        self._start_date = start_date
        self._hourly_pay = hourly_pay

    def give_raise(self, new_hourly_pay):
        self._hourly_pay = new_hourly_pay

    def display(self):
        newline = '\n'
        return f"{super().display()}" \
               f"Start date: {self._start_date.strftime('%m-%d-%Y')} {newline}" \
               f"Hourly Pay: ${self._hourly_pay:.2f}"


# Driver
salaryEmp = SalariedEmployee("Wilhelm", "Greg", datetime.date.today(), 40000)
print(salaryEmp.display())
salaryEmp.give_raise(45000)
print(salaryEmp.display())
del salaryEmp

hourlyEmp = HourlyEmployee("Wilhelm", "Greg", datetime.date.today(), 10.00)
print(hourlyEmp.display())
hourlyEmp.give_raise(12.00)
print(hourlyEmp.display())
del hourlyEmp
