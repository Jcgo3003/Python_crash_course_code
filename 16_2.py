import csv
from datetime import datetime

"""
16-2. Sitka–Death Valley Comparison: The temperature scales on 
the Sitka and Death Valley graphs reflect the different data ranges. 
To accurately compare the temperature range in Sitka to that of Death 
Valley, you need identical scales on the y-axis. Change the settings 
for the y-axis on one or both of the charts in Figures 16-5 and 16-6. 
Then make a direct comparison between temperature ranges in Sitka and 
Death Valley (or any two places you want to compare).
"""
import matplotlib.pyplot as plt

death_valley = 'data/death_valley_2018_simple.csv'
sitka = 'data/sitka_weather_2018_simple.csv'

with open(death_valley) as f1:
	reader_death_valley = csv.reader(f1)
	header_row_death_valley = next(reader_death_valley)

	# Get dates, and high and low temperatures for the death valley. 
	dates, highs_death_valley, lows_death_valley = [], [], []

	for row_death_valley in reader_death_valley:
		current_date = datetime.strptime(row_death_valley[2], "%Y-%m-%d")
		try:
			high = int(row_death_valley[4])
			low = int(row_death_valley[5])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date)
			highs_death_valley.append(high)	
			lows_death_valley.append(low)

with open(sitka) as f2:
	reader_sitka = csv.reader(f2)
	header_row_sitka = next(reader_sitka)
	
	highs_sitka, lows_sitka = [], []

	# Get high and low temperatures
	for row_sitka in reader_sitka:
		try:
			high = int(row_sitka[5])
			low = int(row_sitka[6])
		except:
			print(f"Missing data in sitka row {row}")
		else:
			highs_sitka.append(high)
			lows_sitka.append(low)




# Plot the high and low temperatures. 
plt.style.use('seaborn') 
fig, ax = plt.subplots()
ax.plot(dates, highs_death_valley, c='red', alpha=0.7)
ax.plot(dates, lows_death_valley, c='blue', alpha=0.7)
ax.plot(dates, highs_sitka, c='red', alpha=0.7)
ax.plot(dates, lows_sitka, c='blue', alpha=0.7)
ax.axis([dates[0], dates[-1], 20, 140])
plt.fill_between(dates, highs_death_valley, lows_death_valley, facecolor='yellow', alpha=0.4)
plt.fill_between(dates, highs_sitka, lows_sitka, facecolor='green', alpha=0.4)

# Format plot
title = "Daily high and low temperatures - 2018\nDeath Valley, CA" 
plt.title(title, fontsize=20)
fig.autofmt_xdate()
plt.ylabel("Temperatuer (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()

