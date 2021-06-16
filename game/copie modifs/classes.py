import random
import pygame
from pygame.locals import *

W, H = 1000, 1000
HW, HH = W / 2, H / 2
AREA = W * H
class Attaque:       
    def __init__(self, name, degat, typa, taux_critique, image_path):
        self.name = name
        self.degat = degat
        self.typa = typa
        self.taux_critique = taux_critique
        self.image = pygame.image.load(image_path).convert_alpha()
        self.mask_image = pygame.mask.from_surface(self.image)
        
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
    def __init__(self, espece, name, pvmax, typp, xp, attaques):
        self.espece = espece
        self.pvmax = pvmax
        self.pv = pvmax
        self.typp = typp
        self.xp = xp
        self.attaques = attaques

    def capturer(self):
        taux_echec = int((self.pv / self.pvmax) * 100)
        nbr_echec = []
        while len(nbr_echec) < self.taux_echec:
            nbr = random.randint(1, 100)
            if nbr not in nbr_echec:
                nbr_echec.append(nbr)

        if random.randint(1, 100) not in nbr_echec:
            print('Capturé!')
            return True
        
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
        self.i = 0
        
        self.playerX = W/2 - 32
        self.playerY = H/1.25
        self.playerX_change = 0
        self.playerY_change = 0
        self.equipe = []
        self.mort = []
        self.argent = 0
        self.sac = {}
        self.index = 0
        
        self.carré_white = pygame.image.load('test_obstacle.jpg').convert_alpha()
        self.carré_white_mask = pygame.mask.from_surface(self.carré_white)
        self.carré_whiteX = self.playerX
        self.carré_whiteY = self.playerY
   
       
    def draw(self, surface, cellIndex, x, y, handle = 0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])
    
    def deplacer(self, event, mask):
        if event.type == pygame.KEYDOWN and not collision(mask):
            if event.key == pygame.K_RIGHT:
                self.playerX_change = -10
            if event.key == pygame.K_LEFT:
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
            if event.key == pygame.K_DOWN:
                self.playerY_change = -10
       
            if event.key == pygame.K_UP:
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

    def marcher(self):
        if pygame.key.get_pressed() [pygame.K_LEFT] == True:
            self.i += 1
            self.index = 4 + self.i % 4
        
        if pygame.key.get_pressed() [pygame.K_RIGHT] == True:
            self.i += 1
            self.index = 8 + self.i % 4

        if pygame.key.get_pressed() [pygame.K_DOWN] == True:
            self.i += 1
            self.index = 0 + self.i % 4
        
        if pygame.key.get_pressed() [pygame.K_UP] == True:
            self.i += 1
            self.index = 12 + self.i % 4
        
    
    def collision(self, ):
        
        
class PNJCombat(Joueur):
    def __init__(self, name, equipe, ko, argent, sac):
        Joueur.__init__(self, name, equipe, ko, argent, sac)
    
#     def lance_combat(self):
#         if joueur dans ma zone:
#             return True
    
        
class PNJ:
    def __init__(self, name, job):
        self.name = name
        self.job = job



