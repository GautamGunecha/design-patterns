# Python Object Oriented Programming

# class
"""
class - It can be defined as collection of objects.
Example - An employee class. It contains an attributes and methods, i.e. an email id, name, age, salary, designation etc.
"""

# object
"""
object - An entity that has state and behavior.
When we define a class it needs to create an object to allocate memory. 
"""

# class variables
"""
Variables that are shared among all instances of the class.
"""

# class method
"""
A class method in Python is a method that is bound to the class, not the instance of the class.
It can access and modify the class state using the cls parameter (which refers to the class itself). 
Class methods are defined using the @classmethod decorator. 
"""

# static methods
"""
A staticmethod in Python is a method that belongs to a class but does not have access to the class (cls) or instance (self) itself. 
It is defined using the @staticmethod decorator.
Unlike instance methods and class methods, a static method is more like a regular function that is part of the class namespace.
It cannot modify or access the class or instances state and is typically used to define utility functions related to the class.
"""

import datetime

class Employee:
  number_of_employee = 0
  raise_amount = 1.20

  def __init__(self, name, designation, pay):
    self.name = name
    self.designation = designation
    self.pay = pay

    Employee.number_of_employee += 1
  
  def apply_raise(self):
    self.pay = float(self.pay * self.raise_amount)
    return self.pay

  @classmethod
  def set_raise_amount(cls, amount):
    cls.raise_amount = amount

  @classmethod
  def from_string(cls, employee_string):
    name, designation, pay = employee_string.split("-")
    return cls(name, designation, pay)
  
  @staticmethod
  def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
      return False
    return True

# Inheritance

"""
Inheritance allowed us to inherit attributes and method from parent class.
"""

class Developer(Employee):
  raise_amount = 1.30

  def __init__(self, name, designation, pay, prog_lang):
    super().__init__(name, designation, pay)
    self.prog_lang = prog_lang

# developer_one = Developer('Test', 'Software Developer Engineer', 50000, 'Python')
# developer_two = Developer('Case', 'UI/UX Developer', 45000, 'Javascript')

class Manager(Employee):
  def __init__(self, name, designation, pay, employees = None):
    super().__init__(name, designation, pay)
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

  def print_emp(self):
    for emp in self.employees:
      print("---- >", emp.name)

dev_one = Developer('Test', 'Software Developer Engineer', 50000, 'Python')
dev_two = Developer('Case', 'Software Developer Engineer', 50000, 'Javascript')

manager_one = Manager('Jon Snow', 'Senior Engineer', 90000, [dev_one, dev_two])
