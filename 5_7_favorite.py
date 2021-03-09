# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series 
# of independent if statements that check for certain fruits in your list.

# • Make a list of your three favorite fruits and call it favorite_fruits.

# • Write five if statements. Each should check whether a certain kind of fruit is in 
# your list. If the fruit is in your list, the if block should print a statement, such 
# as You really like bananas!

favorite_fruits = ["Banana", "Manzana", "Fresa", "Naranja", "Melon"]

# selection = input("Dime una fruta ")
# mi solucion alejada de lo que me pidieron
# if selection.title() in favorite_fruits:
# 	print(f"You really like {selection.title()}")

selection = "Melon"

if selection == "Banana":
	print("You really like babanas")
if selection == "Manzana":
	print("You really like Manzana")
if selection == "Fresa":
	print("You really like Fresa")
if selection == "Naranja":
	print("You really like Naranja")
if selection == "Melon":
	print("You really like Melon")

