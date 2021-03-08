import pygame
from pygame.locals import *
import math, sys, os
pygame.init()

#variables couleurs
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
ScreenBackground = BLACK


#key dict pour savoir quelle forme faire
key_dict1 = {K_p:'rectangle', K_l:'ellipse', K_m:'polygone', K_n:'image', K_d:'deplace'}
forme = 'rectangle'

#crée l'écran
screen = pygame.display.set_mode([800, 600])

#Titre et icone
pygame.display.set_caption("Editeur")
icon = pygame.image.load('Icone.png')
pygame.display.set_icon(icon)

#rect
start = (0, 0)
size = (0, 0)
drawing = False
rect_list = []
RECT_COLOR = RED
key_dict_RECT_COLOR = {K_r:'RED', K_g:'GREEN', K_b:'BLUE', K_w:'WHITE'}
key_dict_RECT_WIDTH = {K_0:0, K_1:1, K_2:2, K_3:3, K_4:4, K_5:5, K_6:6, K_7:7, K_8:8, K_9:9}
RECT_WIDTH = 1

class Rectangle:
    def __init__(self, rect, color=RECT_COLOR, width=RECT_WIDTH):
        self.rect = rect
        self.color = color
        self.width = width
        
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, self.width)
        
#     def moving():
#         self.rect.move_ip(event.rel)
#         
#     def si_dessus():
#         self.rect.collidepoint(event.pos)

#polygone
points = []
key_dict_POLYGON_COLOR = {K_r:'RED', K_g:'GREEN', K_b:'BLUE', K_w:'WHITE'}
key_dict_POLYGON_WIDTH = {K_0:0, K_1:1, K_2:2, K_3:3, K_4:4, K_5:5, K_6:6, K_7:7, K_8:8, K_9:9}
POLYGON_COLOR = RED
POLYGON_WIDTH = 2

#image
img_list = []

moving = False
#boucle editeur
running = True
while running:
    
    screen.fill(ScreenBackground)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key in key_dict1:
                forme = key_dict1[event.key]

######################################################################################################

        if forme == 'rectangle':
            if event.type == MOUSEBUTTONDOWN:
                start = event.pos
                size = 0, 0
                drawing = True
                
            elif event.type == MOUSEBUTTONUP:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                rect = Rectangle(Rect(start, size), RECT_COLOR, RECT_WIDTH)
                rect_list.append(rect)
                drawing = False
                
            elif event.type == MOUSEMOTION and drawing:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                
            if event.type == KEYDOWN:
                if event.key in key_dict_RECT_WIDTH:
                    rect_list[-1].width = key_dict_RECT_WIDTH[event.key]
                
            if event.type == KEYDOWN:
                if event.key in key_dict_RECT_COLOR:
                    rect_list[-1].color = key_dict_RECT_COLOR[event.key]
                     
                     
                     
        
                
     #####################################################################################################
     
        if forme == 'ellipse':
            if event.type == KEYDOWN:
                if event.key == K_1:
                    print('hello')
    ######################################################################################################

        if forme == 'polygone':
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if len(points) > 0:
                        points.pop()

            elif event.type == MOUSEBUTTONDOWN:
                points.append(event.pos)
                drawing = True

            elif event.type == MOUSEBUTTONUP:
                drawing = False

            elif event.type == MOUSEMOTION and drawing:
                points[-1] = event.pos

            if event.type == KEYDOWN:
                if event.key in key_dict_POLYGON_WIDTH:
                    RECT_WIDTH = key_dict_POLYGON_WIDTH[event.key]
            
            if event.type == KEYDOWN:
                if event.key in key_dict_POLYGON_COLOR:
                    POLYGON_COLOR = key_dict_POLYGON_COLOR[event.key]



    #####################################################################################################
        if forme == 'image':
            module = sys.modules['__main__']
            path, name = os.path.split(module.__file__)
            path = os.path.join(path, 'bird.png')
            img = pygame.image.load('bird.png')
            img.convert()
            rect_img = img.get_rect()
            center = 800//2, 600//2
            rect_img.center = center
            angle = 0
            scale = 1
            img_list.append(img)
            
            if event.type == KEYDOWN:
                if event.key == K_r:
                    if event.mod & KMOD_SHIFT:
                        angle -= 10
                    else:
                        angle += 10
                    img_list[-1] = pygame.transform.rotozoom(img_list[-1], angle, scale)

                elif event.key == K_s:
                    if event.mod & KMOD_SHIFT:
                        scale /= 1.1
                    else:
                        scale *= 1.1
                    img_list[-1] = pygame.transform.rotozoom(img_list[-1], angle, scale)
                
                elif event.key == K_h:
                    img_list[-1] = pygame.transform.flip(img_list[-1], True, False)
                    
                elif event.key == K_v:
                    img_list[-1] = pygame.transform.flip(img_list[-1], False, True)
    
###########################################################################################################
        
        if forme == 'deplace':
            
            if event.type == MOUSEBUTTONDOWN:
                if rect_img.collidepoint(event.pos):
                    moving = True

            elif event.type == MOUSEBUTTONUP:
                moving = False

            elif event.type == MOUSEMOTION and moving:
                rect_img.move_ip(event.rel)
    
        
    for img in img_list:
        screen.blit(img, rect_img)
        pygame.draw.rect(screen, RED, rect_img, 1)
    
    for rect in rect_list:
        rect.draw()
        
    
    if len(points)>1:
        rect = pygame.draw.lines(screen, POLYGON_COLOR, True, points, POLYGON_WIDTH)
        pygame.draw.rect(screen, GREEN, rect, POLYGON_WIDTH)
        pygame.display.update()

    pygame.display.update()
    
pygame.quit()