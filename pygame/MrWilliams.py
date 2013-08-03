#Anderson Evans
#August 3rd - 2013

import pygame
import sys, glob
from pygame import *

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('19man.png')
        self.rect = pygame.rect.Rect((320, 240), self.image.get_size())

    def update(self, dt):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
           # self.rect.x -= 10
            self.rect.x -= 300 * dt
        if key[pygame.K_RIGHT]:
           # self.rect.x += 10
            self.rect.x += 300 * dt
        if key[pygame.K_UP]:
           # self.rect.y -= 10
            self.rect.y -= 300 * dt
        if key[pygame.K_DOWN]:
           # self.rect.y += 10
            self.rect.y += 300 * dt

class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()
        pygame.display.set_caption("19th Century Graphics")
        image = pygame.image.load('19Man.png')
        sprites = pygame.sprite.Group()
        self.player = Player(sprites)

        
        
        while 1:
            #clock.tick(40)
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            #sprites.update()
            sprites.update(dt / 1000.)
            screen.fill((200, 200, 200))
            #screen.blit(image, (320, 240))
            sprites.draw(screen)
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 490))
    Game().main(screen)

