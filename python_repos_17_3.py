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
	status_code = r.status_code
	# print(f'Status code: {status_code}' )

	# Store API response in a variable
	response_dict = r.json()
	count_total_repositories = response_dict['total_count']

	# print(f"Total repositories: {count_total_repositories}")
	
	repo_dicts = response_dict['items']
	count_responsed_repositories = len(repo_dicts)
	# print(f"Repositories returned: {len(repo_dicts)}")

	# print("\nSelected information about each repository:")
	dict = []
	for repo_dict in repo_dicts:
		dict_temp = { "Name": repo_dict['name'], 
		"Owner": repo_dict['owner']['login'], 
		"Stars": repo_dict['stargazers_count'], 
		"Repository": repo_dict['html_url'], 
		"Created": repo_dict['created_at'], 
		"Updated": repo_dict['updated_at'], 
		"Description": repo_dict['description'],}

		dict.append(dict_temp)
	    

	return [status_code, count_total_repositories, count_responsed_repositories, dict] 

