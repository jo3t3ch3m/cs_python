import urllib, json
url = 'https://secure.techemstudios.com/classes.json'
response = urllib.urlopen(url)
data = json.load(response)
print data
