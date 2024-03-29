"""
16-6. Refactoring: The loop that pulls data from 
all_eq_dicts uses variables for the magnitude, longitude, 
latitude, and title of each earthquake before appending 
these values to their appropriate lists. This approach 
was chosen for clarity in how to pull data from a JSON 
file, but it’s not necessary in your code. Instead of using 
these temporary variables, pull each value from eq_dict and 
append it to the appropriate list in one line. Doing so should 
shorten the body of this loop to just four lines.
"""
import json
from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline

# Explore the structure of the data
filename = "data/eq_data_30_day_m1.json"

with open(filename) as f:
	all_eq_data = json.load(f)

	
all_eq_dicts = all_eq_data['features']

# Solved doing some little modifications to the code
mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dicts:
	mags.append(eq_dict['properties']['mag']) 
	lons.append(eq_dict['geometry']['coordinates'][0]) 
	lats.append(eq_dict['geometry']['coordinates'][1])
	hover_texts.append(eq_dict["properties"]["title"])

# Solved with compresed lists
mags = [element["properties"]["mag"] for element in all_eq_dicts]
lons = [element["geometry"]["coordinates"][0] for element in all_eq_dicts]
lats = [element["geometry"]["coordinates"][1] for element in all_eq_dicts]
hover_texts = [element["properties"]["title"] for element in all_eq_dicts]


print(hover_texts)
# Map the earthquakes.
# data = [{ 
# 'type': 'scattergeo', 
# 'lon': lons, 
# 'lat': lats, 
# 'text': hover_texts,
# 'marker': { 'size': [5*mag for mag in mags],
# 		'color': mags, 
# 		'colorscale': 'Viridis', 
# 		'reversescale': True, 
# 		'colorbar': {'title': 'Magnitude'},	
#  },
# }]


# # my_layout = Layout(title='Global Earthquakes') 

# # fig = {'data': data, 'layout': my_layout} 
# # offline.plot(fig, filename='global_earthquakes.html')


