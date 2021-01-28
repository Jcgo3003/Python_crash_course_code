q# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
#  Write a class called IceCreamStand that inherits from the Restaurant 
#  class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). 
#  Either version of the class will work; just pick the one you like better.
#  dd an attribute called flavors that stores a list of ice cream flavors.
#   Write a method that displays these flavors. Create an instance of 
#   IceCreamStand, and call this method.

class Restaurant:
	"""Restaurant class """

	def __init__(self, restaurant_name, cuisine_type):
		"""Declaring the variables"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Method to print out the information"""
		print(f"The name of the restaurant is {self.restaurant_name}")
		print(f"and is a {self.cuisine_type} restaurant.")

	def open_restaurant(self):
		print("The restaurant is open")

	def set_number_served(self, number_served):
		self.number_served = number_served

	def increment_number_served(self):
		self.number_served += 4


class IceCreamStand(Restaurant):
	"""docstring for IceCreamStand"""
	def __init__(self, restaurant_name, cuisine_type, flavor_day="Chocolate"):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ["Chocolate", "Lime", "Strawberry", "Orange"]
		self.flavor_day = flavor_day


	def display_flavors(self):
		""" Displaying the flavor"""
		print(f"The Ice Cream flavor can be {self.flavors}")

helado = IceCreamStand("Morena", "Ice Cream")

helado.display_flavors()

