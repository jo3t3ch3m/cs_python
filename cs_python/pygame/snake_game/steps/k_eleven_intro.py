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
lead_y_change = 0 

clock = pygame.time.Clock()

#EVENT LOOP:
while not gameEXIT: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEXIT = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                lead_x_change = -10
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0
            elif event.key == pygame.K_UP: 
                lead_y_change = -10
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0

# BOUNDARIES
        if lead_x >= 800 or lead_x < 0 or lead_y >= 600 or lead_y < 0:
            gameExit = True


        


        

# LOGIC LOOP:
    lead_x += lead_x_change
    lead_y += lead_y_change
           
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])
    pygame.display.update()

    clock.tick(30)





pygame.quit()
quit()






