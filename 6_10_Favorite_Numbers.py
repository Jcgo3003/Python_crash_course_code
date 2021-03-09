# 6-10. Favorite Numbers: Modify your program 
# from Exercise 6-2 (page 99) so each person 
# can have more than one favorite number. 
# Then print each person’s name along with 
# their favorite numbers.

numero = {
	"Josep": [1, 28], 
	"Martin": [30] ,
	"Carlos": [23, 3, 12, 2],
	"Alex": [10, 2, 243]
	}

for person, num in numero.items():
	print(f"{person.title()} favorite numbers are:")

	for n in num:
		print(n)