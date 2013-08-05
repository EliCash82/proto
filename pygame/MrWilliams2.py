#Anderson Evans
#August 3rd - 2013

#much of code taken from tutorial http://www.youtube.com/watch?v=mTmJfWdZzbo

import pygame
import sys, glob
from pygame import *


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('19man2.png')
        self.rect = pygame.rect.Rect((320, 240), self.image.get_size())
        
        self.resting = False
        self.dy = 0

    def update(self, dt, game):

        last = self.rect.copy()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
           # self.rect.x -= 10
            self.rect.x -= 300 * dt
        if key[pygame.K_RIGHT]:
           # self.rect.x += 10
            self.rect.x += 300 * dt
       # if key[pygame.K_UP]:
           # self.rect.y -= 10
           # self.rect.y -= 300 * dt
       # if key[pygame.K_DOWN]:
           # self.rect.y += 10
           # self.rect.y += 300 * dt

        if self.resting and key[pygame.K_SPACE]:
            self.dy = -500
        self.dy = min(400, self.dy + 40)

        self.rect.y += self.dy * dt

        new = self.rect

        self.resting = False

        for cell in pygame.sprite.spritecollide(self, game.walls, False):

            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if last.bottom <= cell.top and new.bottom > cell.top:
                self.resting = True
                new.bottom = cell.top
                self.dy = 0
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
                self.dy = 0

class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()

        pygame.display.set_caption("Hit SPACEBAR to bounce.")
        
        #image = pygame.image.load('meWalk/walk1.png')
        background = pygame.image.load('MrWilliamsbg2.png')
        sprites = pygame.sprite.Group()
        #sprites.add(background)#newish - error prone
        self.player = Player(sprites)
        
        self.walls = pygame.sprite.Group()
        block = pygame.image.load('block.png')
        for x in range(0, 640, 32):
            for y in range(0, 480, 32):
                if x in (0, 640-32) or y in (0, 480-32):
                    wall = pygame.sprite.Sprite(self.walls)
                    wall.image = block
                    wall.rect = pygame.rect.Rect((x, y), block.get_size())
        sprites.add(self.walls)
        
        
        while 1:
            #clock.tick(40)
            dt = clock.tick(30)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            #sprites.update()
            #sprites.update(dt / 1000.)
            sprites.update(dt / 1000., self)
            #screen.fill((200, 200, 200))
            screen.blit(background, (0, 0))# - unsure, could be overstepping
            sprites.draw(screen)
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    Game().main(screen)

