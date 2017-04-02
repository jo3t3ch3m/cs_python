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
lead_x_change = 0

clock = pygame.time.Clock() # will return pygame clock object

#EVENT LOOP:
while not gameEXIT: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEXIT = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                lead_x_change = -10 
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10
# adding event for when the key is stopped being pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_change = 0

        

# LOGIC LOOP:
    lead_x += lead_x_change
           
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])
    pygame.display.update()

    clock.tick(30)





pygame.quit()
quit()






