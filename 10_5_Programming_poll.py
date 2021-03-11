# 10-5. Programming Poll: Write a while loop that asks people why they like programming. 
# Each time someone enters a reason, add their reason to a file that stores all 
# the responses.

answer = "Bla"
all_answers = "responses.txt"
counter = 0

while answer != "exit":
	answer = input("Why you like programming? / Write exit to exit\n")
	if answer != "exit" and counter == 0:
		with open(all_answers, "w") as file:
			file.write(answer)
			file.write("\n")
			counter += 1
			print("Thank you for your reply\n")
	elif answer != "exit" and counter != 0:
		with open(all_answers, "a") as file:
			file.write(answer)
			file.write("\n")
			print("Thank you for your reply\n")
print("Bye")
