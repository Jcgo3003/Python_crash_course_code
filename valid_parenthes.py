# Write a function called that takes a string of parentheses, and 
# determines if the order of the parentheses is valid. The function 
# should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false



# print(valid_parentheses(a))

def valid_parentheses(string):
	counter = 0
	flag = True
	for letter in string:
		if letter == "(" :
			counter += 1

		elif letter == ")":
			counter -= 1
		
		if counter < 0:
			flag = False
			break

	print("lba")		
	if counter != 0:
		flag = False

	return flag


print(valid_parentheses("(") )


# def valid_parentheses(string):
# 	caso = 0
# 	counter = 0
# 	x = 0
# 	while x < len(string):
# 		if string[x] == "(" and x == 0:
# 			counter += 1
# 			case = 3

# 		if string[x] == "(" and caso == 3:
# 			counter += 1
# 			caso = 1

# 		if string[x] == ")" and caso == 3:
# 			counter = 0

# 		if string[x] == ")" and caso == 1:
# 			counter -= 1
            


# 		if string[x] == ")" and caso == 2:
# 			counter -= 1
# 		x += 1

# 	if counter != 0:
# 		return False		
# 	else:
# 		return True


# a = "()"
