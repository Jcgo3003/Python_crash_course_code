#4-5. Summing a Million: Make a list of the numbers 
# from one to one million, and then use min() and max() 
# to make sure your list actually starts at one and ends 
# at one million. Also, use the sum() function to see how 
# quickly Python can add a million numbers.

mill = list(range(1, 100001))

# Printing the results
print(f"The minimun number in mill is {min(mill)}")
print(f"The maximun number in mill is {max(mill)}")
print(f"The total sum in mill is {sum(mill)}")
