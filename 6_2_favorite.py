# 6-2. Favorite Numbers: Use a dictionary to 
# store people’s favorite numbers. 
# Think of five names, and use them as keys 
# in your dictionary. Think of a favorite 
# number for each person, and store each as a 
# value in your dictionary. Print each person’s 
# name and their favorite number. For even more 
# fun, poll a few friends and get some actual 
# ata for your program.



numero = {
	"Josep": 1, 
	"Martin": 30, 
	"Carlos": 23,
	"Alex": 10
	}

for element in numero:
	print(f"A {element} le gusta {numero[element]}")