def suma(x):
	""" A function to sum a number digits. """
	digits = str(x)

	while (len(digits) > 1):
		suma = 0
		for i in range(len(digits)): 

			suma += int(digits[i])
		digits = str(suma)


	return suma







