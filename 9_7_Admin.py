# 9-7. Admin: An administrator is a special kind of user. Write a class 
# called Admin that inherits from the User class you wrote in Exercise 9-3 
# (page 162) or Exercise 9-5 (page 167). Add an attribute, privileges, 
# that stores a list of strings like "can add post", "can delete post", 
# "can ban user", and so on. Write a method called show_privileges() 
# that lists the administrator’s set of privileges. Create an instance 
# of Admin, and call your method.

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

test = User("John", "Doe")	

class Admin(User):
	"""docstring for Admin"""
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = ["Can add post", "Can delete post", "Can ban user"]

	def show_privileges(self):
		"""Listing all the privileges"""
		print(f"The Admin {self.first_name} {self.last_name}")
		print("As the following privileges:")
		for item in self.privileges:
			print(item)

director = Admin("Simmour", "Skynner")

director.show_privileges()
