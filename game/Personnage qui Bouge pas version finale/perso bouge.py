import math, random, sys
import pygame
from pygame.locals import *


# define display surface            
W, H = 1920, 1080
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
pygame.display.set_caption("spritesheet.png")
FPS = 2

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

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10
                index = 4
            if event.key == pygame.K_RIGHT:
                playerX_change = +10
                index = 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                
    s.draw(DS, index % s.totalCellCount, playerX, playerY, CENTER_HANDLE)
    index += 1
    
    #pygame.draw.circle(DS, WHITE, (int(HW), int(HH)), 2, 0)
    playerX += playerX_change
    playerY += playerY_change
    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
