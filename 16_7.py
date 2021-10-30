"""
16-7. Automated Title: In this section, we specified 
the title manually when defining my_layout, which means 
we have to remember to update the title every time the 
source file changes. Instead, you can use the title for 
the data set in the metadata part of the JSON file. 
Pull this value, assign it to a variable, and use this 
for the title of the map when you’re defining my_layout.
"""
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data
file = "data/eq_data_30_day_m1.json"

with open(file) as f:
	all_eq_data = json.load(f)

all_features = all_eq_data["features"]
title_file = all_eq_data["metadata"]["title"]


# Solved with compresed lists
mags = [element["properties"]["mag"] for element in all_features]
lons = [element["geometry"]["coordinates"][0] for element in all_features]
lats = [element["geometry"]["coordinates"][1] for element in all_features]
hover_texts = [element["properties"]["title"] for element in all_features]

# Getting all the data tougether
data = [{
	"type": "scattergeo",
	"lon": lons,
	"lat": lats,
	"text": hover_texts,
	"marker": { "size": [5*mag for mag in mags], 
				"color": mags,
				"colorscale": "Viridis",
				"reversescale": True,
				"colorbar": {"title": "Magnitude"},
	      		},
}]

my_layout = Layout(title= title_file)

fig = { "data": data, "layout": my_layout}
offline.plot(fig, filename="global-earthquakes.html")


