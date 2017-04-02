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

    gameDisplay.fill(white)
    
# DRAW RECTANGLE:
    pygame.draw.rect(gameDisplay, black, [400, 300, 10, 10]) # (WHERE, COLOR, SPECIFY RECTANGLE SIZE IN A LIST) 
# DRAW ANOTHER RECTANGLE:
#    pygame.draw.rect(gameDisplay, red, [400, 300, 10, 10])

# MORE EFFICIENT WAY TO DRAW RECTANGLE USING FILL:
    gameDisplay.fill(red, rect = [200, 200, 50, 50])
    
    pygame.display.update() 





pygame.quit()
quit()






