# # 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 
# five letters. Randomly select four numbers or letters from the list and print 
# a message saying that any ticket matching these four numbers or letters wins 
# a prize.

from random import choice


numeros = (432, 123, 892, 231, 392, 503, 923, 692, 102, 837, "bol", "snt", "rul", "tue", "uee")
print("The winning numbers are")
for x in range (0, 4):
	print(choice(numeros))