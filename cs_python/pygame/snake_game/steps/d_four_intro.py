# MAKING A SNAKE GAME


# import the pygame module:
import pygame

pygame.init()

# COLORS:

black = (0, 0, 0)          # (RED, GREEN, BLUE)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))


pygame.display.set_caption('Slither')




gameEXIT = False


# most basic way to draw something to the screen is "fill"

# GAME LOOP (main loop):
while not gameEXIT: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEXIT = True 

# GENERATE A WHITE BACKGROUND:

    gameDisplay.fill(white) # after you've done an action like this, you must update the display
    pygame.display.update() # updates the background to be filled in with white





pygame.quit()
quit()






