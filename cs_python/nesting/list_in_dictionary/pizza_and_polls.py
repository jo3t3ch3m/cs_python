# Python 2.7
# example from Python Crash Course by Eric Matthes
# store info about a pizza being ordered
# list in a dictionary
pizza = {
  'crust':'thick',
  'toppings': ['mushrooms', 'pepperoni', 'extra cheese'],
}

# summarize the order:
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
  print("\t" + topping)
  
  # Let's look at another example...
  # From our look at the similar objects dictionary
  # where we look at a poll taken from a population for favorite programming languages
  
favorite_languages = {
  'jen': ['python', 'ruby'],
  'sarah': ['c'],
  'edward': ['ruby', 'go'],
  'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
  print("\n" + name.title() + "'s favorite languages are:")
  for language in languages:
    print("\t" + language.title())      # simple fix to attr. error ("languages" changed to "language")
