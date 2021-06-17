import math, random, sys
import pygame

from classesCopie1 import *
from variablesCopie1 import *
pygame.mixer.init()
pygame.mixer.music.load('sound/map_music.wav')
pygame.mixer.music.play(-1)
running = True
# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
                
        joueur.deplacer(event)
    
    joueur.marcher()
    
    DS.blit(pygame.image.load('pokemap/map_finale(buissons).png'), (joueur.playerX - 1090, joueur.playerY - 1460))
    DS.blit(pygame.image.load('pokemap/map_finale(obstacles).png'), (joueur.playerX - 1090, joueur.playerY - 1460))
    advers.posX = random.randint(-300, 100)
    advers.posY = random.randint(800, 900)
    DS.blit(advers.place, (joueur.playerX - advers.posX, joueur.playerY - advers.posY))
    DS.blit(joueur.carré_white, (500 - 19, 500 - 20))
    DS.blit(pygame.image.load('pokemap/map_finale.png'), (joueur.playerX - 1090, joueur.playerY - 1460))
    DS.blit(pygame.image.load(pnj.filename), (joueur.playerX - pnj.posX, joueur.playerY - pnj.posY))
    joueur.draw(DS, joueur.index % joueur.totalCellCount, 500, 500, CENTER_HANDLE)
    
    joueur.playerX += joueur.playerX_change
    joueur.playerY += joueur.playerY_change
    
    obstacle = Obstacle('pokemap/map_finale(obstacles).png', joueur.playerX - 1090, joueur.playerY - 1460)
    obstacle.collision(joueur)
    
    pnj.lance_combat(joueur)
    advers.lance_combat(joueur)
    
    #test = Combat(joueur, advers)
    #test.combat()
    
    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)