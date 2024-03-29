""" 15-2. Colored Cubes: Apply a colormap to your cubes plot. """

import matplotlib.pyplot as plt 
import math


def cubic(rango):
	""" Function to plot a cubic variable, 
		taking x as a range of numbers """
	
	# Data
	valores = [(pow(x, 3)) for x in rango]

	plt.style.use("seaborn")
	fig, ax = plt.subplots()

	ax.plot(rango, valores,  linewidth=1)
	ax.scatter(rango, valores, c=valores, cmap=plt.cm.Blues, s=80)

	# Set chart title and label axes
	ax.set_title("Cubic numbers", fontsize=24)
	ax.set_xlabel("Value", fontsize=14)
	ax.set_ylabel("Square of value", fontsize=14)

	# Ste size of tick labels.
	ax.tick_params(axis="both", which='major', labelsize=10)

	plt.show()

# Range between 1 - 5
rango = range(1, 6)
cubic(rango)

# Range between 1 - 5000
rango = range(1, 5000)
cubic(rango)

