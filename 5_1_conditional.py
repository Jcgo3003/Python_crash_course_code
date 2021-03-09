# 5-1. Conditional Tests: Write a series of conditional tests. 
# Print a statement describing each test and your prediction for 
# the results of each test. Your code should look something like this:

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



