# 6-3. Glossary: A Python dictionary can be 
# used to model an actual dictionary. However, 
# o avoid confusion, let’s call it a glossary.

# • Think of five programming words you’ve 
# learned about in the previous chapters. 
# Use these words as the keys in your glossary, 
# and store their meanings as values.

# • Print each word and its meaning as neatly 
# ormatted output. You might print the word 
# followed by a colon and then its meaning, 
# or print the word on one line and then print 
# ts meaning indented on a second line. Use 
# the newline character (\n) to insert a blank 
# ne between each word-meaning pair in your 
# output.

glossary = {
	"list": "A collection of elements",
	"tupla": "A collection of elements but inmutable",
	"dictionary": "A collection of pairs elements"
	}

print(f"Lista es {glossary['list']}")
print(f"tupla es {glossary['tupla']}")
print(f"Dictionary es {glossary['dictionary']}")

for key, value in glossary.items(): 
	print(f"\nKey: {key}") 
	print(f"Value: {value}")



