#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 3/2/2023
#Project: Student Class (SubClass of Person Class)
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"Using your Person class from a previous assignment as a superclass. If your Person class 
#had errors, correct them prior to using it for this project. Make two classes, Student and 
#Instructor, that inherit from Person.  A student has a major, a GPA and classification (FR, 
#SO, JR, SR) and an instructor has a salary, degree (PhD, MS) and department (CIS, CNG, CSC)."
#--------------------------------------------------------------------------------------------
#UML Class Diagram
#-----------------
#See accompanying UML Class Diagram.
#--------------------------------------------------------------------------------------------
from Person import Person

# Create structure for Student class.
class Student(Person):

    # CONSTUCTURE...
    # Initialization for each instance. The constructer uses the validation code within the 
    # setters to reduce code redundancy and valid parameters passed to constructer.
    def __init__(self, first, middle, last, date, major, gpa, classification):
        super().__init__(first, middle, last, date) # Call the super initializer.
        self.major = major
        self.gpa = gpa
        self.classification = classification

    @property
    # Getter.
    def major(self):
        return self._major

    # Sets the attribute. If empty string, raise valueerror.
    @major.setter
    def major(self, value):
        if value != '': # No empty strings.
            self._major = value
        else:
            raise ValueError('Major cannot be empty string.')

    @major.deleter
    def major(self):
        del self._major

    # Getter.
    @property
    def gpa(self):
        return self._gpa

    # Sets the attribute. If empty string, raise valueerror.
    @gpa.setter
    def gpa(self, value):
        if value != '': # No empty strings.
            self._gpa = value
        else:
            raise ValueError('GPA cannot be empty string.')

    @gpa.deleter
    def gpa(self):
        del self._gpa

    # Getter.
    @property
    def classification(self):
        return self._classification

    # Sets the attribute. If empty string, raise valueerror.
    @classification.setter
    def classification(self, value):
        if value != '': # No empty strings.
            self._classification = value
        else:
            raise ValueError('Classification cannot be empty string.')

    @classification.deleter
    def classification(self):
        del self._classification

    # str method.
    def __str__(self):
        return f'Name: {self.full_name}\ngpa: {self.gpa}\nclassification: {self.classification}\nmajor: {self.major}'

    # repr method.
    def __repr__(self):
        return f"Student.Student('{self.first_name}', '{self.middle_initial}', '{self.last_name}', '{self.date_of_birth}', '{self.major}', '{self.gpa}', '{self.classification}')"