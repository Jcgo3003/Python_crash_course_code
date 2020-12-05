# 5-11. Ordinal Numbers: Ordinal numbers indicate their 
# position in a list, such as 1st or 2nd. Most ordinal 
# numbers end in th, except 1, 2, and 3.

# • Store the numbers 1 through 9 in a list.

# • Loop through the list.

# • Use an if- elif- else chain inside the loop to print 
# the proper ordinal ending for each number. Your output 
# should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and 
#  result should be on a separate line.

numeros = list(range(1, 11))

for numero in numeros:
	if numero == 1:
		print(f"{numero}st")
	elif numero == 2:
		print(f"{numero}nd")
	elif numero == 3:
		print(f"{numero}rd")
	else:
		print(f"{numero}th")
