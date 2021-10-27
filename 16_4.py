"""
16-4. Automatic Indexes: In this section, we hardcoded the 
indexes corresponding to the TMIN and TMAX columns. 
Use the header row to determine the indexes for these values, 
so your program can work for Sitka or Death Valley. 
Use the station name to automatically generate an 
appropriate title for your graph as well.
"""
import csv
from datetime import datetime

import matplotlib.pyplot as plt

file = "data/sitka_weather_2018_simple.csv"

with open(file) as f: 
	reader = csv.reader(f)
	header_row = next(reader)
	
	# Getting the righ data on place
	for x in range(len(header_row)):
		if(header_row[x] == "TMIN"):
			tmin_place = x
		if(header_row[x] == "TMAX"):
			tmax_place = x
		if(header_row[x] == "STATION"):
			station_place = x
		if(header_row[x] == "DATE"):
			date_place = x

	dates, highs, lows = [], [], []

	for row in reader:
		current_date = datetime.strptime(row[date_place], "%Y-%m-%d")
		try:
			high = int(row[tmax_place])
			low = int(row[tmin_place])
		except ValueError:
			print(f"Value error in date {current_date}")
		else:
			dates.append(current_date)	
			highs.append(high)
			lows.append(low)
			station = row[station_place]


# Ploting all the info
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.3)

# Format plot
plt.title("Daily high and low temperatures for {}".format(station), fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (f)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()


