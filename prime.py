""" A function to find if a number is a prime number """

def prime(x):
	i = 2
	while(i < x):
		if(x % i == 0): 
			return 0
		i += 1
	return x

print(prime(4))