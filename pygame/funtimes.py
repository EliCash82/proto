#import pygame library
import pygame

#Initialize pygame engine
pygame.init()

#Define colors
black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red   = ( 255,   0,   0)
blue  = (   0,   0, 255)

#set screen size 700 is width and 500 is height

size=[700, 500]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("Library")

#define pi for arcs
pi=3.141592643

#loop until user closes
done=False

#manage screen update time
clock=pygame.time.Clock()

#Main Program Loop!!!!!!!!!!!!!

while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

#screen fill
    screen.fill(white)

#Drawing a line
    for x in range(0,100,20):
        pygame.draw.line(screen, red, [x, 0], [x, 100], 5)

#Drawing a line - pygame(library), draw(module), line(function)
        pygame.draw.line(screen, green, [0,0], [100, 100], 3)

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
        pygame.draw.polygon(screen, green, [[100,100],[0,200],[200,200],[100, 150]], 5)

    pygame.display.flip()

    clock.tick(20)

pygame.quit ()
