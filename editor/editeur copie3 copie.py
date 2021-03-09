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
key_dict2 = {(KMOD_LMETA, K_p):'move rectangle', K_l:'ellipse', K_m:'polygone', K_n:'image', K_d:'deplace'}
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

class Shapes:
    def __init__(self, rect_shape, form, color=RECT_COLOR, width=RECT_WIDTH):
        self.rect_shape = rect_shape
        self.color = color
        self.width = width
        self.form = form
        
    def draw(self):
        if self.form == 'rectangle':
            pygame.draw.rect(screen, self.color, self.rect_shape, self.width)
        elif self.form == 'ellipse':
            pygame.draw.ellipse(screen, self.color, self.rect_shape, self.width) 

#polygone
points = []
key_dict_POLYGON_COLOR = {K_r:'RED', K_g:'GREEN', K_b:'BLUE', K_w:'WHITE'}
key_dict_POLYGON_WIDTH = {K_0:0, K_1:1, K_2:2, K_3:3, K_4:4, K_5:5, K_6:6, K_7:7, K_8:8, K_9:9}
POLYGON_COLOR = RED
POLYGON_WIDTH = 2

#image
class Images:
    def __init__(self, nom, center = (800//2, 600//2), angle = 0, scale = 1,
                 rect_img = 'rien', image = 'rien'):
        self.nom = nom
        self.center = center
        self.angle = angle
        self.scale = scale
        self.rect_img = rect_img
        self.image = image
        
    def print_img(self):
        module = sys.modules['__main__']
        path, name = os.path.split(module.__file__)
        path = os.path.join(path, self.nom)
        self.image = pygame.image.load(self.nom)
        self.image.convert()
        self.rect_img = self.image.get_rect()
        self.rect_img.center = self.center
        
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
            #print(event)
            if event.key in key_dict1:
                forme = key_dict1[event.key]
            elif event.key in key_dict1 and event.mod & KMOD_LMETA:
                forme = 'move ' + key_dict1[event.key]

######################################################################################################
        #print(forme)
        if forme == 'rectangle':
            if event.type == MOUSEBUTTONDOWN:
                start = event.pos
                size = 0, 0
                drawing = True
                
            elif event.type == MOUSEBUTTONUP:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                rect = Shapes(Rect(start, size), forme, RECT_COLOR, RECT_WIDTH)
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
            if event.type == MOUSEBUTTONDOWN:
                start = event.pos
                size = 0, 0
                drawing = True
                
            elif event.type == MOUSEBUTTONUP:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                rect = Shapes(Rect(start, size), forme, RECT_COLOR, RECT_WIDTH)
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
            
            img = Images('bird.png')
            img.print_img()
            img_list.append(img)
            
            if event.type == KEYDOWN:
                if event.key == K_r:
                    if event.mod & KMOD_SHIFT:
                        img.angle -= 10
                    else:
                        img.angle += 10
                    img_list[-1].image = pygame.transform.rotozoom(img_list[-1].image, img.angle, img.scale)

                elif event.key == K_s:
                    if event.mod & KMOD_SHIFT:
                        img.scale /= 1.1
                    else:
                        img.scale *= 1.1
                    img_list[-1].image = pygame.transform.rotozoom(img_list[-1].image, img.angle, img.scale)
                
                elif event.key == K_h:
                    img_list[-1] = pygame.transform.flip(img_list[-1], True, False)
                    
                elif event.key == K_v:
                    img_list[-1] = pygame.transform.flip(img_list[-1], False, True)
    
###########################################################################################################
        
        if forme == 'deplace':
            
            if event.type == MOUSEBUTTONDOWN:
                if img.rect_img.collidepoint(event.pos):
                    moving = True

            elif event.type == MOUSEBUTTONUP:
                moving = False

            elif event.type == MOUSEMOTION and moving:
                img.rect_img.move_ip(event.rel)
    
        
    for img in img_list:
        screen.blit(img.image, img.rect_img)
        pygame.draw.rect(screen, RED, img.rect_img, 1)
    
    for rect in rect_list:
        rect.draw()
        
    
    if len(points)>1:
        rect = pygame.draw.lines(screen, POLYGON_COLOR, True, points, POLYGON_WIDTH)
        pygame.draw.rect(screen, GREEN, rect, POLYGON_WIDTH)
        pygame.display.update()

    pygame.display.update()
    
pygame.quit()