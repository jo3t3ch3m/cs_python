pizza = {
  'crust':'thick',
  'toppings': ['mushrooms', 'pepperoni', 'extra cheese'],
}

# summarize the order:
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
  print("\t" + topping)

print("\nAbove is an example of a pizza already built")

# starting program with user input:

def crust():
    crust = raw_input("\nType in the style of crust you want for your pizza")
    
