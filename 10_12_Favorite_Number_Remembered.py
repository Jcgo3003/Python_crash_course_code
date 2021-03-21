# 10-12. Favorite Number Remembered: Combine the two programs from Exercise 10-11 
# into one file. If the number is already stored, report the favorite number to 
# the user. If not, prompt for the user’s favorite number and store it in a file. 
# Run the program twice to see that it works.

import json

def saveNumber():
	"""A program that saves a number into a json"""
	archivo = "numero.json"
	
	print("Hello there\n")
	try:
		numero = input("Please write a your favorite number ")
		with open(archivo, "w") as file:
			json.dump(int(numero), file)
			return numero

	except ValueError:
		print("Err: Please write a number ")

def readNumber():
	"""A program that reads a json file"""
	archivo = "numero.json"

	try: 
		with open(archivo) as file:
			numero = json.load(file)
	except FileNotFoundError:
		return None
	else: 
		return numero

def favoriteNumber():
	"""Managing the programs sabeNumber/readNumber"""
	numero = readNumber()
	if numero:
		print(f"Your favorite number is {numero}")
	else: 
		numero = saveNumber()

		print(f"Your favorite number is {numero}, and now is saved")

favoriteNumber()