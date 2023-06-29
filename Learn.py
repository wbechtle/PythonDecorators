import unittest
from Person import Person
from Instructor import Instructor
from Student import Student

#The purpose of this class is to test every case possible in the classes listed above.
class Person_Test(unittest.TestCase):

    # 1st test: used to ensure constructor default values sets to 0 or specified value.
    def test_person_constructor(self):

        print('\nTesting Person constructor...')

        # Test constructor with valid inputs (edge case)
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        expected_full_name = 'Jane A Doe'
        expected_date_of_birth = '11/12/1996'
        self.assertEqual(expected_full_name, person.full_name)
        self.assertEqual(expected_date_of_birth, person.date_of_birth)

        # Test constructor with invalid input (edge case)
        with self.assertRaises(ValueError):
            Person('', 'A', '', '11/12/1996')

        print('\tPerson constructor functions as expected.')

    # 2nd test: used to ensure get first name functions.
    def test_get_first_name(self):

        print('\nTesting get_first_name method of Person...')
        # Test getter with valid inputs (edge case)
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        expected_first_name = 'Jane'
        self.assertEqual(expected_first_name, person.first_name)
        print('\tExpected first name: ', expected_first_name)
        print('\tResult first name: ', person.first_name)

    # 3rd test: used to ensure get middle initial functions.
    def test_get_middle_initial(self):

        print('\nTesting get_middle_initial method of Person...')
        # Test getter with valid inputs (edge case)
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        expected_middle_initial = 'A'
        self.assertEqual(expected_middle_initial, person.middle_initial)
        print('\tExpected middle initial: ', expected_middle_initial)
        print('\tResult middle initial: ', person.middle_initial)

    # 4th test: used to ensure get last name functions.
    def test_get_last_name(self):

        print('\nTesting get_last_name method of Person...')
        # Test getter with valid inputs (edge case)
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        expected_last_name = 'Doe'
        self.assertEqual(expected_last_name, person.last_name)
        print('\tExpected last name: ', expected_last_name)
        print('\tResult last name: ', person.last_name)

    # 5th test: used to ensure get full name functions.
    def test_get_full_name(self):

        print('\nTesting get_full_name method of Person...')
        # Test getter with valid inputs (edge case)
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        expected_full_name = 'Jane A Doe'
        self.assertEqual(expected_full_name, person.full_name)
        print('\tExpected full name: ', expected_full_name)
        print('\tResult full name: ', person.full_name)

    #7th test: used to ensure str method functions.
    def test_str_method_of_person(self):

        print('\nTesting __str__ method of Person...')
        #Test __str__. (Edge Case)
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        expected = 'Name: Jane A Doe\nDate of Birth: 11/12/1996'
        result = person.__str__()
        self.assertEqual(expected, result)
        print(f'\tExpected result: {expected}')
        print(f'\tResult: {result}')

    #8th test: used to ensure repr method functions.
    def test_repr_method_of_person(self):

        print('\nTesting __repr__ method of Person...')
        #Test __repr__. (Edge Case)
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        expected = "person.Person('Jane', 'A', 'Doe', '11/12/1996')"
        result = person.__repr__()
        self.assertEqual(expected, result)
        print(f'\tExpected result: {expected}')
        print(f'\tResult: {result}')

    #9th test: used to ensure all delete methods function.
    def test_delete_methods_of_person(self):

        print('\nTesting delete methods of Person...')
        
        #Test all deletes.
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        del person.first_name
        del person.middle_initial
        del person.last_name
        del person.date_of_birth
        
        #Make assertions.
        with self.assertRaises(AttributeError):
            person.first_name
            print('\tDelete first name successful')
        with self.assertRaises(AttributeError):
            person.middle_initial
            print('\tDelete middle initial successful')
        with self.assertRaises(AttributeError):
            person.last_name
            print('\tDelete last name successful')
        with self.assertRaises(AttributeError):
            person.date_of_birth  
            print('\tDelete date of birth successful')
        
        #New object to test full name.
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        del person.full_name
        with self.assertRaises(AttributeError):
            person.full_name   
            print('\tDelete full name successful')  
            
        print('\tAll delete methods are functioning correctly.')

    #10th test: used to ensure set first name method functions.
    def test_set_first_name_method(self):

        print('\nTesting set_first_name method of Person...')

        #Create an object to run tests with.
        person = Person('Jane', 'A', 'Doe', '11/12/1996')

        #Call all setters and test after each call.
        person.first_name = 'John'
        expected = 'John'
        result = person.first_name
        self.assertEqual(expected, result)
        print(f'\tExpected first name: {expected}')
        print(f'\tResult first name: {result}')

    # 11th test: used to ensure set middle initial method functions.
    def test_set_middle_initial_method(self):

        print('\nTesting set_middle_initial method of Person...')

        # Create an object to run tests with.
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        
        # Test set_middle_initial method
        expected_initial = 'S'
        person.middle_initial = expected_initial
        result_initial = person.middle_initial
        self.assertEqual(expected_initial, result_initial)
        print(f'\tExpected middle initial: {expected_initial}')
        print(f'\tResult middle initial: {result_initial}')

    # 12th test: used to ensure set last name method functions.
    def test_set_last_name_method(self):

        print('\nTesting set_last_name method of Person...')

        # Create an object to run tests with.
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        
        # Test set_last_name method
        expected_last_name = 'Smith'
        person.last_name = expected_last_name
        result_last_name = person.last_name
        self.assertEqual(expected_last_name, result_last_name)
        print(f'\tExpected last name: {expected_last_name}')
        print(f'\tResult last name: {result_last_name}')

    # 13th test: used to ensure set date of birth method functions.
    def test_set_date_of_birth_method(self):

        print('\nTesting set_date_of_birth method of Person...')

        # Create an object to run tests with.
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        
        # Test set_date_of_birth method
        expected_date_of_birth = '12/10/1990'
        person.date_of_birth = expected_date_of_birth
        result_date_of_birth = person.date_of_birth
        self.assertEqual(expected_date_of_birth, result_date_of_birth)
        print(f'\tExpected date of birth: {expected_date_of_birth}')
        print(f'\tResult date of birth: {result_date_of_birth}')

    # 14th test: used to ensure set full name method functions.
    def test_set_full_name_method(self):

        print('\nTesting set_full_name method of Person...')

        # Create an object to run tests with.
        person = Person('Jane', 'A', 'Doe', '11/12/1996')
        
        # Test set_full_name method
        expected = 'Java L Hut'
        person.full_name = expected
        result = person.full_name
        self.assertEqual(expected, result)
        print(f'\tExpected full name: {expected}')
        print(f'\tResult full name: {result}')

    # 15th test: used to ensure the instructor constructor functions.
    def test_instructor_constructor(self):

        print('\nTesting Instructor constructor...')
        
        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        self.assertEqual('Jane A Doe', instructor.full_name)
        self.assertEqual('10/11/1996', instructor.date_of_birth)
        self.assertEqual('50000', instructor.salary)
        self.assertEqual('PhD', instructor.degree)
        self.assertEqual('Mathematics', instructor.department)

        #Test the invalid input scenario. (Edge Case)
        with self.assertRaises(ValueError):
            Instructor('', 'A', '', '11/12/1996', '50000', 'PhD', '')

        print('\tPerson constructor functions as expected.')


    #16th test: used to ensure the get salary method functions.
    def test_get_salary(self):

        print('\nTesting get_salary method of Instructor...')

        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        expected = '50000'
        result = instructor.salary
        self.assertEqual(expected, result)
        print(f'\tExpected gpa: {expected}')
        print(f'\tResult gpa: {result}')

    #17th test: used to ensure the get degree method functions.
    def test_get_degree(self):

        print('\nTesting get_degree method of Instructor...')

        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        expected = 'PhD'
        result = instructor.degree
        self.assertEqual(expected, result)
        print(f'\tExpected degree: {expected}')
        print(f'\tResult degree: {result}')

    #18th test: used to ensure the get department method functions.
    def test_get_department(self):

        print('\nTesting get_department method of Instructor...')

        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        expected = 'Computer Science'
        instructor.department = expected
        result = instructor.department
        self.assertEqual(expected, result)
        print(f'\tExpected department: {expected}')
        print(f'\tResult department: {result}')

    #19th test: used to ensure the str method functions.
    def test_str_of_instructor(self):

        print('\nTesting __str__ method of Instructor...')

        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        expected = 'Name: Jane A Doe\nDegree: PhD\nDepartment: Mathematics\nSalary: $50,000'
        result = instructor.__str__()
        self.assertEqual(expected, result)
        print(f'\tExpected: {expected}')
        print(f'\tResult: {result}')

    #20th test: used to ensure the repr department method functions.
    def test_repr_of_instructor(self):

        print('\nTesting __repr__ method of Instuctor...')

        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        expected = "Instructor.Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')"
        result = instructor.__repr__()
        self.assertEqual(expected, result)
        print(f'\tExpected: {expected}')
        print(f'\tResult: {result}')

    #21st test: used to ensure the set salary method functions.
    def test_set_salary(self):

        print('\nTesting set_salary method of Instructor...')

        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        instructor.salary = '60000'
        expected = '60000'
        result = instructor.salary
        self.assertEqual(expected, result)
        print(f'\tExpected salary: {expected}')
        print(f'\tResult salary: {result}')

    #22nd test: used to ensure the set degree method functions.
    def test_set_degree(self):

        print('\nTesting set_degree method of Instructor...')

        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        instructor.degree = 'MS'
        expected = 'MS'
        result = instructor.degree
        self.assertEqual(expected, result)
        print(f'\tExpected degree: {expected}')
        print(f'\tResult degree: {result}')

    #23rd test: used to ensure the set department method functions.
    def test_set_department(self):

        print('\nTesting set_department method of Instructor...')
        
        instructor = Instructor('Jane', 'A', 'Doe', '10/11/1996', '50000', 'PhD', 'Mathematics')
        instructor.department = 'Computer Science'
        expected = 'Computer Science'
        result = instructor.department
        self.assertEqual(expected, result)
        print(f'\tExpected department: {expected}')
        print(f'\tResult department: {result}')

    #24th test: used to ensure all delete methods function.
    def test_delete_methods_of_instructor(self):
        
        print('\nTesting delete methods of Instructor...')
        
        #Test all deletes.
        instructor = Instructor('Jane', 'A', 'Doe', '11/12/1996', '50000', 'PhD', 'Mathematics')
        del instructor.salary
        del instructor.degree
        del instructor.department
        
        #Make assertions.
        with self.assertRaises(AttributeError):
            instructor.salary
            print('\tDelete salary successful')
        with self.assertRaises(AttributeError):
            instructor.degree
            print('\tDelete degree successful')
        with self.assertRaises(AttributeError):
            instructor.department
            print('\tDelete department successful')

    #25th test: used to ensure the student constructor functions.
    ##The getter methods are implicitly tested in each test.##
    def test_student_constructor(self):

        print('\nTesting Student constructor...')

        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        self.assertEqual('Jane A Doe', student.full_name)
        self.assertEqual('10/11/1996', student.date_of_birth)
        self.assertEqual('CSC', student.major)
        self.assertEqual('3.67', student.gpa)
        self.assertEqual('JR', student.classification)
        
        #Test the invalid input scenario. (Edge Case)
        with self.assertRaises(ValueError):
            Student('', 'A', 'Doe', '', 'CSC', '3.67', '')

        print('\Student constructor functions as expected.')


    #26th test: used to ensure the get major method functions.
    def test_get_major(self):

        print('\nTesting get major method of Student...')

        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        expected = 'CSC'
        result = student.major
        self.assertEqual(expected, result)
        print(f'\tExpected major: {expected}')
        print(f'\tResult major: {result}')

    #27th test: used to ensure the get gpa method functions.
    def test_get_gpa(self):

        print('\nTesting get gpa method of Student...')

        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        expected = '3.67'
        result = student.gpa
        self.assertEqual(expected, result)
        print(f'\tExpected gpa: {expected}')
        print(f'\tResult gpa: {result}')

    #28th test: used to ensure the get classification method functions.
    def test_get_classification(self):

        print('\nTesting get classification method of Student...')

        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        expected = 'JR'
        result = student.classification
        self.assertEqual(expected, result)
        print(f'\tExpected classification: {expected}')
        print(f'\tResult classification: {result}')

    #29th test: used to ensure the str method functions.
    def test_str_of_student(self):

        print('\nTesting __str__ method of Student...')

        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        expected = 'Name: Jane A Doe\ngpa: 3.67\nclassification: JR\nmajor: CSC'
        result = student.__str__()
        self.assertEqual(expected, result)
        print(f'\tExpected: {expected}')
        print(f'\tResult: {result}')

    #30th test: used to ensure the repr department method functions.
    def test_repr_of_student(self):

        print('\nTesting __repr__ method of Student...')
        
        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        expected = "Student.Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')"
        result = student.__repr__()
        self.assertEqual(expected, result)
        print(f'\tExpected: {expected}')
        print(f'\tResult: {result}')

    #31st test: used to ensure the set major method functions.
    def test_set_major(self):

        print('\nTesting set major method of Student...')

        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        student.major = 'MAT'
        expected = 'MAT'
        result = student.major
        self.assertEqual(expected, result)
        print(f'\tExpected major: {expected}')
        print(f'\tResult major: {result}')

    #32nd test: used to ensure the set gpa method functions.
    def test_set_gpa(self):

        print('\nTesting set gpa method of Student...')

        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        student.gpa = '3.33'
        expected = '3.33'
        result = student.gpa
        self.assertEqual(expected, result)
        print(f'\tExpected gpa: {expected}')
        print(f'\tResult gpa: {result}')

    #33rd test: used to ensure the set classification method functions.
    def test_set_classification(self):

        print('\nTesting set classification method of Student...')
        
        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        student.classification = 'SR'
        expected = 'SR'
        result = student.classification
        self.assertEqual(expected, result)
        print(f'\tExpected classification: {expected}')
        print(f'\tResult classification: {result}')

    #34th test: used to ensure all delete methods function.
    def test_delete_methods_of_student(self):

        print('\nTesting all delete methods of Student...')

        #Test all deletes.
        student = Student('Jane', 'A', 'Doe', '10/11/1996', 'CSC', '3.67', 'JR')
        del student.major
        del student.gpa
        del student.classification
        
        #Make assertions.
        with self.assertRaises(AttributeError):
            student.major
            print('\tDelete major successful')
        with self.assertRaises(AttributeError):
            student.gpa
            print('\tDelete gpa successful')
        with self.assertRaises(AttributeError):
            student.classification
            print('\tDelete classification successful')

#Run unnittest main if ran as main.
if __name__ == '__main__':
    unittest.main()