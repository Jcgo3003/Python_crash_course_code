# 11-2. Population: Modify your function so it requires a third parameter, population. 
# It should now return a single string of the form City, Country population xxx, such 
# as Santiago, Chile – population 5000000. Run test _cities.py again. Make sure 
# test_city_country() fails this time.

# Modify the function so the population parameter is optional. Run test _cities.py 
# again, and make sure test_city_country() passes again.

# Write a second test called test_city_country_population() that verifies you 
# can call your function with the values 'santiago', 'chile', and 'population=5000000'. 
# Run test_cities.py again, and make sure this new test passes.


def city_country(city, country, population=0):
	"""Function to show a country with a city"""
	if population:
		return (f"{city}, {country} - population {population}") 
	else:
		return (f"{city}, {country}") 


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
	