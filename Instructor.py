#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 4/20/2023
#Project: Instructor Class (SubClass of Person Class)
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"Rewrite your Person class (Student and Instructor classes will be extra credit ) to utilize 
#the @property decorator. Write a unit test program to test the functionality of ALL the 
#classes methods."
#--------------------------------------------------------------------------------------------
#UML Class Diagram
#-----------------
#See accompanying UML Class Diagram.
#--------------------------------------------------------------------------------------------
from Person import Person

# Create structure for Instructor class.
class Instructor(Person):

    # CONSTUCTURE...
    # Initialization for each instance. The constructer uses the validation code within the 
    # setters to reduce code redundancy and valid parameters passed to constructer.
    def __init__(self, first, middle, last, date, salary, degree, department):
        super().__init__(first, middle, last, date) # Call the super initializer.
        self.salary = salary
        self.degree = degree
        self.department = department

    # Getter.
    @property
    def salary(self):
        return self._salary

    # Sets the attribute. If empty string, raise valueerror.
    @salary.setter
    def salary(self, salary):
        if salary != '': #Check if value is empty string.
            self._salary = salary
        else:
            raise ValueError('Salary cannot be empty string.')

    @salary.deleter
    def salary(self):
        del self._salary

    # Getter.
    @property
    def degree(self):
        return self._degree

    # Sets the attribute. If empty string raise valueerror.
    @degree.setter
    def degree(self, degree):
        if degree != '': #Check if value is empty string.
            self._degree = degree
        else:
            raise ValueError('Degree cannot be empty string.')

    @degree.deleter
    def degree(self):
        del self._degree

    # Getter.
    @property
    def department(self):
        return self._department

    # Sets the attribute. If empty string raise valueerror.
    @department.setter
    def department(self, department):
        if department != '': #Check if value is empty string.
            self._department = department
        else:
            raise ValueError('Department cannot be empty string.')

    @department.deleter
    def department(self):
        del self._department

    # str method.
    def __str__(self):
        unformatted_salary = self.salary
        return f'Name: {self.full_name}\nDegree: {self.degree}\nDepartment: {self.department}\nSalary: ${float(unformatted_salary):,.0f}'

    # repr method.
    def __repr__(self):
        first_name = self.first_name
        middle_initial = self.middle_initial
        last_name = self.last_name
        date_of_birth = self.date_of_birth

        return f"Instructor.Instructor('{first_name}', '{middle_initial}', '{last_name}', '{date_of_birth}', '{self.salary}', '{self.degree}', '{self.department}')"
