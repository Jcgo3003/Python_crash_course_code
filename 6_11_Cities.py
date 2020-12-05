# 6-11. Cities: Make a dictionary called cities. 
# Use the names of three cities as keys in your 
# dictionary. Create a dictionary of information 
# about each city and include the country that 
# he city is in, its approximate population, 
# and one fact about that city. The keys for 
# each city’s dictionary should be something 
# like country, population, and fact. Print the 
# name of each city and all of the information 
# you have stored about it.

cities = {"ny":{"country": "US", "population": 12000000,"fact": "they love pizza" },
		  "paris":{"country": "france", "population": 8000000,"fact": "they love chesse" },
		  "london":{"country": "UK", "population": 8000000,"fact": "they love beer" }  
			}

for city, info in cities.items():
	inf = f"{info['country']} with a population of {info['population']}"
	fun_fact = info["fact"]

	print(f"The city of {city.title()} is in\n{inf}\na fun fact about the city is\n{fun_fact}\n")