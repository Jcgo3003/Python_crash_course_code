# 7-2. Restaurant Seating: Write a program that asks the user 
# how many people are in their dinner group. If the answer is 
# more than eight, print a message saying they’ll have to wait 
# for a table. Otherwise, report that their table is ready.

num_seatings = int(input("How many people is comming? "))

if num_seatings > 8:
	print("You have to wait")
else:
	print("The table is ready")





