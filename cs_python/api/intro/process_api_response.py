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

# Process the results.
print(response_dict.keys())
