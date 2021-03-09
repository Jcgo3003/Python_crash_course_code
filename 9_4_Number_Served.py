# 9-4. Number Served: Start with your program from 
# Exercise 9-1 (page 162). Add an attribute called 
# number_served with a default value of 0. Create 
# an instance called restaurant from this class. 
# Print the number of customers the restaurant has 
# served, and then change this value and print it 
# again.

# Add a method called set_number_served() that lets 
# you set the number of customers that have been 
# served. Call this method with a new number and 
# print the value again.

# Add a method called increment_number_served() 
# that lets you increment the number of customers 
# who’ve been served. Call this method with any 
# number you like that could represent how many 
# customers were served in, say, a day of business.

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

restaurant = Restaurant("Vapiano", "Italian")
restaurant.describe_restaurant()

print(f"Number served {restaurant.number_served}")

print("---- Updating data ----")
restaurant.number_served = 10
print(f"Number served {restaurant.number_served}")

print("---- Updating data after method set_number_served ----")
restaurant.set_number_served(20)
print(f"Number served {restaurant.number_served}")

print("---- Updating data after method increment_number_served ----")
restaurant.increment_number_served()
print(f"Number served {restaurant.number_served}")





