

class Privileges:
	"""docstring for Privileges"""
	def __init__(self):
		self.privileges = ["Can add post", "Can delete post", "Can ban user"]

	def show_privileges(self):
		"""Listing all the privileges"""
		for item in self.privileges:
			print(item)