# If we list all the natural numbers below 10 that are multiples of 3 
# or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples 
# of 3 or 5 below the number passed in.

# Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)

# Courtesy of projecteuler.net

def solution(number):
	numeros = list(range(0, number))
	suma = []
	for numero in numeros:
		if (numero % 3 and numero % 5) == 0 :
			suma.append(numero)
	return sum(suma)

# Solutiones de la comunidad
# def solution(number):
#     return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

# def solution(number):
#     sum = 0
#     for i in range(number):
#         if (i % 3) == 0 or (i % 5) == 0:
#             sum += i
#     return sum

#  def solution(number):
#     a3 = (number-1)/3
#     a5 = (number-1)/5
#     a15 = (number-1)/15
#     result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
#     return result