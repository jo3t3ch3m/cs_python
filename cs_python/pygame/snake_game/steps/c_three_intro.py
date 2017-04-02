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

while not gameEXIT: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # "if the event type is a pygame.QUIT: what do we want to happen?" -we want it to quit
            gameEXIT = True # will stop running this loop

        # eventually you will have a few more event conditions:
        if event.type == pygame.KEYUP:
            gameEXIT = True
        if event.type == pygame.KEYDOWN:
            gameEXIT = True
        if event.type == pygame.MOUSEMOTION:
            gameEXIT = True




# TO EXIT PYGAME:
pygame.quit() # uninitializes all of the above
quit() # A window pops up and goes away






