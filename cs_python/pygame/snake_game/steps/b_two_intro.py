# MAKING A SNAKE GAME


# import the pygame module:
import pygame

x = pygame.init()
print(x)


# SURFACE:
gameDisplay = pygame.display.set_mode((800, 600))

# Creating a game name (a caption):
pygame.display.set_caption('Slither')


pygame.display.update()

# Specify constant variable:
gameEXIT = False
 # creating simple game loop:

while not gameEXIT: # "while gameEXIT is false"
    for event in pygame.event.get(): # "event handling"
        print(event) # once you run this, you can type in keys and see the events pop up in the interpreter
        
# you decide how the events are handled

# http://www.pygame.org/docs/ref/event.html shows all the events that could happen




# TO EXIT PYGAME:
pygame.quit() # uninitializes all of the above
quit() # A window pops up and goes away