class Combat:
    def __init__(self, joueur, adversaire):
        self.joueur = joueur
        self.adversaire = adversaire
        self.etat = False
        self.pokemon_joueur = self.joueur.equipe[0]
        if isinstance(self.adversaire, PNJCombat):
            self.pokemon_adverse = self.adversaire.equipe[0]
        else:
            self.pokemon_adverse = self.adversaire
    def combat(self):       
        if adversaire.lance_combat():
            self.etat = True
        combat_template = pygame.image.load('img/Combat_template.png')
        
        combat_attaque = pygame.image.load('img/Combat_mask(attaque).png')
        combat_attaque_mask = pygame.mask.from_surface(combat_attaque)

        combat_bag = pygame.image.load('img/Combat_mask(bag).png')
        combat_bag_mask = pygame.mask.from_surface(combat_bag)
        
        combat_pokemon = pygame.image.load('img/Combat_mask(pokemon).png')
        combat_pokemon_mask = pygame.mask.from_surface(combat_pokemon)
        
        combat_run = pygame.image.load('img/Combat_mask(pokemon).png')
        combat_run_mask = pygame.mask.from_surface(combat_run)

        DS.blit(combat_attaque, (0, 0))
        DS.blit(combat_bag, (0, 0))
        DS.blit(combat_pokemon, (0, 0))
        DS.blit(combat_run, (0, 0))
        DS.blit(combat_template, (0, 0))
        
        mx, my = pygame.mouse.get_pos()
        combat_souris = pygame.image.load('img/souris.png')
        combat_souris_mask = pygame.mask.from_surface(combat_souris)
        DS.blit(combat_souris,(mx, my))
        
        offset1 = (int(mx - 0), int(my - 0))
        result1 = combat_attaque_mask.overlap(combat_souris_mask, offset1)
        
        offset2 = (int(mx - 0), int(my - 0))
        result2 = combat_bag_mask.overlap(combat_souris_mask, offset2)
        
        offset3 = (int(mx - 0), int(my - 0))
        result3 = combat_pokemon_mask.overlap(combat_souris_mask, offset3)
        
        offset4 = (int(mx - 0), int(my - 0))
        result4 = combat_run_mask.overlap(combat_souris_mask, offset4)
        
        if result1 = True, and jhyxcjkh:
            action = 'attaquer'
            
        if result2 = True, and jhyxcjkh:
            action = 'utiliser objet'
            
        if result3 = True, and jhyxcjkh:
            action = 'changer'
            
        if result4 = True, and jhyxcjkh:
            action = 'run'
        
        #blit le nouveau background
        while self.etat:
            action = 'attaquer'
            #en fonction d'ou on appuie, l'action change
            if action == 'attaquer':
                #blit image des attaques
                for attaque in self.pokemon_joueur.attaques:
                    attaque.img_attaque #à tel position
                
                #attaque choisie = en fonction de sur quelle attaque on clique
                self.pokemon_joueur.attaques[attaque choisie].attaquer(self.pokemon_adverse)
                
            if action = 'utiliser objet':
                #objet en fonction de sur lequel on clique
                objet = Item('pokeball', 'capture')
                
                if objet.utilite == 'capture' and isinstance(self.adversaire, Pokemon):
                    if objet.utilisation(self.pokemon_adverse):
                        self.joueur.equipe.append(self.pokemon_adverse)
                        self.pokemon_adverse.pv = 0
                        
                if objet.utilite == 'soin':
                    self.pokemon_joueur.pv = self.pokemon_joueur.pvmax
            
            if action == 'changer':
                #blit choix pokemon
                #nombre choisi = pokemon sur lequel on clique
                self.changement(nombre choisis)
            
            if isinstance(self.adversaire, PNJCombat) and len(adversaire.equipe) = 0:
                vainqueur = self.joueur
                self.etat = False
            
            elif isinstance(self.adversaire, Pokemon) and self.pokemon_adverse.pv <= 0:
                vainqueur = self.joueur
                self.etat = False
            
            self.pokemon_adverse.attaques[random.randint(0, 3)].attaquer(self.pokemon_joueur)
            if self.pokemon_joueur.pv <= 0 and len(self.joueur.equipe) > 0:
                self.joueur.ko.append(self.pokemon_joueur)
                self.joueur.equipe.remove(self.pokemon_joueur)
                self.changement(numero choisis)
                
            elif len(self.joueur.equipe) = 0:
                self.etat = False
                vainqueur = self.adversaire
            
        if vainqueur == self.joueur:
            for pokemon in self.joueur.equipe:
                pokemon.xp += 10
            if isinstance(self.adversaire, PNJCombat):
                self.joueur.argent += self.adversaire.argent
        else:
            self.joueur.argent *= (19/20)

    def changement(self, nbr):
        self.pokemon_joueur = joueur.equipe[nbr]
        
class Item:
    def __init__(self, nom, utilite):
        self.nom = nom
        self.utilite = utilite
        
#     def utilisation(self, beneficiaire):
#         if self.utilite == 'soin':
#             beneficiaire.pv = beneficiaire.pvmax
#             
#         if self.utilite = 'capture':
#             beneficiaire.capturer()
            
            
  
  
class Sprite:
    def __init__(self, nom, position):
        self.nom = nom
        self.position = position
