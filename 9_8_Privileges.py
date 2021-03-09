# 9-8. Privileges: Write a separate Privileges class. The class should 
# have one attribute, privileges, that stores a list of strings as 
# described in Exercise 9-7. Move the show_privileges() method to this 
# class. Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges.

class User:
	""" Class user for """
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0

	def describe_user(self):
		print(f"First name:{self.first_name}")
		print(f"Last name:{self.last_name}")

	def greet_user(self):
		print(f"Hello {self.first_name} {self.last_name}")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

class Admin(User):
	"""docstring for Admin"""
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()


class Privileges:
	"""docstring for Privileges"""
	def __init__(self):
		self.privileges = ["Can add post", "Can delete post", "Can ban user"]

	def show_privileges(self):
		"""Listing all the privileges"""
		for item in self.privileges:
			print(item)


test = User("John", "Doe")	
test.greet_user()

capitan = Admin("Barba", "Roja")
capitan.privileges.show_privileges()


		