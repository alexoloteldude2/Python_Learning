import pygame 
class Plane:
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("images/me1.png")
        self.rect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom
        self.speed=1
        self.moveUp = False
        self.moveLeft = False
        self.moveRight = False
        self.moveDown = False
        

    def blit (self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        if self.moveLeft and self.rect.left>0:
            self.rect.centerx -= self.speed
        if self.moveRight and self.rect.right<self.screenRect.right:
            self.rect.centerx += self.speed 
        if self.moveUp  and self.rect.top>0:
            self.rect.bottom -= self.speed
        if self.moveDown and self.rect.bottom<self.screenRect.bottom:
            self.rect.bottom += self.speed