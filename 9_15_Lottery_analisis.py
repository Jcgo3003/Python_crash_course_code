# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win 
# the kind of lottery you just modeled. Make a list or tuple called my_ticket. 
# Write a loop that keeps pulling numbers until your ticket wins. Print a message 
# reporting how many times the loop had to run to give you a winning ticket.

from random import choice


numeros = (432, 123, 892, 231, 392, 503, 923, 692, 102, 837, "bol", "snt", "rul", "tue", "uee")

my_ticket = (123)
times = 0

while True:
	winner = choice(numeros)
	times += 1
	if (my_ticket == winner):
		break

print(f"I won at the game number {times}")



