# 11-3. Employee: Write a class called Employee. The __init__() method should 
# take in a first name, a last name, and an annual salary, and store each of 
# these as attributes. Write a method called give_raise() that adds $5,000 to 
# the annual salary by default but also accepts a different raise amount.

# Write a test case for Employee. Write two test methods, test_give_default _raise() 
# st_give_custom_raise(). Use the setUp() method so you don’t have to create a new 
# mployee instance in each test method. Run your test case, and make sure both 
# tests pass.

import unittest

class Employee:
	"""A class that stores first name, last name and annual salary """
	def __init__(self, first, last, salary):
 		"""Storing first name, last name and annual salary"""
 		self.first = first
 		self.last = last
 		self.salary = salary


	def give_raise(self, salary_raise=5000):
		self.salary += salary_raise

	def show(self):
		"""Showing all info"""
		print(f"{self.first} {self.last} {self.salary}")


class test_give_default(unittest.TestCase):
	"""Testing all the methods"""
	def setUp(self):
		"""Setting up all the parameters"""
		self.my_test = Employee("Juan", "Gomez", 100000)

	def test_give_default_raise(self):
		self.my_test.give_raise()
		self.assertEqual(100000 + 5000, self.my_test.salary)

	def test_give_custom_raise(self):
		self.my_test.give_raise(8000)
		self.assertEqual(100000 + 8000, self.my_test.salary)


if __name__ == "__main__":
	unittest.main()
 