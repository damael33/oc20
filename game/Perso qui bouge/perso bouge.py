import math, random, sys
import pygame
from pygame.locals import *

#background
background = pygame.image.load('background.jpg')

#Titre et icone
pygame.display.set_caption("pokemon")
icon = pygame.image.load('pokeball.png')
pygame.display.set_icon(icon)

# define display surface            
W, H = 1000, 1000
HW, HH = W / 2, H / 2
AREA = W * H

#perso
playerX =  W/2 - 32
playerY = H/1.25
playerX_change = 0
playerY_change = 0

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
FPS = 8

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

class spritesheet:
    def __init__(self, filename, cols, rows):
        self.sheet = pygame.image.load(filename).convert_alpha()
        
        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols * rows
        
        self.rect = self.sheet.get_rect()
        w = self.cellWidth = int(self.rect.width / cols)
        h = self.cellHeight = int(self.rect.height / rows)
        hw, hh = self.cellCenter = (int(w / 2), int(h / 2))
        
        self.cells = list([(index % cols * w, int(index / cols) * h, w, h) for index in range(self.totalCellCount)])
        self.handle = list([
            (0, 0), (-hw, 0), (-w, 0),
            (0, -hh), (-hw, -hh), (-w, -hh),
            (0, -h), (-hw, -h), (-w, -h),])
        
    def draw(self, surface, cellIndex, x, y, handle = 0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])

s = spritesheet("spritesheet.png", 4, 4)

CENTER_HANDLE = 4

index = 0
i = 0

running = True
# main loop
while running:
    DS.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#droite-gauche ------------------------------------------------------------------------------------------------
        print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10
       
            if event.key == pygame.K_RIGHT:
                playerX_change = +10
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                index = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                index = 8
#haut-bas-----------------------------------------------------------------------------------------------------------------           
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -10
       
            if event.key == pygame.K_DOWN:
                playerY_change = +10
               
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                index = 12
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                index = 0   
     
     
    s.draw(DS, index % s.totalCellCount, playerX, playerY, CENTER_HANDLE)
    playerX += playerX_change
    playerY += playerY_change
    
    if pygame.key.get_pressed() [pygame.K_LEFT] == True:
        i += 1
        index = 4 + i % 4
        
    if pygame.key.get_pressed() [pygame.K_RIGHT] == True:
        i += 1
        index = 8 + i % 4

    if pygame.key.get_pressed() [pygame.K_DOWN] == True:
        i += 1
        index = 0 + i % 4
        
    if pygame.key.get_pressed() [pygame.K_UP] == True:
        i += 1
        index = 12 + i % 4
        
    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
