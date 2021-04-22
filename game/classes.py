import random
import pygame
from pygame.locals import *


class Attaque:       
    def __init__(self, degat, typa, taux_critique):
        self.degat = degat
        self.typa = typa
        self.taux_critique = taux_critique


    def critique(self):
        nbr_critique = []
        while len(nbr_critique) < self.taux_critique:
            nbr = random.randint(1, 100)
            if nbr not in nbr_critique:
                nbr_critique.append(nbr)

        if random.randint(1, 100) in nbr_critique:
            print('Coup critique!')
            return True
    
    def attaquer(adversaire):
        if affinites[liste_types.index(self.typa)][liste_types.index(adversaire.typp)] == '0':
            print('C\'est inefficace !')
        
        if affinites[liste_types.index(self.typa)][liste_types.index(adversaire.typp)] == 'd':
            print('Ce n\'est pas très efficace...')
            if self.critique():
                adversaire.pv -= self.degat
            else:
                adversaire.pv -= self.degat / 2
            
        if affinites[liste_types.index(self.typa)][liste_types.index(adversaire.typp)] == '2':
            print('C\'est super efficace!')
            if self.critique():
                adversaire.pv -= self.degat *4
            else:
                adversaire.pv -= self.degat * 2
            
        else:
            if self.critique():
                adversaire.pv -= self.degat * 2
            else:
                adversaire.pv -= self.degat
            

class Pokemon:
    def __init__(self, espece, name, pv, typp, xp, attaques):
        self.espece = espece
        self.pv = pv
        self.typp = typp
        self.xp = xp
        self.attaques = attaques


class Joueur:
    def __init__(self, name, filename, cols, rows, equipe=[], mort=[], argent=0, sac={}):
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
        
    def draw(self, surface, cellIndex, x, y, handle = 0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])
    
    def deplacer(self, event):
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
    
class PNJCombat(Joueur):
    def __init__(self, name, equipe, ko, argent, sac):
        Joueur.__init__(self, name, equipe, ko, argent, sac)
    
    
        
class PNJ:
    def __init__(self, name, job):
        self.name = name
        self.job = job



class Combat:
    def __init__(self, joueur, adversaire):
        self.joueur = joueur
        self.adversaire = adversaire
        


class Item:
    def __init__(self, nom, utilite):
        self.nom = nom
        self.utilite = utilite
        
  
  
class Sprite:
    def __init__(self, nom, position):
        self.nom = nom
        self.position = position
