import unittest

from city_functions import city_country

class CountryCityTestCase(unittest.TestCase):
	"""Test function for Country_City """
	def test_Country_City(self):
		"""Do a city like New York and a U.S.A  work?"""
		formatted_name = city_country("New York", "USA")

		self.assertEqual(formatted_name, "New York, USA")

	def test_Country_City_Population(self):
		"""Do a city like Mexico City, Mexico and 24000000 work?"""
		formatted_name = city_country("Mexico City", "Mexico", 24000000)

		self.assertEqual(formatted_name, "Mexico City, Mexico - population 24000000")

if __name__ == "__main__":
	unittest.main()
	