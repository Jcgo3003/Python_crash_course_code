"""
15-9. Die Comprehensions: For clarity, the listings 
in this section use the long form of for loops. 
If you’re comfortable using list comprehensions, 
try writing a comprehension for one or both of the 
loops in each of these programs.
"""
from plotly.graph_objs import Bar, Layout 
from plotly import offline
from dice import Dice

# Create two D6 dice. 
dice_1 = Dice() 
dice_2 = Dice()

# Make some rolls, and store results in a list. 
results = [dice_1.roll() + dice_2.roll() for roll_num in range(1000)]

# Analyze the results.
max_result = dice_1.num_sides + dice_2.num_sides
frequencies = [results.count(value)  for value in range(2, max_result+1)]

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times', 
	yaxis=y_axis_config) 

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')

