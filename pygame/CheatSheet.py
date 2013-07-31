#Running Python/Pygame Cheat Sheet:

#Notes:
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
	screen.fill(blue)
	
#Text on screen                                                                                        
    font = pygame.font.Font(None, 25)

#True makes text ANTI-ALIASED: Anti-alias would be a cool name for a game/novel.                       
    text = font.render("My text", True, black)
    screen.blit(text, [100, 100] )

#Drawing a line - pygame(library), draw(module), line(function)
	pygame.draw.line(screen, red, [0,0], [100, 100], 3)
	
#Drawing more than one line                                                                                     
    for	x in range(0,100,20):
        pygame.draw.line(screen, red, [x, 0], [x, 100], 5)

#Recatangle drawing                                                                                 
	pygame.draw.rect(screen, black,[50, 50, 250, 100], 2)
	pygame.draw.rect(screen, black, [300, 300, 250, 100])

#Drawing an ellipse                                                                                 
        pygame.draw.ellipse(screen, black,[50, 50, 250, 100], 2)

#Drawing arcs                                                                                       
	pygame.draw.arc(screen, green, [100,100,250,200], pi/2, pi, 2)
	pygame.draw.arc(screen, red, [100,100,250,200], 0, pi/2, 2)
	pygame.draw.arc(screen, black, [100,100,250,200], 3*pi/2, 2*pi, 2)
	pygame.draw.arc(screen, white, [100,100,250,200], pi, 3*pi/2, 2)
	
#Drawing polygons                                                                                   
	pygame.draw.polygon(screen, green, [[100,100], [0,200],	[200,200]], 5)

#Discussion about putting text on screen: stamp - what font, how big, what you want it to say

#Output desired display	
	pygame.display.flip()
	
	clock.tick(20)
	
pygame.quit()
