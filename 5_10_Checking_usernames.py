# 5-10. Checking Usernames: Do the following to create a 
# program that simulates how websites ensure that everyone 
# has a unique username.

# • Make a list of five or more usernames called current_users.

# • Make another list of five usernames called new_users. Make 
# sure one or two of the new usernames are also in the 
# current_users list.

# • Loop through the new_users list to see if each new 
# username has already been used. If it has, print a message 
# that the person will need to enter a new username. 
# If a username has not been used, print a message saying 
# that the username is available.

# • Make sure your comparison is case insensitive. If 'John' 
# has been used, 'JOHN' should not be accepted. (To do this, 
# 	you’ll need to make a copy of current_users containing 
# 	the lowercase versions of all existing users.)

current_users = ["admin", "Damon", "David", "Kevin", "Janely", "Esther"]

new_users = ["Alexander", "Aron", "Thomas", "George", "Paul", "David", "Esther"]

copy_current_users = []

for users in current_users:
	copy_current_users.append(users.lower())

for new_user in new_users:
	if new_user.lower() in copy_current_users:
		print(f"{new_user} as been already taken, please create another username")
	else:
		print(f"{new_user} in available")





