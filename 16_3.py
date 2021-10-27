"""
16-3. San Francisco: Are temperatures in San Francisco more 
like temperatures in Sitka or temperatures in Death Valley? 
Download some data for San Francisco, and generate a high-low 
temperature plot for San Francisco to make a comparison."""
import csv 
from datetime import datetime

import matplotlib.pyplot as plt

file = "data/los_angeles_2021.csv"

with open(file) as f:
	reader = csv.reader(f)
	header = next(reader)

	print(header)

	header = next(reader)
	print(header[4])
	print(header[5])

	dates, highs, lows = [], [], []

	for row in reader:
		current_date = datetime.strptime(row[2], "%Y-%m-%d")
		try: 
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Missing data for {current_date}")
		else: 
			dates.append(current_date)
			highs.append(high)
			lows.append(low)


# Plot the high and low temperatures
plt.style.use("classic")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.6)
ax.plot(dates, lows, c="green", alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.5)

# Format plot 
title = "Daily high and low temperatures - 2021 Los angeles"
plt.title(title, fontsize=20)
fig.autofmt_xdate()
plt.ylabel("Temerature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()








