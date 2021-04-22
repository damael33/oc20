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
        s.deplacer(event)
        
    s.draw(DS, index % s.totalCellCount, playerX, playerY, CENTER_HANDLE)
    playerX += playerX_change
    playerY += playerY_change
    
    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)