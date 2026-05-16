import pygame 
from sys import exit
def eventHandler(planeSurface):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                planeSurface.moveRight = True
            elif event.key == pygame.K_UP:
                planeSurface.moveUp = True
            elif event.key == pygame.K_DOWN:
                planeSurface.moveDown = True
            elif event.key == pygame.K_LEFT:
                planeSurface.moveLeft = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                planeSurface.moveRight = False
            elif event.key == pygame.K_UP:
                planeSurface.moveUp = False
            elif event.key == pygame.K_DOWN:
                planeSurface.moveDown = False
            elif event.key == pygame.K_LEFT:
                planeSurface.moveLeft = False
