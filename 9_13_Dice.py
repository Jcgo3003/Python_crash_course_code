# 9-13. Dice: Make a class Die with one attribute called sides, which has a default 
# value of 6. Write a method called roll_die() that prints a random number between 
# 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.

from random import randint

class Dice:
	"""A class for ramdonly get some numbers"""
	def __init__(self, sides=6):
		self.sides = sides

	def roll_dice(self):
		"""Rolling the dice"""
		numero = randint(1, self.sides)
		print(f"Rolling Dice\n...\n..\n.\n{numero}")

dado = Dice(10)
for x in range (0, 10):
	dado.roll_dice()