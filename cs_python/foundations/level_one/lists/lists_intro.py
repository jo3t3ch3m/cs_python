# Python 2.7

# This program shows the difference between a strings and lists
# with a quick introduction to using functions with a list

# activity template from Python for Kids by Jason Briggs

# This is my typical grocery list stored as one single STRING

grocery_list_for_Joe = ['eggs, milk, dandruff shampoo, holy grail, 2 african swallows, coconut']
#print(grocery_list_for_Joe)




# Below is my grocery list created as a LIST instead of a STRING:
	
grocery_list_for_Joe = ['eggs', 'milk', 'dandruff shampoo', 'holy grail', '2 african swallows', 'coconut']
#print(grocery_list_for_Joe)




# Creating a list takes a bit more than creating a string.
# But, a list is more useful than a string because it can be manipulated.

# For example, we can print the third item in our list (called the INDEX position) inside square brackets ([]):

#print(grocery_list_for_Joe[2])

# WAIT! isn't this the third item on our list? Yes, but lists in Python are 0-based, meaning the first item  in a list can be selected using syntax like [0].

# If the first item in a list is [0], then the second item in the list [1]





# You can also switch out an item in the list much more easily than you could than w/ a string.

# Let's say I need yogurt instead of dandruff shampoo, I can easily replace it.

#grocery_list_for_Joe[2] = 'yogurt'

#print(grocery_list_for_Joe)

# now the item in index postion 2 in my list, is replaced with 'yogurt'




# I can also show a subset of the items in my list by using a colon (:) inside square brackets.
#For example, to see the third to sixth items in my list (items from Monty Python) I would type the following:
	
#print(grocery_list_for_Joe[3:6])

# In other words, writing [3:6] is the same as saying "show the items from the index postion 3 up to index position 6"
# Or "show items 3, 4, 5"




# Lists can be used to store all sorts of items, like numbers:
	
some_numbers = [1, 2, 5, 10, 25]
#print(some_numbers)
#print(some_numbers[2])


# ADDING ITEMS TO A LIST

# To add items to a list, we use the append function.
# Remember a function is a chunk of code that we can reuse, that tells Python to do something

# For this case, the append function adds items to the end a list

# For example, let's add the item, avocado, to the end of my grocery list:
	
grocery_list_for_Joe.append('avocado')
#print(grocery_list_for_Joe)

# You can keep adding to your grocery list
# I'm going to add three more items

grocery_list_for_Joe.append('dragon egg')
grocery_list_for_Joe.append('apple')
grocery_list_for_Joe.append('banana')

#print(grocery_list_for_Joe)

# To add items to our list, we used the APPEND function

# Remember, a function is a chunk of code that tells Python to perform a specific action

# The function we just used (append), adds an item to the end of a list.



# REMOVING ITEMS FROM A LIST

# Let's say I realize I already have an item in my grocery list
# To remove items from a list, use the del command (short for delete).

# For example, to remove the fifth item in grocery_list_for_Joe, coconut, write:

del grocery_list_for_Joe[5]
#print(grocery_list_for_Joe)

# Remember that postions in a list start at zero, so grocery_list_for_joe[5] refers to the sixth item in my grovcery list.

# I realized I don't need those items I just recently added (dragon egg, 2 african swallows, banana)
# So I am going to remove those items:
	
del grocery_list_for_Joe[4]
del grocery_list_for_Joe[5]
del grocery_list_for_Joe[6] 

#print(grocery_list_for_Joe)

# LIST ARITHMETIC

# lists can also contain numbers and even store other lists

# We can join lists by adding them, just like with adding numbers, using a (+) sign.

# For example, suppose we two lists: list1, containing the numbers 1 through 4, and list2, containing some words.

# We can add them together using the print function and the + sign:
	
list1 = [1, 2, 3, 4]
list2 = ['I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']

#print(list1 + list2)

# We can also add the two lists and set the result equal to another variable.

list3 = ['I', 'ate', 'the', 'choclate', 'and', 'I', 'want', 'more']
list4 = list1 + list3
print(list4)

# So our new variable (list4) is equal to list1 and list3 together












