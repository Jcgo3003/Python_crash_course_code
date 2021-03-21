# 10-11. Favorite Number: Write a program that prompts for the user’s favorite number. 
# Use json.dump() to store this number in a file. Write a separate program that reads 
# in this value and prints the message, “I know your favorite number! It’s _____.” 
import json

archivo = "numero.json"

try: 
	with open(archivo) as file:
		numero = json.load(file)
	print(f"Your favorite number is {numero}")	
except FileNotFoundError:
	print("Err: There's no such file")
