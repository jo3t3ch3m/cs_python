"""
Most APIs are rate-limited. This means there is a limit to how many
requests you can make in a certain amount of time.

For GitHub, you can check to see if you're coming to it's limits by
visiting https://api.github.com/rate_limit

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

# ** B **
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])
    
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

# Let's summarize the top repositories at ** B ** above.
    # When making avisulaization for this data, we probably waant to include more
    # than one repo. So, we'll write a loop to print selected information about each
    # of the repos returned by the API call so we can have them all 'visualized'.
