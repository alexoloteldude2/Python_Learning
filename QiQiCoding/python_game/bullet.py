import pygame 
from pygame.sprite import Sprite
class Bullet (Sprite):
    def __init__(self,screen,plane):
        super(Bullet,self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/bullet1.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = plane.rect.top
        self.rect.centerx = plane.rect.centerx
        self.speed=2
        self.movement = 1
        
    def blit (self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        self.rect.top -= self.speed
        if self.movement % 3 == 0:
            self.rect.top += self.speed
        if self.rect.bottom<0:
            self.kill()



        