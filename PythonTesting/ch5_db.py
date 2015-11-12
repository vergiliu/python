from unittest import TestCase
import unittest
from sqlite3 import connect
from sqlite3 import PARSE_DECLTYPES
from datetime import date
from employees import Employees


class TestEmployees(TestCase):
    def setUp(self):
        connection = connect(':memory:', detect_types=PARSE_DECLTYPES)
        cursor = connection.cursor()
        cursor.execute('''create table employees (first text, last text, date_of_employment date)''')
        cursor.execute('''insert into employees(first, last, date_of_employment) values ("John", "Smith", :date)''',
                       {'date': date(year=2013, month=7, day=12)})
        cursor.execute('''insert into employees(first, last, date_of_employment) values ("Jane", "Doe", :date)''',
                       {'date': date(year=2011, month=3, day=11)})
        self.connection = connection

    def tearDown(self):
        self.connection.close()

    def test_add_employee(self):
        new_employee = Employees(self.connection)
        new_employee.add_employee('Test', 'Employee', date.today())
        cursor = self.connection.cursor()
        cursor.execute('''select * from employees''')
        self.assertEqual(tuple(cursor),
                         (('John', 'Smith', date(year=2013, month=7, day=12)),
                          ('Jane', 'Doe', date(year=2011, month=3, day=11)),
                          ('Test', 'Employee', date.today())))

    def test_find_employee(self):
        new_employee = Employees(self.connection)
        found = tuple(new_employee.find_employees_by_name('John', 'Smith'))
        expected = (('John', 'Smith', date(year=2013, month=7, day=12)),)  # expecting single element tuple
        self.assertEqual(found, expected)


if __name__ == "__main__":
    unittest.main()