"""
15-10. Practicing with Both Libraries: Try using Matplotlib 
to make a die-rolling visualization, and use Plotly to make 
the visualization for a random walk. (You’ll need to consult 
the documentation for each library to complete this exercise.)
"""

""" Using Matplotlib used to visualise the results of rolling two dice 1000 times """
import matplotlib.pyplot as plt
from dice import Dice

# Create two D6 dice. 
dice_1 = Dice() 
dice_2 = Dice()

# Make some rolls, and store results in a list. 
results = [dice_1.roll() + dice_2.roll() for roll_num in range(1000)]

# Analyze the results.
max_result = dice_1.num_sides + dice_2.num_sides
frequencies = [results.count(value)  for value in range(2, max_result+1)]

# Plot the points in the frecuency of numbers
plt.style.use("classic")
fig, ax = plt.subplots()

x_values = list(range(2, max_result+1))

# Imprimiendo los resultados
ax.scatter(x_values, frequencies, s=100)

plt.show()
