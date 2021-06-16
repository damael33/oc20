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
# playerX =  W/2 - 32
# playerY = H/1.25
# playerX_change = 0
# playerY_change = 0

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
FPS = 8

#obstacle test
# obstacle1 = pygame.image.load('obstacle1.png').convert_alpha()
# obstacleX = 100
# obstacleY = 700
# obstacle_mask1 = pyame.mask.from_surface(obstacle1)


# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
class Joueur:
    def __init__(self, name, filename, cols, rows):
        self.name = name
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
        
        self.playerX = W/2 - 32
        self.playerY = H/1.25
        self.playerX_change = 0
        self.playerY_change = 0
        self.equipe = []
        self.mort = []
        self.argent = 0
        self.sac = {}
        self.index = 0
        
    def draw(self, surface, cellIndex, x, y, handle = 0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])
    
    def deplacer(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.playerX_change = -10
            if event.key == pygame.K_RIGHT:
                self.playerX_change = +10
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.playerX_change = 0
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.index = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.index = 8

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.playerY_change = -10
       
            if event.key == pygame.K_DOWN:
                self.playerY_change = +10
               
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.playerY_change = 0
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.index = 12
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.index = 0
                

################################################################################################################################################
#carré blanc qui suit joueur
s = Joueur('Matt', 'spritesheet.png', 4, 4)

carré_white = pygame.image.load('test_obstacle.jpg').convert_alpha()
carré_white_mask = pygame.mask.from_surface(carré_white)
carré_whiteX = s.playerX
carré_whiteY = s.playerY
#####
class obstacle:
    def __init__(self, filename, posX, posY):
        self.filename =filename
        self.image_load = pygame.image.load(self.filename).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image_load)
        self.x = posX
        self.y = posY
#         self.offset = (int((s.playerX-19) - self.x), int((s.playerY- 20) - self.y))
#         self.result = self.mask.overlap(carré_white_mask, self.offset)
        
    def collision(self, x, y):
        offset = (int((x-19) - self.x), int((y- 20) - self.y))
        result = self.mask.overlap(carré_white_mask, offset)
        if result:
            print('carré fraté')
            if s.playerX_change > 0:
                s.playerX_change = 0
                s.playerX -= 10
            if s.playerX_change < 0:
                s.playerX_change = 0
                s.playerX += 10
            if s.playerY_change > 0:
                s.playerY_change = 0
                s.playerY -= 10
            if s.playerY_change < 0:
                s.playerY_change = 0
                s.playerY += 10
        else:
            print('nope')
        
    def draw(self, surface):
        surface.blit(self.image_load, (self.x, self.y))     

########################################################################################################################
obstacleTest = obstacle('obstacle1.png', 100, 700)
obstacleTest1 = obstacle('obstacle1.png', 500, 700)
obstacleTest2 = obstacle('obstacle1.png', 100, 200)



CENTER_HANDLE = 4

index = 0
i = 0
# main loop
while True:
    #DS.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        s.deplacer(event)



    DS.blit(carré_white, (s.playerX - 19, s.playerY- 20))
    DS.blit(background, (0, 0))
    ####
    obstacleTest.draw(DS)
    obstacleTest1.draw(DS)
    obstacleTest2.draw(DS)
    ####
    #DS.blit(obstacle1, (obstacleX, obstacleY))
    s.draw(DS, index % s.totalCellCount, s.playerX, s.playerY, CENTER_HANDLE)
#     print(obstacleTest.offset, obstacleTest.x, obstacleTest.y, s.playerX, s.playerY)
    s.playerX += s.playerX_change
    s.playerY += s.playerY_change
    obstacleTest.collision(s.playerX, s.playerY)
    obstacleTest1.collision(s.playerX, s.playerY)
    obstacleTest2.collision(s.playerX, s.playerY)
    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
