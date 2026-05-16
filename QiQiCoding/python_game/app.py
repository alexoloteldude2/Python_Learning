import pygame 
from sys import exit
from plane import *
from event import *
from bullet import *
from pygame.sprite import Group
from enemy import *
def initMainWindow():
    pygame.init()
    screen=pygame.display.set_mode((475,700))
    pygame.display.set_caption("Plane War✈️🔫")
    background=pygame.image.load("images/background.png")
    #planeImg=pygame.image.load("images/me1.png")
    #planeRect=planeImg.get_rect()
    #screenRect=screen.get_rect()
    #planeRect.centerx=screenRect.centerx
    #planeRect.bottom=screenRect.bottom
    planeSurface = Plane(screen)
    #bulletSurface=Bullet(screen,planeSurface)
    bullets=Group()
    enemies=Group()
    rates=0
    enemyRates=0
    score=0
    gameFont=pygame.font.SysFont('arial',26,True)
    while True:
        screen.blit(background,(0,0))
        planeSurface.blit()
        eventHandler(planeSurface)
        planeSurface.update()
        rates+=1
        if rates %90==0:
            newBullet=Bullet(screen,planeSurface)
            bullets.add(newBullet)
        bullets.draw(screen)
        bullets.update()
        enemyRates+=1
        if enemyRates %1000==0:
            newEnemy=Enemy(screen)
            enemies.add(newEnemy)
        enemies.draw(screen)
        enemies.update()
        if pygame.sprite.groupcollide(enemies,bullets,True,True) :
            score+=1
        scoreRender=gameFont.render("score: "+str(score), True, (128,128,128))
        screen.blit(scoreRender,screen.get_rect().topleft)
        if pygame.sprite.spritecollide(planeSurface,enemies,False) :
            screen.blit(background,(0,0))
            gameOverRender=gameFont.render("Game 0ver",True,(128,128,129))
            screen.blit(gameOverRender,[screen.get_rect().width/3,screen.get_rect().centery])
            screen.blit(scoreRender,[screen.get_rect().width/3,screen.get_rect().centery+36])
            break

        pygame.display.update()

    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            
        # bulletSurface.blit()
        # bulletSurface.update()
initMainWindow()


