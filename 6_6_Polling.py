# 6-6. Polling: Use the code in favorite_languages.py (page 97).

# • Make a list of people who should take the favorite languages 
# oll. Include some names that are already in the dictionary and 
# me that are not.

# • Loop through the list of people who should take the poll. 
# If they have already taken the poll, print a message thanking 
# hem for responding. If they have not yet taken the poll, print 
# message inviting them to take the poll.

favorite_languages = { 'jen': 'python', 
	'sarah': 'c', 
	'edward': 'ruby', 
	'phil': 'python', }

people_poll = ["adam", "george", "aaron", "sarah", "phil"]

todos = set(favorite_languages.keys()) | set(people_poll)



for person in todos:
	if person in favorite_languages.keys():	
		print(f"{person.title()} Thanks for take the poll")
	else:
		print(f"{person.title()} Please answer to our poll")


