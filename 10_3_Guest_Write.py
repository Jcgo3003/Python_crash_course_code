# 10-3. Guest: Write a program that prompts the user for 
# their name. When they respond, write their name to a file 
# alled guest.txt.

name = input("What's your name? ")
print(name)

archivo = "guest.txt"

with open(archivo, "w") as file:
	file.write(name)

print("Succeded")