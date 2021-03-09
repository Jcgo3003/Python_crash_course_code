# 5-2. More Conditional Tests: You don’t have to limit the 
# number of tests you create to ten. If you want to try more 
# comparisons, write more tests and add them to
# conditional_tests.py. Have at least one True and one False 
# result for each of the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, 
#   greater than and less than, greater than or equal to, and less 
# 	than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

comida = 'Pizza'
print("Is comida == 'Pizza'? I predict yes. ")
print(comida == 'Pizza')

print("Is comida == 'Taco'? I predict yes. ")
print(comida == 'Taco')

comprobacion = comida == 'Bla'
print(comprobacion)

# Checking for Inequality

musica = "Bach"
comprobacion = musica != "Bla bla"
print(comprobacion)

# Cheking for a value
juegos = ["Mario 64", "Crash", "GTA"]
comprobacion = "GTA 2" in juegos
print(comprobacion)

# Test with lower() and a list
cars = ['audi','bmw','subaru','toyota']

coche = 'AUdI'

if coche.lower() in cars:
	print(f"{coche.title()} esta en cars")



