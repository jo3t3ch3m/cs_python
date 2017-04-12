"""

Rolling the Die
Before we create the visualization based on the Die class,
we'll roll a D6, print its results, then check if the results look reasonable.

"""

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
# analyzing the results, changing range of 100 to 1000
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

##print(results)


"""

Analyze the Results
We can analyze the results of rolling one D6 by counting how many times
each number is rolled.

"""

# Analyze the results:
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
