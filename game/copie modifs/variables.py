import pygame
from pygame.locals import *
from classes import *
#background


#Titre et icone
pygame.display.set_caption("pokemon")
icon = pygame.image.load('pokeball.png')
pygame.display.set_icon(icon)



# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
FPS = 80

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

joueur = Joueur("Bebel", "spritesheet.png", 4, 4)
joueur.equipe = [Pokemon('salameche', 'Feu', 0, [Attaque('boule feu', 5, 'Feu', 20, 'Combat pokemon/potion.png')], 'Combat pokemon/sprites pokemon/salamèche/salamèche_allié.png', 'Combat pokemon/changement pokemon/changement_pokemon_salameche.png')]

advers = Pokemon('bublizare', 'Plante', 0, [Attaque('jet', 5, 'Eau', 30, 'Combat pokemon/potion.png')], 'Combat pokemon/sprites pokemon/bulbizare/bulbisare_ennemi.png', 'Combat pokemon/changement pokemon/changement_pokemon_bulbizare.png')



CENTER_HANDLE = 4
#Affinité de types et liste des types
