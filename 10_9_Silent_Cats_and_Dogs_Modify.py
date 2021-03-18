# 10-9. Silent Caats and Dogs: Modify your except block in Exercise 10-8 to fail silently 
# if either file is missing.

archivos = ["cats.txt", "dogs.txt"]

def read(archivo):
	try: 
		with open(archivo, "r") as file:
			for line in file:
				print(line.rstrip())
	except FileNotFoundError:
		pass

for archivo in archivos:
	read(archivo)