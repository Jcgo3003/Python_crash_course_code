# 7-6. Three Exits: Write different versions of either Exercise 7-4 
# or Exercise 7-5 that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 
# 'quit' value.

prompt = "How are you? "
flag = True

while flag:
	value = input(prompt)
	print(value)
	
	if value < 3:
		print("Your ticket is on us")
		flag = False
	elif value < 13:
		print("Your ticket is $10")
		flag = False
	elif value > 12:
		print("Your ticket is $15")
		flag = False
	else:
		print("Quit")
		break


