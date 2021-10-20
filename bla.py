from pathlib import Path

filename = Path('savedata.txt')
filename.touch(exist_ok=True)  # will create file, if it exists will do nothing
file = open(filename, "r+")
score_savedata = file.read()
if score_savedata:
	print(score_savedata)
else: 
	print("nothing here")

numero = input("Numero   ")


if numero > score_savedata:
	file = open(filename, "w+")
	file.write(numero)
	print(numero)

	
print("succedeed")

file.close()

#### Creo que con with open(arschivo, "w") as file: 
#### Es mas que suficiente, por que si no exite lo creara, 
#### Y cuando lea el contenido que estara vacio, encontes no cambiara
#### el high score.

# Primero necesito saber si el archivo ya existe
# Si ya existe 	
	# Obtener el valor del archivo
# Si no crear un archivo con valor de cero

# savedata
# En este punto ya habra si o si un archivo que leer
# Abrir el archivo y obtener el valor high score
	# Si high score actual mayor que high score del archivo
		# Escribir el valor actual
	# Si no no hacer nada

