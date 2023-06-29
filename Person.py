#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 4/20/2023
#Project: Person Class (SuperClass to Instructor, Student)
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

# Create structure for Person class.
class Person:

    # CONSTUCTURES...
    # Initialization for each instance. The constructer uses the validation code within the 
    # setters to reduce code redundancy and valid parameters passed to constructer.
    def __init__(self, first_name, middle_initital, last_name, date):

        # Call first_name setter method and pass parameter.
        self.first_name = first_name

         # Call middle_initital setter method and pass parameter.
        self.middle_initial = middle_initital

         # Call last_name setter method and pass parameter.
        self.last_name = last_name

        # Call date_of_birth setter method and pass parameter.
        self.date_of_birth = date

    @property
    #Getter...
    def first_name(self):  
        return self.__first_name

    # Sets the attribute. If empty string raise valueerror.
    @first_name.setter
    def first_name(self, new_name):
        if new_name != '': #Check if value is empty string.
            self.__first_name = new_name
        else:
            raise ValueError('Name cannot be empty string.')
        
    @first_name.deleter
    def first_name(self):
        del self.__first_name

    @property
    #Getter...
    def middle_initial(self):
        return self.__middle_initial

    # Sets the attribute. If empty string raise valueerror.
    @middle_initial.setter
    def middle_initial(self, new_initial):
        if new_initial != '': #Check if value is empty string.
            self.__middle_initial = new_initial
        else:
            raise ValueError('Initial cannot be empty string.')
        
    @middle_initial.deleter
    def middle_initial(self):
        del self.__middle_initial

    @property
    #Getter...
    def last_name(self):
        return self.__last_name

    # Sets the attribute. If empty string raise valueerror.
    @last_name.setter
    def last_name(self, new_name):
        if new_name != '': #Check if value is empty string.
            self.__last_name = new_name
        else:
            raise ValueError('Name cannot be empty string.')
        
    @last_name.deleter
    def last_name(self):
        del self.__last_name

    @property
    #Getter...
    def date_of_birth(self):
        return self.__date_of_birth

    # Sets the attribute. If empty string raise valueerror.
    @date_of_birth.setter
    def date_of_birth(self, new_date_of_birth):
        if new_date_of_birth != '': #Check if value is empty string.
            self.__date_of_birth = new_date_of_birth
        else:
            raise ValueError('Date cannot be empty string.')
        
    @date_of_birth.deleter
    def date_of_birth(self):
        del self.__date_of_birth

    @property
    #Getter...
    def full_name(self):
        return str(self.first_name) + ' ' + str(self.middle_initial) + ' ' + str(self.last_name)

    # Sets the attribute. If empty string raise valueerror.
    @full_name.setter
    def full_name(self, new_name):
        if new_name != '': #Check if value is empty string.
            self.__first_name, self.__middle_initial, self.__last_name = new_name.split(' ')
        else:
            raise ValueError('Names cannot be empty string.')
        
    @full_name.deleter
    def full_name(self):
        del self.__first_name, self.__middle_initial, self.__last_name

    # str method.
    def __str__(self):
        return f'Name: {self.full_name}\nDate of Birth: {self.date_of_birth}'
    
    # repr method.
    def __repr__(self):

        #Assign values to variable to make more readable in return statement.
        first_name = self.first_name
        middle_initial = self.middle_initial
        last_name = self.last_name
        date_of_birth = self.date_of_birth

        return f"person.Person('{first_name}', '{middle_initial}', '{last_name}', '{date_of_birth}')"