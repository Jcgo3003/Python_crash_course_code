# 10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org/ ) and find 
# a few texts you’d like to analyze. Download the text files for these works, or 
# copy the raw text from your browser into a text file on your computer.

 # You can use the count() method to find out how many times a word or phrase appears 
 # in a string. For example, the following code counts the number of times 'row' 
 # appears in a staaring:

archivos = ["Around the Black Sea.txt", "The dawn of astronomy.txt", "Healing Rays.txt"]

def read(archivo):
	try: 
		with open(archivo, "r") as file:
			count = file.read().lower().count("the ")
			print(f"The count of 'the ' it {archivo} is {count}")
	except FileNotFoundError:
		pass

for archivo in archivos:
	read(archivo)