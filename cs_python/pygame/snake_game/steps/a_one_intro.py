# import the pygame module:
import pygame

x = pygame.init() #this function initializes all of the pygame modules we'll use
print(x)
# this funcion returns a tuple
# You could run:
# x = pygame.init()
# print(x)
# When you run the above, it returns a tuple that relays successes and failures
# x being the successes
# In other words, (x, y) is equal to (success #, fail #)

# Next, we'll need to make our surface
# Arguably the most important part of pygame
# Think of the surface as a blank piece of paper or canvas that we'll "draw" our objects to

# SURFACE:
gameDisplay = pygame.display.set_mode((800, 600)) # will have one paremeter for now, a tuple

# This will return a pygame.surface object

# example: gameDisplay = pygame.display.set_mode((800, 600)) <--- sets the size of the surface

# We will update the surface later

pygame.display.update() # pygame.display.flip() does the exact same thing as update()

# Motion in a game is actually like a flip book
# motion is only precieved motion, it is a collection of frames
# you start with one frame, then update that frame to make the next and so on, all together it looks like there is fluid motion (hopefully fluid)

# ALL THE ABOVE IS REQUIRED FOR YOUR GAME TO RUN

# TO EXIT PYGAME:
pygame.quit() # uninitializes all of the above
quit() # A window pops up and goes away

# ALL THE ABOVE IS THE "SKELETON" OF PYGAME, the "bare bones"

# THE "MUSCLES":

# more logic, and events we can use:

# 




