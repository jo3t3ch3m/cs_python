# A simple program to show a list in a dictionary

# storing inforamtion about a pizza being ordered

pizza = {
    'crust':'thick',
    'toppings':['mushrooms', 'pepperoni', 'extra cheese']
    }

# summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

