# 9-2. Three Restaurants: Start with your class from Exercise 9-1. 
# Create three different instances from the class, and call 
# describe_restaurant() for each instance.

class Restaurant:
	"""Restaurant class """

	def __init__(self, restaurant_name, cuisine_type):
		"""Declaring the variables"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Method to print out the information"""
		print(f"The name of the restaurant is {self.restaurant_name}")
		print(f"and is a {self.cuisine_type} restaurant.")

	def open_restaurant(self):
		print("The restaurant is open")

italian = Restaurant("Luigi's", "Italian")
italian.describe_restaurant()

print()

mexican = Restaurant("La casa de mama", "Mexican")
mexican.describe_restaurant()

print()

indian = Restaurant("Varanasi", "Indian")
indian.describe_restaurant()

