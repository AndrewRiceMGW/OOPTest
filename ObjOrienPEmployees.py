#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:34:10 2019

@author: andrew
"""
import datetime
class Employee:
    num_of_emps = 0
    raise_amount = 4 # 4% 
    def __init__(self, first, last, pay, yearEmp, monthEmp, dayEmp):
        #initialises employee
        self.first = first
        self.last = last
        self.pay = pay
        self.year = yearEmp
        self.month = monthEmp
        self.day = dayEmp
        #self.email = first + "." + last + "@company.com"
        self.PayRaise()
        Employee.num_of_emps += 1
        
    #   Property Decorators
    @property
    def email(self):
        print('{}.{}@company.com'.format(self.first, self.last))
        
    def PayRaise(self):
        # adds the raise_amount to the starting salary depending on the years worked
        if self.lengthEmployed() > 0:
            self.pay = self.pay + ((self.pay//100) * self.raise_amount * self.lengthEmployed()) # pay increases each year by raise
        else:
            self.pay = self.pay
    @property    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    #   Setter
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    #   Deleter
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
        
    def StartDate(self):
         Start = datetime.datetime(self.year, self.month, self.day)
         return Start
    
    def lengthEmployed(self):
        # calculates how many years employee has been employed
        LengthEmployed = []
        if self.year:
            Now = datetime.datetime.now()
            Start = datetime.datetime(self.year, self.month, self.day)
            LengthEmployed = Now.year - Start.year;
        return LengthEmployed
    
    def printEmployeeDetails(self):
        print('Name: {}\nStart Date: {}\nPay: {}'.format(self.fullname, self.StartDate(), self.pay))
        
    @classmethod
    def set_raise_amount(cls, amount):
        # class method sets raise amount for class
        cls.raise_amount = float(amount)
    
    @classmethod
    def from_string(cls, emp_str):
        #automatically parses string 
        first, last, pay, yearEmp, monthEmp, dayEmp = emp_str.split("-")
        return cls(first, last, int(pay), int(yearEmp), int(monthEmp), int(dayEmp))
    
    @staticmethod
    def is_workday(day):
        #Tests wether the day is a workday
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    #   Special Methods
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)
    
    def __add__(self, other):
        totalpay = self.pay + other.pay
        print(totalpay)
        
    def __len__(self):
        lengthName = len(self.fullname)
        print(lengthName)
    
 # Inheritance Class 
class Developer(Employee):
    raise_amount = 7
    def __init__(self, first, last, pay, yearEmp, monthEmp, dayEmp, prog_lang):
        super().__init__(first, last, pay, yearEmp, monthEmp, dayEmp)
        self.prog_lang = prog_lang
        self.position = "Developer"
    def printEmployeeDetails(self):
        print('Name: {}\nStart Date: {}\nPosition: {}\nPay: {}\nProgramming Language: {}\nEmail: {}\n'.format(self.fullname, 
              self.StartDate(), self.position, self.pay, self.prog_lang, self.email))
#       Regular Method Examples

class Artist(Employee):
    raise_amount = 6
    def __init__(self, first, last, pay, yearEmp, monthEmp, dayEmp, art_type):
        super().__init__(first, last, pay, yearEmp, monthEmp, dayEmp)
        self.art_type = art_type
        self.position = "Artist"
    def printEmployeeDetails(self):
        print('Name: {}\nStart Date: {}\nPosition: {}\nPay: {}\nArt: {}\nEmail: {}\n'.format(self.fullname, 
              self.StartDate(), self.position, self.pay, self.art_type, self.email))
    
class Manager(Employee):
    raise_amount = 7
    N_Employees = Employee.num_of_emps -1
    def __init__(self, first, last, pay, yearEmp, monthEmp, dayEmp, prog_lang, employees= None):
        super().__init__(first, last, pay, yearEmp, monthEmp, dayEmp)
        self.prog_lang = prog_lang
        self.position = "Manager"
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def printEmployeeDetails(self):
        print('Name: {}\nStart Date: {}\nPosition: {}\nPay: {}\nProgramming Language: {}\nEmail: {}\nNumber of Employees: {}\n'.format(self.fullname, 
              self.StartDate(), self.position, self.pay, self.prog_lang, self.email, self.N_Employees))
        
    def add_employees(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def rem_employees(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_employees(self):
        for emp in self.employees:
            print('--> {}\n'.format( emp.fullname))
    
    
        
emp1 = Manager("Andrew", "Rice", 50000, 2012, 2, 24, "MATLAB and Python")
emp2 = Artist("Rebecca", "Debono", 50000, 2014, 2, 24, "3D-Animation")
emp3 = Artist("Jada", "Debono", 50000, 2019, 2, 24, "2D-Animation")
#print(emp1.fullname())
#print("Pay: £" '{}'.format(emp1.pay))
#print("Email: " + emp1.email )
#print("Years Employed: {} ".format(emp1.lengthEmployed()))
##       Class Method examples @classmethod
#Employee.set_raise_amount(5) # sets raise amount
#emp3.raise_amount = 4 # sets individual amount
#emp3.raise_amount
#emp1.raise_amount
#Employee.set_raise_amount(6)
#emp3.raise_amount

emp4_str = "Gabriel-Debono-40000-2018-2-24-Abstract"
first, last, pay, yearEmp, monthEmp, dayEmp, art_type = emp4_str.split("-") #Manual Parse
emp4 = Artist(first, last, int(pay), int(yearEmp), int(monthEmp), int(dayEmp), art_type)

emp5_str = "Sushi-Debono-40000-2018-2-24"
emp5 = Employee.from_string(emp5_str) # Automatic

#       Static Method Examples

#my_date = datetime.date(2019, 9, 22) #22 = Sunday 24 = Tuesdat
#print(Employee.is_workday(my_date))

# Inheritance Class
emp6 = Developer("Matthew", "Rice", 450000, 2016, 2, 24, "Python")
emp6.printEmployeeDetails()
emp1.printEmployeeDetails()
emp2.printEmployeeDetails()

emp1.add_employees(emp2)
emp1.add_employees(emp3)
emp1.add_employees(emp4)
emp1.add_employees(emp5)
emp1.add_employees(emp6)

emp1.print_employees()
emp1.printEmployeeDetails()
#print(isinstance(emp1, Developer)) #False
#print(isinstance(emp1, Employee))   # True
#print(issubclass(Developer, Employee)) #True
#print(issubclass(Developer, Manager)) #False

#   Special Methods

## repr and str
#repr(emp1)
#str(emp1)
#print(repr(emp1))
#print(str(emp1))
#print(emp1.__repr__())
#print(emp1.__str__())

## add
#Employee.__add__(emp1, emp2)
## len
#Employee.__len__(emp3)

##   Property Decorators
#emp1.email

# setter

emp7 = Developer("John", "Smith", 350000, 2019, 2, 24, "Java")
emp7.fullname = 'Alec Guiness'
emp7.email

# deleter
del emp7.fullname