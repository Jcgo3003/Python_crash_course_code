"""
16-8. Recent Earthquakes: You can find data files containing 
information about the most recent earthquakes over 1-hour, 
1-day, 7-day, and 30-day periods online. 
Go to https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php 
and you’ll see a list of links to data sets for various time periods, 
focusing on earthquakes of different magnitudes. 
Download one of these data sets, and create a visualization of the 
most recent earthquake activity.
"""
import json 
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

file = "data/eq_data_2021_10_29.json"

with open(file) as f: 
	all_data = json.load(f)

eq_data = all_data["features"]
data_title = all_data["metadata"]["title"]

mags = [element["properties"]["mag"] for element in eq_data]
lons = [element["geometry"]["coordinates"][0] for element in eq_data]
lats = [element["geometry"]["coordinates"][1] for element in eq_data]
hover_text = [element["properties"]["title"] for element in eq_data]

# Map the earthquakes
data = [{ 
'type': 'scattergeo', 
'lon': lons, 
'lat': lats, 
'text': hover_text,
'marker': { 'size': [5*mag for mag in mags],
		'color': mags, 
		'colorscale': 'Viridis', 
		'reversescale': True, 
		'colorbar': {'title': 'Magnitude'},	
 },
}]

my_layout = Layout(title = data_title)

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="Global_earthquakes_2021_10_29.html")


