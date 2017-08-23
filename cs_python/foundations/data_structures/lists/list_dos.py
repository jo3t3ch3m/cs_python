import random

# In Python, square brackets ([]) indicate a list.
# Each element in a list is separated by commas.
mc = ['redstone', 'pick axe', 'glass block', 'tnt block']

print("Below, a list of Minecraft items: ")
print(mc)

# USING SPECIFIC VALUES FROM A LIST
# Lists are 0-based
# They are ordered collections, so you can access any element in a list by telling Python the position
# or index, of the item you want.

def specificElement():
	print("\nThe third item in the list: " + mc[2] + ".")
	print("\nThe third item in the list(capitalized): " + mc[2].title() + ".")
	print("\nThe third item in the list(all caps): " + mc[2].upper() + ".")
specificElement()

# ACCESSING THE LAST ELEMENT FROM A LIST
def lastElement():
	print("\nThe last item in the list: " + mc[-1].upper() + ".")
lastElement()

# CHANGING ELEMENTS IN A LIST
mc[0] = 'grass block'

print("\nBelow, updated list of Minecraft items: ")
print(mc)

# ADDING ELEMENTS TO A LIST
mc.append('minecart')
print("\nBelow, updated list of Minecraft items: ")
print(mc)

# INSERTING ELEMENTS INTO A LIST
mc.insert(1, 'torch')
print("\nBelow, updated list of Minecraft items: ")
print(mc)

# REMOVING ITEMS FROM A LIST
del mc[3]
print("\nBelow, updated list of Minecraft items: ")
print(mc)

del mc[2]
print("\nBelow, updated list of Minecraft items: ")
print(mc)

del mc[1]
print("\nBelow, updated list of Minecraft items: ")
print(mc)

# ORGANIZING A LIST
mc.sort()
print("\nBelow, a sorted list of Minecraft items: ")
print(mc)

# FINDING THE LENGTH OF A LIST
print("\nHere is the length of our list so far: ")
len(mc)
print(len(mc))

# LOOPING THROUGH A LIST
print("\nHere, we are looping though all items in the list: ")
for items in mc:
	#print(items.title())
	print("\t" + items.title() + ", is an item found in the game, Minecraft" + "!")
	
	print("\t" + "This item does something, " + items.title() + ".\n")

