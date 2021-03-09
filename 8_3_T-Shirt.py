# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and 
# the text of a message that should be printed on the shirt. The function 
# should print a sentence summarizing the size of the shirt and the message 
# printed on it.

# Call the function once using positional arguments to make a shirt. Call the 
# function a second time using keyword arguments.

def make_shirt(size, text):
	""" Text and size into a same shirt """
	print(f"the size would be {size}")
	print(f"With the next message {text}")

make_shirt(12, "This is the great message for the T-Shirt")

make_shirt(18, "Bla bla bla bla")