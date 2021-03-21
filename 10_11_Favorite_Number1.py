# 10-11. Favorite Number: Write a program that prompts for the user’s favorite number. 
# Use json.dump() to store this number in a file. Write a separate program that reads 
# in this value and prints the message, “I know your favorite number! It’s _____.” 
import json

archivo = "numero.json"

print("Hello there\n")
try:
	numero = input("Please write a your favorite number ")
	with open(archivo, "w") as file:
		json.dump(int(numero), file)
		print(f"Your favorite numeber is {numero}")

except ValueError:
	print("Err: Please write a number ")
