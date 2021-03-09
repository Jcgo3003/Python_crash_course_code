# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.



def find_it(seq):
    dic = {}
    lista_seq = set(seq)

    for elemento in lista_seq:
    	dic[elemento] = 0
    	while elemento in seq:
    		dic[elemento] += 1
    		seq.remove(elemento)

    for key, value in dic.items():
    	if not value % 3 == 0:
    		return key

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))


# Respuestas de la comunidad

# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i

# def find_it(seq):
#     return [x for x in seq if seq.count(x) % 2][0]

# def find_it(xs):
#     return reduce(operator.xor, xs)


# from collections import Counter
# def find_it(l):
#     return [k for k, v in Counter(l).items() if v % 2 != 0][0]

Investigar .count