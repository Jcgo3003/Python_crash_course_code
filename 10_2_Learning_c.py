# 10-2. Learning C: You can use the replace() method to replace 
# any word in a string with a different word. Here’s a quick 
# example showing how to replace 'dog' with 'cat' in a 
# 'dog' with 'cat' in a sentence:
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat') 'I really like cats.'
# Read in each line from the file you just created, 
# learning_python.txt, and replace the word Python with 
# the name of another language, such as C. Print each 
# modified line to the screen.

archivo = "learning_python.txt"

with open(archivo) as file:
	lineas = file.readlines()

# lineas.rstrip()

for linea in lineas:
	bla = linea.replace("Python", "C++")
	print(bla.rstrip())