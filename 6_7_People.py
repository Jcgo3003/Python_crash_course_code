# 6-7. People: Start with the program you wrote 
# for Exercise 6-1 (page 99). Make two new 
# dictionaries representing different people, 
# nd store all three dictionaries in a list 
# called people. Loop through your list of 
# people. As you loop through the list, print
#  everything you know about each person.

persona = {
	"nombre": "Juan", 
	"edad": 30, 
	"altura": "1.67m"
	}

persona2 = {
	"nombre": "Abril", 
	"edad": 28, 
	"altura": "1.60m"
	}

persona3 = {
	"nombre": "Raphael", 
	"edad": 35, 
	"altura": "1.70m"
	}

people = [persona, persona2, persona3]

for dic in people:
	print(dic)