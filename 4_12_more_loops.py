# 4-12. More Loops: All versions of foods.py in this section have 
# avoided using for loops when printing to save space. Choose a 
# version of foods.py, and write two for loops to print each list 
# of foods.

pizza = ["Hawuaiana", "Chicago", "New York", "Home", "Mexicana", "Marguerita"]

pizza = ["Hawuaiana", "Chicago", "New York", "Home", "Mexicana", "Marguerita"]

friend_pizzas = pizza[:]

pizza.append("Pollo")

print("My favorites pizzas are:")
for x in pizza:
	print(x)

print("------------------------")
print("My friend's favorites pizzas are:")
for x in friend_pizzas:
	print(x)