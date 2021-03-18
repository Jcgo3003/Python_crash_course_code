# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the 
# user can continue entering numbers even if they make a mistake and enter text instead 
# of a number.



while(True):

	number1 = input("Please, introduce a number\nPress 'q' for exit  ")
	if (number1 == "q"):
		print("Bye")
		break
	number2 = input("Please, introduce another number ")
	
	try:
		print(f"The addition is {int(number1 + number2)}\n")
	except ValueError:
		print("Err: please introduce a only numbers\n")



