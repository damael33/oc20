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
      
    DS.blit(joueur.carré_white, (500 - 19, 500 - 20))
    DS.blit(background, (joueur.playerX, joueur.playerY))
    joueur.draw(DS, joueur.index % joueur.totalCellCount, 500, 500, CENTER_HANDLE)
    joueur.playerX += joueur.playerX_change
    joueur.playerY += joueur.playerY_change  
    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)