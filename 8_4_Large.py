# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are 
# large by default with a message that reads I love Python. Make a large 
# shirt and a medium shirt with the default message, and a shirt of any 
# size with a different message.


def make_shirt(text, size="large"):
	""" Text and size into a same shirt """
	print(f"the size would be {size}")
	print(f" {text}")

make_shirt("I love Python")

make_shirt("Bla bla", "medium" )

make_shirt("More bla bla", "any size" )