# 10-4. Guest Book: Write a while loop that prompts users 
# for their name. When they enter their name, print a 
# greeting to the screen and add a line recording their 
# visit in a file called guest_book.txt. Make sure each 
# entry appears on a new line in the file.

name = "Something"
archivo = "guest.txt"
counter = 0

while (name != "exit"):
	name = input("What's your name?, Write 'exit' to exit\n")
	if name != "exit" and counter == 0:
		print(f"Hello {name}\n")
		counter += 1
		with open(archivo, "w") as file:
			file.write(name)
			file.write("\n")
	elif name != "exit" and counter != 0:
		print(f"Hello {name}\n")
		with open(archivo, "a") as file:
			file.write(name)
			file.write("\n")
print("Bye")


