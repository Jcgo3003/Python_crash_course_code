# 7-8. Deli: Make a list called sandwich_orders and fill it with the names 
# of various sandwiches. Then make an empty list called finished_sandwiches. 
# Loop through the list of sandwich orders and print a message for each order, s
# uch as I made your tuna sandwich. As each sandwich is made, move it to the 
# list of finished sandwiches. After all the sandwiches have been made, print a 
# essage listing each sandwich that was made.


sandwich_orders = ["Club", "French", "Cheese", "Doble Chesse"]

finished_sandwiches = [ ]

while sandwich_orders:
	temp =  sandwich_orders.pop()

	print(f"I made your {temp}")
	finished_sandwiches.append(temp)

print(f"These are the finished orders \n{finished_sandwiches}")