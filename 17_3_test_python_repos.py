import unittest

# Testing function
from python_repos_17_3 import api_response

class APITest(unittest.TestCase):
	'''A class with series of unittest for github's API'''

	def test_online(self):
		# Testing if we get an online(200) response
		self.assertEqual(api_response()[0], 200)

	def test_number_repositories(self):
		# Total number of repositories must be greater that 8,000,000
		self.assertGreater(api_response()[1], 8_000_000)

	def test_items(self): 
		# Total number of items returned must be 30
		self.assertEqual(api_response()[2], 30)

if __name__ == '__main__':
	unittest.main()

