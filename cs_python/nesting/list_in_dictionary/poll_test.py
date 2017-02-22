# Python 2.7
# Example from Python Crash Course

# Here's another example of nesting a list inside of a dictionary
# looking at our previous example of a dicitonary of similar objects
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title()) # fixed attribute error ("languages" to language")
        
# test for remote username change
# second test, changing git config
