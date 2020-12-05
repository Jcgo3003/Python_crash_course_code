# 6-5. Rivers: Make a dictionary containing three major rivers 
# and the country each river runs through. One key-value pair 
# might be 'nile': 'egypt'.

# • Use a loop to print a sentence about each river, such as 
# The Nile runs through Egypt.

# • Use a loop to print the name of each river included in the 
# dictionary.

# • Use a loop to print the name of each country included in the 
# dictionary.

rivers = {"Nile":"Egypt", 
	"Bravo": "US-Mex", 
	"Senna": "France", 
	"Thames": "UK"}

for river, country in rivers.items():
	print(f"The {river} runs through {country}")

print("These are the rivers contain in the dictionary")
for river in rivers:
	print(f"The {river}")

print("These are the countries contain in the dictionary")
for countries in rivers.values():
	print(f"The {countries}")	