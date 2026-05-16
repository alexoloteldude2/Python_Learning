import pygame 
from pygame.sprite import Sprite
from random import randint
class Enemy (Sprite):
    def __init__(self,screen):
        super(Enemy,self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/enemy2.png")
        self.screenRect = self.screen.get_rect() 
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = randint (0+self.rect.width//2,self.screenRect.width-self.rect.width//2)
        self.speed=1
        self.movement = 1
        
    def blit (self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        self.movement +=1
        if self.movement % 2 == 0:
            self.rect.top += self.speed
            if self.rect.bottom<(0-self.screenRect.height):
                self.kill()