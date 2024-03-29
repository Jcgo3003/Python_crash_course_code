"""
15-8. Multiplication: When you roll two dice, 
you usually add the two numbers together to get the result. 
Create a visualization that shows what happens if you 
multiply these numbers instead.
"""
from plotly.graph_objs import Bar, Layout 
from plotly import offline
from dice import Dice

# Create two D6 dice. 
dice_1 = Dice() 
dice_2 = Dice()

# Make some rolls, and store results in a list. 
results = []  
for roll_num in range(1_000_000):
	result = dice_1.roll() * dice_2.roll()
	results.append(result)

# Analyze the results.
frequencies = []
max_result = dice_1.num_sides * dice_2.num_sides

for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1,000,000 times and multiplying the results', 
	yaxis=y_axis_config) 

offline.plot({'data': data, 'layout': my_layout}, filename='Multiply_d6.html')