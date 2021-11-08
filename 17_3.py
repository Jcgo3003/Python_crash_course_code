'''
17-3. Testing python_repos.py: In python_repos.py, we printed 
the value of status_code to make sure the API call was successful. 
Write a program called test_python_repos.py that uses unittest to 
assert that the value of status_code is 200. Figure out some other 
assertions you can make—for example, that the number of items 
returned is expected and that the total number of repositories 
is greater than a certain amount.

'''

import requests

def api_response():
	# Make and API call and store the response
	url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
	headers = { 'Accept': 'application/vnd.github.v3+json'}
	r = requests.get(url, headers=headers)
	print(f'Status code: {r.status_code}' )

