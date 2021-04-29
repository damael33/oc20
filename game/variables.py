import pygame
from pygame.locals import *
from classes import *
#background
background = pygame.image.load('background.jpg')

#Titre et icone
pygame.display.set_caption("pokemon")
icon = pygame.image.load('pokeball.png')
pygame.display.set_icon(icon)



# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
FPS = 8

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

s = Joueur("Bebel", "spritesheet.png", 4, 4)
CENTER_HANDLE = 4
i = 0
#Affinité de types et liste des types
affinites = ['            d0  d',
             ' dd2 2     2d d 2',
             ' 2dd    2   2 d  ',
             ' d2d   d2d d2 d d',
             '  2dd   02    d  ',
             ' dd 2 d  22   2 d',
             '2    2 d ddd20 22',
             '   2   dd   dd  0',
             ' 2 d2  2 0 d2   2',
             '   2d 2    2d   d',
             '      22  d    0d',
             ' d 2  dd d2  d 2d',
             ' 2   2d d2 2    d',
             '0         2  2 dd',
             '              2 d',
             '      d   2  2 dd',
             ' dd  2      2   d']

liste_types = ['Normal', 'Feu', 'Eau', 'Plante', 'Electrik',
               'Glace', 'Combat', 'Poison', 'Sol', 'Vol',
               'Psy', 'Insecte', 'Roche', 'Spectre', 'Dragon',
               'Ténèbres', 'Acier']