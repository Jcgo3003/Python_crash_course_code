"""
17-2. Active Discussions: Using the data from hn_submissions.py, 
make a bar chart showing the most active discussions currently 
happening on Hacker News. The height of each bar should 
correspond to the number of comments each submission has. 
The label for each bar should include the submission’s 
title and should act as a link to the discussion page for 
that submission.
"""
from operator import itemgetter
import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and stero the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()
submission_dicts = []
article_title = []
article_score = []
for submission_id in submission_ids[:10]:
	# Make a separate API call for each submission
	url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
	r = requests.get(url)
	print(f"id: {submission_id}\tstatus: {r.status_code}")
	response_dict = r.json()

	article_title.append(response_dict['title'])
	article_score.append(response_dict['score'])

	# Build a dictionary for each article. 
	# submission_dict = {
	# 	'title': response_dict['title'],
	# 	'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
	# 	'score': response_dict['score'], 
	# }

	# submission_dicts.append(submission_dict)


submission_dicts = sorted(submission_dicts, key=itemgetter("score"), reverse=True)

# Make wisualization.
data = [{
	'type': 'bar',
	'x':  article_title,
	'y': article_score,
	'marker': {
		'color': 'rgb(60, 100, 150)',
		'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
		'opacity': 0.6,
	}
}]

my_layout = {
	'title': 'Best-scored articles in hacker-news',
	'titlefont': {'size': 28},
	'xaxis': {
		'title': 'Article',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14}, },
	'yaxis': { 
        'title': 'Stars', 
        'titlefont': {'size': 24}, 
        'tickfont': {'size': 14}, },
}

fig = {"data": data, 'layout': my_layout}
offline.plot(fig, filename="Top 10 hacker-news.html")
