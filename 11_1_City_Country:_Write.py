# 11-1. City, Country: Write a function that accepts two parameters: a city name and 
# a country name. The function should return a single string of the form City, 
# Country, such as Santiago, Chile. Store the function in a module called 
# city_functions.py.

# Create a file called test_cities.py that tests the function you just wrote 
# (remember that you need to import unittest and the function you want to test). 
# Write a method called test_city_country() to verify that calling your function 
# with values such as 'santiago' and 'chile' results in the correct string. 
# Run test_cities.py, and make sure test_city_country() passes.


def city_country(city, country):
	"""Function to show a country with a city"""
	return (f"{city}, {country}")

print(city_country("London", "U.K."))


import unittest

from city_functions import city_country

class CountryCityTestCase(unittest.TestCase):
	"""Test function for Country_City """
	def test_Country_City(self):
		"""Do a city like New York and a U.S.A  work?"""
		formatted_name = city_country("New York", "USA")

		self.assertEqual(formatted_name, "New York, USA")

		