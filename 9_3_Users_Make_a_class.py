# 9-3. Users: Make a class called User. Create two attributes 
# called first_name and last_name, and then create several other 
# attributes that are typically stored in a user profile. Make a 
# method called describe_user() that prints a summary of the user’s 
# information. Make another method called greet_user() that prints 
# a personalized greeting to the user.

# Create several instances representing different users, and call 
# both methods for each user.

class User:
	""" Class user for """
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def describe_user(self):
		print(f"First name:{self.first_name}")
		print(f"Last name:{self.last_name}")

	def greet_user(self):
		print(f"Hello {self.first_name} {self.last_name}")

juan = User("Juan", "Gomez")
jose = User("Jose", "Obregon")
luis = User("Luis", "Gomez")

juan.describe_user()
juan.greet_user()
print()

jose.describe_user()
jose.greet_user()

print()

luis.describe_user()
luis.greet_user()

