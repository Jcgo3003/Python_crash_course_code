from plotly.graph_objs import Bar, Layout 
from plotly import offline
from dice import Dice

# Create two D6 dice. 
dice_1 = Dice() 
dice_2 = Dice()

# Make some rolls, and store results in a list. 
results = []  
for roll_num in range(20):
	result = dice_1.roll() + dice_2.roll()
	results.append(result)

results = [dice_1.roll() + dice_2.roll() for roll_num in range(20)]


print(results)


max_result = dice_1.num_sides + dice_2.num_sides

frequencies = [results.count(value)  for value in range(2, max_result+1)]

print(frequencies)