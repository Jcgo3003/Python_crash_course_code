# 4-9. Cube Comprehension: Use a list comprehension to generate a list 
# of the first 10 cubes.


cube = [number**3 for number in range(1, 11) ]
print(*cube)