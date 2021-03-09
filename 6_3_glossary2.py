# 6-4. Glossary 2: Now that you know how to loop through a 
# dictionary, clean up the code from Exercise 6-3 (page 99) 
# by replacing your series of print() calls with a loop that 
# runs through the dictionary’s keys and values. When you’re 
# sure that your loop works, add five more Python terms to 
# your glossary. When you run your program again, these new 
# words and meanings should automatically be included in the 
# output.

glossary = {
	"list": "A collection of elements",
	"tupla": "A collection of elements but inmutable",
	"dictionary": "A collection of pairs elements",
	"sets": "A collection of unique items",
	"print": "Prints variables or strings"
	}

for keys,  values in glossary.items():
		print(f"{keys} is {values}")


