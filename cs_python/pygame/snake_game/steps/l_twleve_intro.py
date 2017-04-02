# MAKING A SNAKE GAME
# allowing user to press and hold arrow keys to make object move
import pygame
import time

pygame.init()

black = (0, 0, 0)          
white = (255, 255, 255)
red = (255, 0, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')

gameEXIT = False

lead_x = display_width/2
lead_y = display_height/2

lead_x_change = 0
lead_y_change = 0 

clock = pygame.time.Clock()

block_size = 10

FPS = 30

font = pygame.font.SysFont(None, 25) # making font object

# FUNCTION FOR PUTTING TEXT ON SCREEN:
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2]) # python list

#EVENT LOOP:
while not gameEXIT: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEXIT = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                lead_x_change = -block_size
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
            elif event.key == pygame.K_UP: 
                lead_y_change = -block_size
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0

# BOUNDARIES
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameExit = True




# LOGIC LOOP:
    lead_x += lead_x_change
    lead_y += lead_y_change       
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, block_size, block_size])
    pygame.display.update()

    clock.tick(FPS)



#reference the new message to screen function
message_to_screen("You Lose", red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()






