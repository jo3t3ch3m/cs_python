# Python 2.7
# Solution from the Python Crash Course Book 6-9. Favorite Places
# A simple program showing a nested list in a dictionary
# Three names are used as keys, and each person's favorite place as the nested list value

favorite_cities = {
    'albert': ['paris', 'richmond', 'tijuana'],
    'watson': ['chicago', 'tokyo', 'boston'],
    'crick': ['tokyo', 'sacramento'],
    }
for name, cities in favorite_cities.items():
    print("\n" + name.title() + "'s favorite cities are:")
    for city in cities:
        print("\t" + city.title())
