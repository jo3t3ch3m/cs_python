# Python 2.7

# First of all, don't forget that lines (like this one) starting with 
# the pound sign/hashtag are called "comments". We use them like I am 
# here -- to help explain your code to other humans. All of these 
# comment lines are ignored when your program is interpreted (run).
# They are ignored by the computer.

# Remember what the keyword "import" is doing here.
# And remember the term: identifier. "random" is an identifier for the
# imported library
import random

nouns = ["bird","dog","house"]
verbs = ["ate","bought","smelled"]

# Lists in Python are 0-based, meaning the first item in a list can be selected using
# syntax like nouns[0]. Thus, the random integer function is choosing one of
# the three items in the list by choosing a random integer between 0 and 2 (inclusive).
# When we use this bracket syntax, it is sometimes referred to as "indexing" the list.
# So, we would use the index "2" to select the third item, like nouns[2]. You can
# practice creating a list and indexing it using the Python interpreter like we do in class.
sub = nouns[random.randint(0,2)]
verb = verbs[random.randint(0,2)]
obj = nouns[random.randint(0,1)]

print("The " + sub + " " + verb + " the " + obj + ".")


# To illustrate how easy Python and its libraries make it to grab a list of
# 187 animals to select from for the subject of your sentence, we import a library
# called json which knows how to unpack data available on the web into
# a regular Python list.
import json

# The urllib2 library enables your program to connect to a website and, in this
# case, get some random data.
import urllib

# In one line of code we are connecting to a site, grabbing a random collection
# of 187 animal names and packing that into a Python list.
# Don't worry if this seems complicated -- we'll break this up and review every
# step again in class.
animals = json.load(urllib.urlopen('https://www.randomlists.com/data/animals.json'))['RandL']

# Now, we reload a subject randomly picked from our new big list of animals
sub = animals[random.randint(0,len(animals)-1)]

print("The " + sub + " " + verb + " the " + obj + ".")
