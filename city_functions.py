
def city_country(city, country, population=0):
	"""Function to show a country with a city"""
	if population:
		return (f"{city}, {country} - population {population}") 
	else:
		return (f"{city}, {country}") 
