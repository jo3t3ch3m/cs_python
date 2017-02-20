# Python 2.7
# example from Python Crash Course by Eric Matthes

# you can store different kinds of information about one object in a dictionary,
# you can also use a dictionary to store one kind of information about many objects.

# Let's say we wanted to poll a number of people and ask them what their favorite programming language is.
# A dictionary can be useful for storing the results of a simple poll:

favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
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
