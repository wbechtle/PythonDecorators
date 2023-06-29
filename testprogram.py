#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 4/20/2023
#Project: Person Class Unit Test
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"Rewrite your Person class (Student and Instructor classes will be extra credit ) to utilize 
#the @property decorator. Write a unit test program to test the functionality of ALL the 
#classes methods."
#--------------------------------------------------------------------------------------------
#Algorithm
#-----------------
#Step 1) Test all edge casses for each method and constructor.
#Step 2) Display results.
#--------------------------------------------------------------------------------------------
import unittest
from Person import Person
from Instructor import Instructor
from Student import Student

#The purpose of this class is to test every case possible in the classes listed above.
class Person_Test(unittest.TestCase):

    #1st test: used to ensure contructor default values sets to 0 or specified value.
    def test_person_constructor(self):

        #Test constructor.
        #Test the input scenario. (Edge Case)
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        self.assertEqual('Jane A Doe', person.full_name)
        self.assertEqual('11/12/1996', person.date_of_birth)

        #Test the invalid input scenario. (Edge Case)
        with self.assertRaises(ValueError):
            Person('', 'A', '', '11/12/1996')

    #2nd test: used to ensure get first name functions.
    def test_get_first_name(self):

        #Test getter. (Edge Case)
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        self.assertEqual('Jane', person.first_name)

    #3rd test: used to ensure get middle intitial functions.
    def test_get_middle_initial(self):

        #Test getter. (Edge Case)
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        self.assertEqual('A', person.middle_initial)

    #4th test: used to ensure get last name functions.
    def test_get_last_name(self):

        #Test getter. (Edge Case)
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        self.assertEqual('Doe', person.last_name)

    #5th test: used to ensure get full name functions.
    def test_get_full_name(self):

        #Test getter. (Edge Case)
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        self.assertEqual('Jane A Doe', person.full_name)

    #6th test: used to ensure get date of birth functions.
    def test_get_date_of_birth(self):

        #Test getter. (Edge Case)
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        self.assertEqual('11/12/1996', person.date_of_birth)

    #7th test: used to ensure str method functions.
    def test_str_method_of_person(self):

        #Test __str__. (Edge Case)
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        self.assertEqual('Name: Jane A Doe\nDate of Birth: 11/12/1996', person.__str__())

    #8th test: used to ensure repr method functions.
    def test_repr_method_of_person(self):

        #Test __repr__. (Edge Case)
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        self.assertEqual("person.Person('Jane', 'A', 'Doe', '11/12/1996')", person.__repr__())

    #9th test: used to ensure all delete methods function.
    def test_delete_methods_of_person(self):

        #Test all deletes.
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        del person.first_name
        del person.middle_initial
        del person.last_name
        del person.date_of_birth
        
        #Make assertions.
        with self.assertRaises(AttributeError):
            person.first_name
        with self.assertRaises(AttributeError):
            person.middle_initial
        with self.assertRaises(AttributeError):
            person.last_name
        with self.assertRaises(AttributeError):
            person.date_of_birth  
        
        #New object to test full name.
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        del person.full_name
        with self.assertRaises(AttributeError):
            person.full_name     

    #10th test: used to ensure set first name method functions.
    def test_set_first_name_method(self):

        #Create an object to run tests with.
        person = Person('Jane', 'A', 'Doe', '11/12/1996')

        #Call all setters and test after each call.
        person.first_name = 'John'
        self.assertEqual('John', person.first_name)

    #11th test: used to ensure set middle initial method functions.
    def test_set_middle_initial_method(self):

        #Create an object to run tests with.
        person = Person('Jane', 'A', 'Doe', '11/12/1996')

        person.middle_initial = 'S'
        self.assertEqual('S', person.middle_initial)

    #12th test: used to ensure set last name method functions.
    def test_set_last_name_method(self):

        #Create an object to run tests with.
        person = Person('Jane', 'A', 'Doe', '11/12/1996')

        person.last_name = 'Smith'
        self.assertEqual('Smith', person.last_name)

    #13th test: used to ensure set date of birth method functions.
    def test_set_date_of_birth_method(self):

        #Create an object to run tests with.
        person = Person('Jane', 'A', 'Doe', '11/12/1996')

        person.date_of_birth = '12/10/1990'
        self.assertEqual('12/10/1990', person.date_of_birth)

    #14th test: used to ensure set full name method functions.
    def test_set_full_name_method(self):

        #Create an object to run tests with.
        person = Person('Jane', 'A', 'Doe', '11/12/1996')

        person.full_name = 'Java L Hut'
        self.assertEqual('Java L Hut', person.full_name)

    #15th test: used to ensure the instructor constructor functions.
    def test_instructor_constructor(self):
        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        self.assertEqual('Jane A Doe', instructor.full_name)
        self.assertEqual('10/11/1996', instructor.date_of_birth)
        self.assertEqual('50000', instructor.salary)
        self.assertEqual('PhD', instructor.degree)
        self.assertEqual('Mathematics', instructor.department)

        #Test the invalid input scenario. (Edge Case)
        with self.assertRaises(ValueError):
            Instructor('', 'A', '', '11/12/1996', '50000', 'PhD', '')

    #16th test: used to ensure the get salary method functions.
    def test_get_salary(self):
        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        self.assertEqual('50000', instructor.salary)

    #17th test: used to ensure the get degree method functions.
    def test_get_degree(self):
        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        self.assertEqual('PhD', instructor.degree)

    #18th test: used to ensure the get department method functions.
    def test_get_department(self):
        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        instructor.department = 'Computer Science'
        self.assertEqual('Computer Science', instructor.department)

    #19th test: used to ensure the str method functions.
    def test_str_of_instructor(self):
        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        self.assertEqual('Name: Jane A Doe\nDegree: PhD\nDepartment: Mathematics\nSalary: $50,000', instructor.__str__())
    
    #20th test: used to ensure the repr department method functions.
    def test_repr_of_instructor(self):
        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        self.assertEqual("Instructor.Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')", instructor.__repr__())

    #21st test: used to ensure the set salary method functions.
    def test_set_salary(self):
        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        instructor.salary = '60000'
        self.assertEqual('60000', instructor.salary)

    #22nd test: used to ensure the set degree method functions.
    def test_set_degree(self):
        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        instructor.degree = 'MS'
        self.assertEqual('MS', instructor.degree)

    #23rd test: used to ensure the set department method functions.
    def test_set_department(self):
        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        instructor.department = 'Computer Science'
        self.assertEqual('Computer Science', instructor.department)

    #24th test: used to ensure all delete methods function.
    def test_delete_methods_of_instructor(self):

        #Test all deletes.
        instructor = Instructor('Jane', 'A', 'Doe', '11/12/1996', '50000', 'PhD', 'Mathematics')
        del instructor.salary
        del instructor.degree
        del instructor.department
        
        #Make assertions.
        with self.assertRaises(AttributeError):
            instructor.salary
        with self.assertRaises(AttributeError):
            instructor.degree
        with self.assertRaises(AttributeError):
            instructor.department
        
    #25th test: used to ensure the student constructor functions.
    ##The getter methods are implicitly tested in each test.##
    def test_student_constructor(self):
        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        self.assertEqual('Jane A Doe', student.full_name)
        self.assertEqual('10/11/1996', student.date_of_birth)
        self.assertEqual('CSC', student.major)
        self.assertEqual('3.67', student.gpa)
        self.assertEqual('JR', student.classification)
        
        #Test the invalid input scenario. (Edge Case)
        with self.assertRaises(ValueError):
            Instructor('', 'A', 'Doe', '', 'CSC', '3.67', '')

    #26th test: used to ensure the get major method functions.
    def test_get_major(self):
        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        self.assertEqual('CSC', student.major)

    #27th test: used to ensure the get gpa method functions.
    def test_get_gpa(self):
        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        self.assertEqual('3.67', student.gpa)

    #28th test: used to ensure the get classification method functions.
    def test_get_classification(self):
        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        self.assertEqual('JR', student.classification)

    #29th test: used to ensure the str method functions.
    def test_str_of_student(self):
        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        self.assertEqual('Name: Jane A Doe\ngpa: 3.67\nclassification: JR\nmajor: CSC', student.__str__())
    
    #30th test: used to ensure the repr department method functions.
    def test_repr_of_student(self):
        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        self.assertEqual("Student.Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')", student.__repr__())

    #31st test: used to ensure the set major method functions.
    def test_set_major(self):
        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        student.major = 'MAT'
        self.assertEqual('MAT', student.major)

    #32nd test: used to ensure the set gpa method functions.
    def test_set_gpa(self):
        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        student.gpa = '3.33'
        self.assertEqual('3.33', student.gpa)

    #33rd test: used to ensure the set classification method functions.
    def test_set_classification(self):
        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        student.classification = 'SR'
        self.assertEqual('SR', student.classification)

    #34th test: used to ensure all delete methods function.
    def test_delete_methods_of_student(self):

        #Test all deletes.
        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        del student.major
        del student.gpa
        del student.classification
        
        #Make assertions.
        with self.assertRaises(AttributeError):
            student.major
        with self.assertRaises(AttributeError):
            student.gpa
        with self.assertRaises(AttributeError):
            student.classification

#Run unnittest main if ran as main.
if __name__ == '__main__':
    unittest.main()