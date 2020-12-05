# 6-8. Pets: Make several dictionaries, where 
# each dictionary represents a different pet. 
# in each dictionary, include the kind of animal
# and the owner’s name. Store these dictionaries 
# in a list called pets. Next, loop through your 
# list and as you do, print everything you know 
# about each pet.

mascota1 = {"owner_name": "emili",
			"name": "candy",
			"species": "dog",
			"age": 2
			}

mascota2 = {"owner_name": "juan",
			"name": "canelo",
			"species": "dog",
			"age": 5
			}

mascota3 = {"owner_name": "diana",
			"name": "princesa",
			"species": "dog",
			"age": 7
			}

animales = [mascota1, mascota2, mascota3]

for animal in animales:
	print(f"El nombre de la mascota es {animal['name'].title()}"
			f" es un {animal['species']}")


