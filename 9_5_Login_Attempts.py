# 9-5. Login Attempts: Add an attribute called 
# login_attempts to your User class from Exercise 
# 9-3 (page 162). Write a method called increment_login 
# _attempts() that increments the value of login_attempts 
# by 1. Write another method called reset_login_attempts() 
# that resets the value of login_attempts to 0.

# Make an instance of the User class and call 
# increment_login_attempts() several times. Print 
# the value of login_attempts to make sure it was 
# incremented properly, and then call reset_login_attempts(). 
# rint login_attempts again to make sure it was reset 
# o 0.

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
test.increment_login_attempts()

print(f"The login attempts are {test.login_attempts}")

test.increment_login_attempts()
test.increment_login_attempts()
test.increment_login_attempts()
test.increment_login_attempts()
print("--- Updating data ---")
print(f"The login attempts are {test.login_attempts}")
print("--- Updating data ---")
test.reset_login_attempts()
print(f"The login attempts are {test.login_attempts}")