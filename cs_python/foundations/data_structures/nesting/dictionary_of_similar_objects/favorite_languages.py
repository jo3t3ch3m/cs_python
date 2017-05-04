# Python 2.7
# example from Python Crash Course by Eric Matthes

# you can store different kinds of information about one object in a dictionary,
# you can also use a dictionary to store one kind of information about many objects.

# Let's say we wanted to poll a number of people and ask them what their favorite programming language is.
# A dictionary can be useful for storing the results of a simple poll:

favorite_languages = {
  'jen': ['python'],
  'sarah': ['c'],
  'edward': ['ruby', 'go'],   # <--- trying to figure what error came up when students nested the list 2/22/2017
  'phil': ['python'],
}

# As you can see, we've broken down a larger dicttionary into several lines.
# WHAT IS THE KEY?

    # Each key is the name of a person who responded to the poll.
    
# WHAT IS THE VALUE?

    # Each value is their language choice

# Now, let's use the dictionary...
# Given the name of a person who took the poll, you can easily look up their
# favorite language:

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")
# So what if you wanted to see everything stored in the poll's dictionary?
# USE A LOOP!

# First, let's loop through all key-value pairs:
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

# Looping through just the values in a dictionary:
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())

# now, check out the pizza.py program
    
