countries = ["Mexico", "France", "U.K.", "Spain"]

# Insert
countries.insert(1, "Germany")
print("Insert function")
print(countries)

# Del function 
del countries[1]
print(countries)

# Pop
print("Pop funtion")
print(f"The country to be poped is {countries.pop()}")
print(f"And {countries.pop(0)}")
print(countries)

# Remove
print("Remove function")
countries.remove("France")
print(countries)

# Appening more countries
countries.append("U.S.")
countries.append("Canada")
countries.append("Argentina")
countries.append("Brazil")
print(countries)

# Sorting temporaly
print("Sorting temporaly")
print(sorted(countries))
print(countries)

# Sorting temporaly reverse True
print("Sorting temporaly reverse True")
print(sorted(countries, reverse=True))
print(countries)

# Reverse 
print("Using reverse")
countries.reverse()
print(countries)

# Using sort
print("Using sort")
countries.sort()
print(countries)

# Using sort reversed True
print("Using sort reverse True")
countries.sort(reverse=True)
print(countries)









