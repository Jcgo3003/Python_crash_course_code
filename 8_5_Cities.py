# 8-5. Cities: Write a function called describe_city() that accepts the 
# name of a city and its country. The function should print a simple 
# sentence, such as Reykjavik is in Iceland. Give the parameter for the 
# country a default value. Call your function for three different cities, 
# at least one of which is not in the default country.

def describe_city(city, country="France"):
	print(f"{city} is in {country}")

describe_city("Marseille")

describe_city("Paris")

describe_city("London", "UK")
