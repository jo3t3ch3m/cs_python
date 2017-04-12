"""
To make a visualization that shows the relative popularity of
Python projects on GitHub, we'll make an interactive bar chart.
The height of each bar will represent the number of stars the project has acquired.
By cliking a bar, you will be taken to that project's home on GitHub.
"""
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
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


# Pygal
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Make visualization:
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')

    
# Examine the first repository.
repo_dict = repo_dicts[0]


# Pulling some values from the keys:
# ** A **
print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])
# ^^ A ^^

print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

# So this returns a lot of information about each repo.
# Let's pull out the values for some of the keys in repo_dict at # ** A ** above.


# At ** A **, we print out values for several keys from the first repo's dictonary.


