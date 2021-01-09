# 9-1. Restaurant: Make a class called Restaurant. The __init__() method 
# for Restaurant should store two attributes: a restaurant_name and a 
# cuisine_type. Make a method called describe_restaurant() that prints 
# these two pieces of information, and a method called open_restaurant() 
# that prints a message indicating that the restaurant is open.

# Make an instance called restaurant from your class. Print the two 
# attributes individually, and then call both methods.

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


french = Restaurant("La maison de Louis", "French cuisine")

print(french.restaurant_name)
print(french.cuisine_type)
print()
french.describe_restaurant()
print()
french.open_restaurant()