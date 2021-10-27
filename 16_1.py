"""
16-1. Sitka Rainfall: Sitka is in a temperate rainforest, 
so it gets a fair amount of rainfall. In the data file 
sitka_weather_2018_simple.csv is a header called PRCP, 
which represents daily rainfall amounts. Make a visualization 
focusing on the data in this column. You can repeat the exercise 
for Death Valley if you’re curious how little rainfall occurs in 
a desert."""

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = "data/sitka_weather_2018_simple.csv"

with open(filename) as f: 
	reader = csv.reader(f)
	header_row = next(reader)

	# Get dates and the PRCP
	dates, prcp = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], "%Y-%m-%d")
		try: 
			
			rain = float(row[3])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date)
			prcp.append(rain)

# Plot the prcp and dates
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, prcp, c="red", alpha=0.3)
plt.fill_between(dates,prcp, facecolor="blue", alpha=0.4)

# Format plot
title = "Daily PRCP - Sitka weather 2018"
plt.title(title, fontsize=20)
fig.autofmt_xdate()
plt.ylabel("", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()





