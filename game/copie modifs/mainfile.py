import math, random, sys
import pygame

from classes import *
from variables import *

running = True
# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        joueur.deplacer(event)
    
    joueur.marcher()
    

    DS.blit(pygame.image.load('img/map finale(buissons).png'), (joueur.playerX, joueur.playerY))
    DS.blit(pygame.image.load('img/map finale(map obstacles).png'), (joueur.playerX, joueur.playerY))
    DS.blit(pygame.image.load('img/map finale(map portes).png'), (joueur.playerX, joueur.playerY))
    DS.blit(joueur.carré_white, (500 - 19, 500 - 20))
    DS.blit(pygame.image.load('img/map finale.png'), (joueur.playerX, joueur.playerY))
    joueur.draw(DS, joueur.index % joueur.totalCellCount, 500, 500, CENTER_HANDLE)
    joueur.playerX += joueur.playerX_change
    joueur.playerY += joueur.playerY_change  
    pygame.display.update()
    test = Combat(joueur, advers)
    test.combat()
    CLOCK.tick(FPS)
    DS.fill(BLACK)