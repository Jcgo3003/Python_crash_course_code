"""
15-10. Practicing with Both Libraries: Try using Matplotlib 
to make a die-rolling visualization, and use Plotly to make 
the visualization for a random walk. (You’ll need to consult 
the documentation for each library to complete this exercise.)

Using Plotly to visualiaze a random walk  """

from plotly.graph_objs import Scatter, Layout
from plotly import offline
from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

x_random  = list (range(min(rw.x_values), max(rw.x_values)))
y_random  = rw.y_values

data = [ Scatter(x=x_random, y= y_random, line=None)]


x_axis_config = {'title': 'x axis', 'dtick': 1}
y_axis_config = {'title': 'y axis'}
my_layout = Layout(title='A visualisation of a random walk', 
	yaxis=y_axis_config) 

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')

