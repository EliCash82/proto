#ROOM 1: The library

#This is my skeletal structure for the first room in the game. There is an overhead camera view of the room with a single desk on the right side of the screen.  I will layer images over it and add a protagonist in due time.

#I have to run a specific python to get pygame module to work
#so when running programs instead of just typing "python" before the executable, type "python2.7-32" then executable

#Setting up
import pygame

pygame.init()

#Defining Colors, first column is RED second is GREEN third is BLUE

black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red   = ( 255,   0,   0)
blue  = (   0,   0, 255)

#When setting screen size first variable is width, second variable is height
size=[700, 500]
screen=pygame.display.set_mode(size)

#Set Caption at top of screen
pygame.display.set_caption("TITLE OF GAME")

#define pi for arcs - you have to use pi to get the correct math, so if you are using arcs, this is the place to define pi.                                                                                  
pi=3.141592643

#Set loop for program that runs until user closes
done=False

#Screen update time
clock=pygame.time.Clock()

#Current Main Loop
while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

#Screen Fill
    screen.fill(white)
        
#Drawing polygons                                                                                   
    pygame.draw.polygon(screen, blue, [[0,0], [100,100],[700,0], [600,100]], 5)
    pygame.draw.polygon(screen, red, [[0,0], [100,100],[600,100], [700,0]], 5)
    pygame.draw.polygon(screen, blue, [[0,500], [100,400],[700,500], [600,400]], 5)    
    pygame.draw.polygon(screen, red, [[0,500], [100,400],[600,400], [700,500]], 5)
    pygame.draw.polygon(screen, blue, [[0,500], [100, 400], [0,0], [100, 100]], 5)
    pygame.draw.polygon(screen, red, [[0,500], [100,400], [100,100], [0,0]], 5)
    pygame.draw.polygon(screen, blue, [[700,0], [600,100], [700,500], [600,400]], 5)
    pygame.draw.polygon(screen, red, [[700,0], [600,100], [600,400], [700,500]], 5)

    pygame.draw.polygon(screen, red, [[500,200], [400,200], [400,350], [500,350]], 5)
#Output desired display
    pygame.display.flip()
        
    clock.tick(20)
        
pygame.quit()
