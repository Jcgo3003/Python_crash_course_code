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
