# 5-9. No Users: Add an if test to hello_admin.py to make sure 
# the list of users is not empty.

# • If the list is empty, print the message We need to find 
# some users!

# • Remove all of the usernames from your list, and make sure 
# he correct message is printed.

usuarios = ["admin", "Damon", "David", "Kevin", "Janely", "Esther"]

usuarios = []

if usuarios:
	for usuario in usuarios:
		if usuario == "admin":
			print(f"Hola admin, would you like to see a status report?")
		else:
			print(f"Hola, {usuario}")
else: 
	print("We need more users")