# 8-6. City Names: Write a function called city_country() that takes in the 
# name of a city and its country. The function should return a string formatted 
# like this:

# "Santiago, Chile"

# Call your function with at least three city-country pairs, and print 
# the values that are returned.

def city_country(name_city, country):
	print("Write a city and a country ")
	print(f"{name_city}, {country}" )

city_country("Paris", "France")
city_country("London", "Canada")
city_country("Mexico", "Mexico")
