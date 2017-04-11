"""
A simple program that issues an API call and process the results by
identifying the most starred Python projects on GitHub.

"""

import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Examine the first repository.
repo_dict = repo_dicts[0]

# ***A***
print
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

# So this returns a lot of information about each repo.
# Let's pull out the values for some of the keys in repo_dict at # ***A*** above ^^^
