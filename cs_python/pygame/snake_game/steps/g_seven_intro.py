# MAKING A SNAKE GAME
# allowing user to press and hold arrow keys to make object move
import pygame

pygame.init()

black = (0, 0, 0)          
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Slither')

gameEXIT = False

lead_x = 300
lead_y = 300
# adding new variable:
lead_x_change = 0 # at first the change is zero

#EVENT LOOP:
while not gameEXIT: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEXIT = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                lead_x_change = -10 # then the lead x change is -10 if left arrow is pressed
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10 # and lead x change is +10 if right arrow is pressed

# LOGIC LOOP:
    lead_x += lead_x_change
           
    gameDisplay.fill(white) # Fill
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10]) # Draw
    pygame.display.update() # Update





pygame.quit()
quit()






