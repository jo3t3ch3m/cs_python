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

# THE HEAD OF THE SNAKE:
lead_x = 300
lead_y = 300




while not gameEXIT: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEXIT = True
# specify new events here:
# KEYSTROKES
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # "if left arrow key is pressed"
                lead_x -= 10 # subtracting x (going left)
            if event.key == pygame.K_RIGHT:
                lead_x += 10 # adding to x
                
    gameDisplay.fill(white)
#   pygame.draw.rect(gameDisplay, black, [400, 300, 10, 10])
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])
    
    pygame.display.update() 





pygame.quit()
quit()






