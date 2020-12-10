# 7-10. Dream Vacation: Write a program that polls users about their dream 
# vacation. Write a prompt similar to If you could visit one place in the world, 
# where would you go? Include a block of code that prints the results of the 
# poll.

flag = True
db = {}

while flag:
	print("Poll about world traveling")

	name = input("What's your name? ")
	answer = input("If you could visit one place in the world, where would you go? ")

	db[name] = answer

	question = input("There is someone else that would like to take the poll? y/n ")

	if question.lower() == "no":
		flag = False

for name, answer in db.items():
	print(f"{name} would like to go to {answer}")

