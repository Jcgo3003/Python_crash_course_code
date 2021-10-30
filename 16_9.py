"""
16-9. World Fires: In the resources for this chapter, 
you’ll find a file called world_fires_1_day.csv. 
This file contains information about fires burning in 
different locations around the globe, including the latitude 
and longitude, and the brightness of each fire. 
Using the data processing work from the first part of this 
chapter and the mapping work from this section, make a map 
that shows which parts of the world are affected by fires.

You can download more recent versions of this data at 
https://earthdata .nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data/. 
You can find links to the data in CSV format in the TXT section.
"""
import csv
from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


file = "data/fire_data_7_2021_10_29.csv"
# file = "data/fire_data_24h_2021_10_29.csv"

with open(file) as f:
	reader = csv.reader(f)
	header_row = next(reader)

# ['latitude', 'longitude', 'brightness', 'scan', 'track', 'acq_date', 'acq_time', 'satellite', 'confidence', 'version', 'bright_t31', 'frp', 'daynight']
# 0 - lat, 1 - lon, 3 - scan, 4-trak, 5 - date, 8 - confidence  
# To get the area of the fire I need to multiply scan and track by 375 and then get the area
	# Getting all the data I need
	lats, lons, areas, dates, confidence_list = [], [], [], [], []
	
	for row in reader:
		current_date = datetime.strptime(row[5], "%Y-%m-%d")
		try:
			lat = float(row[0])
			lon = float(row[1])
			area = (float(row[3])* 375) * (float(row[4])* 375)
			confidence = int(row[8])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			# Addinng only fires larger than 1,000,000 m2
			if area > 1_000_000:
				dates.append(current_date)
				lats.append(lat)
				lons.append(lon)
				# Getting 6 ceros off of the count
				areas.append(area / 1_000_000)
				confidence_list.append(f"Long: {area}m2\nLevel of confidence in the data {confidence}%")


# Map of fires
data = [{
	"type": "scattergeo",
	"lon": lons,
	"lat": lats,
	"text": confidence_list,
	"marker": { "size": [20*area for area in areas],
			"color": areas,
			"colorscale": "Viridis",
			"colorbar": {"title": "Size of fire on 1Million m2"},
			},
}]


my_layout = Layout(title="Global Fires")

fig = { "data": data, "layout": my_layout}
offline.plot(fig, filename="global_fires.html")

