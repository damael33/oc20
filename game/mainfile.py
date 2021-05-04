import math, random, sys
import pygame

from classes import *
from variables import *

running = True
# main loop
while running:
    DS.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        joueur.deplacer(event)

    joueur.draw(DS, joueur.index % joueur.totalCellCount, joueur.playerX, joueur.playerY, CENTER_HANDLE)
    joueur.playerX += joueur.playerX_change
    joueur.playerY += joueur.playerY_change
    
    if pygame.key.get_pressed() [pygame.K_LEFT] == True:
        i += 1
        joueur.index = 4 + i % 4
        
    if pygame.key.get_pressed() [pygame.K_RIGHT] == True:
        i += 1
        joueur.index = 8 + i % 4

    if pygame.key.get_pressed() [pygame.K_DOWN] == True:
        i += 1
        joueur.index = 0 + i % 4
        
    if pygame.key.get_pressed() [pygame.K_UP] == True:
        i += 1
        joueur.index = 12 + i % 4
    
    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)