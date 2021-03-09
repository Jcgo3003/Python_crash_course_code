from user import User
import privileges 

class Admin(User):
	"""docstring for Admin"""
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = privileges.Privileges()
