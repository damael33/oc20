import random
import pygame
from pygame.locals import *

W, H = 1000, 1000
HW, HH = W / 2, H / 2
AREA = W * H
DS = pygame.display.set_mode((W, H))
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
    
    def attaquer(self, adversaire):
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
    def __init__(self, espece, typp, xp, attaques, place, image, image_changement_path, posX, posY):
        self.espece = espece
        self.typp = typp
        self.xp = xp
        self.pvmax = 20 + int(self.xp / 10)
        self.pv = self.pvmax
        self.attaques = attaques
        self.place = pygame.image.load(place).convert_alpha()
        self.image = pygame.image.load(image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.place)
        self.changement_pokemon = pygame.image.load(image_changement_path).convert_alpha()
        self.changement_pokemon_mask = pygame.mask.from_surface(self.changement_pokemon)
        self.posX = posX
        self.posY = posY
        
    def capturer(self):
        taux_echec = int((self.pv / self.pvmax) * 100)
        nbr_echec = []
        while len(nbr_echec) < taux_echec:
            nbr = random.randint(1, 100)
            if nbr not in nbr_echec:
                nbr_echec.append(nbr)

        if random.randint(1, 100) not in nbr_echec:
            print('Capturé!')
            return True
        
    def lance_combat(self, joueur):
        offset = (int(481 - joueur.playerX + self.posX), int(480 - joueur.playerY + self.posY))
        result = self.mask.overlap(joueur.carré_white_mask, offset)
        if result:
            pygame.mixer.music.stop()
            combat = Combat(joueur, self)
            combat.combat()

        
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
    
    def deplacer(self, event):
        if event.type == pygame.KEYDOWN:
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

class Obstacle:
    def __init__(self, filename, posX, posY):
        self.filename = filename
        self.mask = pygame.mask.from_surface(pygame.image.load(self.filename).convert_alpha())
        self.x = posX
        self.y = posY
        
    def collision(self, joueur):
        offset = (int(481 - self.x), int(480 - self.y))
        result = self.mask.overlap(joueur.carré_white_mask, offset)
        if result:
            if joueur.playerX_change > 0:
                joueur.playerX_change = 0
                joueur.playerX -= 10
            if joueur.playerX_change < 0:
                joueur.playerX_change = 0
                joueur.playerX += 10
            if joueur.playerY_change > 0:
                joueur.playerY_change = 0
                joueur.playerY -= 10
            if joueur.playerY_change < 0:
                joueur.playerY_change = 0
                joueur.playerY += 10
        else:
            pass
        
class PNJCombat:
    def __init__(self, name, equipe, mort, argent, filename, posX, posY):
        #Joueur.__init__(self, name, equipe, mort, argent, filename, playerX, playerY)
        self.name = name
        self.equipe = equipe
        self.mort = mort
        self.argent = argent
        self.filename = filename
        self.posX = posX
        self.posY = posY
        self.image = pygame.image.load(self.filename)
        self.mask = pygame.mask.from_surface(self.image)

    def lance_combat(self, joueur):
        offset = (int(481 - joueur.playerX + self.posX), int(480 - joueur.playerY + self.posY))
        result = self.mask.overlap(joueur.carré_white_mask, offset)
        if result:
            pygame.mixer.music.stop()
            combat = Combat(joueur, self)
            combat.combat()



class Combat:
    def __init__(self, joueur, adversaire):
        self.joueur = joueur
        self.adversaire = adversaire
        self.etat = True
        self.pokemon_joueur = self.joueur.equipe[0]
        if isinstance(self.adversaire, PNJCombat):
            self.pokemon_adverse = self.adversaire.equipe[0]
        else:
            self.pokemon_adverse = self.adversaire
    def combat(self):
        pygame.mixer.music.load('sound/combat_music.wav')
        pygame.mixer.music.play(-1)
        
        combat_template = pygame.image.load('Combat pokemon/Combat_template.png').convert_alpha()
        
        combat_attaque = pygame.image.load('Combat pokemon/Combat_mask(attaque).png').convert_alpha()
        combat_attaque_rect = combat_attaque.get_rect()
        combat_attaque_mask = pygame.mask.from_surface(combat_attaque)

        combat_bag = pygame.image.load('Combat pokemon/Combat_mask(bag).png').convert_alpha()
        combat_bag_rect = combat_bag.get_rect()
        combat_bag_mask = pygame.mask.from_surface(combat_bag)
        
        combat_pokemon = pygame.image.load('Combat pokemon/Combat_mask(pokemon).png').convert_alpha()
        combat_pokemon_rect = combat_pokemon.get_rect()
        combat_pokemon_mask = pygame.mask.from_surface(combat_pokemon)
        
        combat_run = pygame.image.load('Combat pokemon/Combat_mask(pokemon).png').convert_alpha()
        combat_run_rect = combat_run.get_rect()
        combat_run_mask = pygame.mask.from_surface(combat_run)
        
        

        DS.blit(combat_attaque, (0, 0))
        DS.blit(combat_bag, (0, 0))
        DS.blit(combat_pokemon, (0, 0))
        DS.blit(combat_run, (0, 0))
        DS.blit(combat_template, (0, 0))
        DS.blit(self.pokemon_adverse.image, (0, 0))
        DS.blit(self.pokemon_joueur.image,(0, 0))
        pygame.display.update()
        while self.etat:
            
            action = ''
            while action == '':
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                         pass
                pos = pygame.mouse.get_pos()
                pos_in_mask = pos[0], pos[1]
                touching1 = combat_attaque_rect.collidepoint(*pos) and combat_attaque_mask.get_at(pos_in_mask)
                touching2 = combat_bag_rect.collidepoint(*pos) and combat_bag_mask.get_at(pos_in_mask)
                touching3 = combat_pokemon_rect.collidepoint(*pos) and combat_pokemon_mask.get_at(pos_in_mask)
                touching4 = combat_run_rect.collidepoint(*pos) and combat_run_mask.get_at(pos_in_mask)
                if touching1 and pygame.mouse.get_pressed()[0]:
                    action = 'attaquer'
                    
                if touching2 and pygame.mouse.get_pressed()[0]:
                    action = 'utiliser objet'
                    
                if touching3 and pygame.mouse.get_pressed()[0]:
                    action = 'changer'
                    
                if touching4 and pygame.mouse.get_pressed()[0]:
                    action = 'run'

            #en fonction d'ou on appuie, l'action change
            if action == 'attaquer':
                
                combat_menu_attaques = pygame.image.load('Combat pokemon/Combat_attaques_bag.png').convert_alpha()
                DS.blit(combat_menu_attaques, (0, 0))
                attaque_pos = [(159, 562), (505, 562), (159, 733), (506, 734)]  
                
                attaque0 = self.pokemon_joueur.attaques[0].image
                attaque0_rect = self.pokemon_joueur.attaques[0].image.get_rect()
                attaque0_mask = pygame.mask.from_surface(self.pokemon_joueur.attaques[0].image)
                attaque_1 = pygame.image.load('Combat pokemon/attaques/attaque1.png').convert_alpha()
                attaque_1_mask = pygame.mask.from_surface(attaque_1)
                attaque_1_rect = attaque_1.get_rect()
                
#                 **********************************************************************************************
                
                attaque1 = self.pokemon_joueur.attaques[1].image
                attaque1_rect = self.pokemon_joueur.attaques[1].image.get_rect()
                attaque1_mask = pygame.mask.from_surface(self.pokemon_joueur.attaques[1].image)
                attaque_2 = pygame.image.load('Combat pokemon/attaques/attaque2.png').convert_alpha()
                attaque_2_mask = pygame.mask.from_surface(attaque_2)
                attaque_2_rect = attaque_2.get_rect()
                
#                 **********************************************************************************************

                attaque2 = self.pokemon_joueur.attaques[2].image
                attaque2_rect = self.pokemon_joueur.attaques[2].image.get_rect()
                attaque2_mask = pygame.mask.from_surface(self.pokemon_joueur.attaques[2].image)
                attaque_3 = pygame.image.load('Combat pokemon/attaques/attaque3.png').convert_alpha()
                attaque_3_mask = pygame.mask.from_surface(attaque_3)
                attaque_3_rect = attaque_3.get_rect()
                
#                 ***********************************************************************************************
                
                attaque3 = self.pokemon_joueur.attaques[3].image
                attaque3_rect = self.pokemon_joueur.attaques[3].image.get_rect()
                attaque3_mask = pygame.mask.from_surface(self.pokemon_joueur.attaques[3].image)
                attaque_4 = pygame.image.load('Combat pokemon/attaques/attaque4.png').convert_alpha()
                attaque_4_mask = pygame.mask.from_surface(attaque_4)
                attaque_4_rect = attaque_4.get_rect()
                
#                 ************************************************************************************************
                DS.blit(attaque_1, (0, 0))
                DS.blit(attaque_2, (0, 0))
                DS.blit(attaque_3, (0, 0))
                DS.blit(attaque_4, (0, 0))
                
                DS.blit(attaque0, attaque_pos[0])
                DS.blit(attaque1, attaque_pos[1])
                DS.blit(attaque2, attaque_pos[2])
                DS.blit(attaque3, attaque_pos[3])

                pygame.display.update()
                
                
                
                wait = True
                while wait:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEMOTION:
                             pass
                    pos = pygame.mouse.get_pos()
                    touching5 = attaque_1_rect.collidepoint(*pos) and attaque_1_mask.get_at(pos_in_mask)
                    touching6 = attaque_2_rect.collidepoint(*pos) and attaque_2_mask.get_at(pos_in_mask)
                    touching7 = attaque_3_rect.collidepoint(*pos) and attaque_3_mask.get_at(pos_in_mask)
                    touching8 = attaque_4_rect.collidepoint(*pos) and attaque_4_mask.get_at(pos_in_mask)

                    if touching5 and pygame.mouse.get_pressed()[0]:
                        attaque_choisie = 0
                        wait = False
                    if touching6 and pygame.mouse.get_pressed()[0]:
                        attaque_choisie = 1
                        wait = False
                    if touching7 and pygame.mouse.get_pressed()[0]:
                        attaque_choisie = 2
                        wait = False
                    if touching8 and pygame.mouse.get_pressed()[0]:
                        attaque_choisie = 3
                        wait = False
                #attaque choisie = en fonction de sur quelle attaque on clique
                self.pokemon_joueur.attaques[attaque_choisie].attaquer(self.pokemon_adverse)
                
            if action == 'utiliser objet':
                combat_menu_objets = pygame.image.load('Combat pokemon/Combat_attaques_bag.png').convert_alpha()
                DS.blit(combat_menu_objets, (0, 0))
                
                combat_pokeball = pygame.image.load('Combat pokemon/bag/bag_pokeball.png').convert_alpha()
                combat_pokeball_mask = pygame.mask.from_surface(combat_pokeball)
                combat_pokeball_rect = combat_pokeball.get_rect()
                DS.blit(combat_pokeball, (0, 0))
                
                combat_potion = pygame.image.load('Combat pokemon/bag/bag_potion.png').convert_alpha()
                combat_potion_mask = pygame.mask.from_surface(combat_potion)
                combat_potion_rect = combat_potion.get_rect()
                DS.blit(combat_potion, (0, 0))
                pygame.display.update()
                
                
                objet = ''
                
                wait = True
                while wait:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEMOTION:
                            pass
                    
                    touching9 = combat_pokeball_rect.collidepoint(*pos) and combat_pokeball_mask.get_at(pos_in_mask)
                    touching10 = combat_potion_rect.collidepoint(*pos) and combat_potion_mask.get_at(pos_in_mask)
                    if touching9 and pygame.mouse.get_pressed()[0]:
                        objet = Item('pokeball', 'capture')
                        wait = False
                    
                    if touching10 and pygame.mouse.get_pressed()[0]:
                        objet = Item('potion', 'soin')
                        wait = False
                #objet en fonction de sur lequel on clique

                
                if objet.utilite == 'capture' and isinstance(self.adversaire, Pokemon):
                    if objet.utilisation(self.pokemon_adverse):
                        self.joueur.equipe.append(self.pokemon_adverse)
                        self.pokemon_adverse.pv = 0
                        
                if objet.utilite == 'soin':
                    self.pokemon_joueur.pv = self.pokemon_joueur.pvmax
            
            if action == 'changer':
                combat_menu_pokemon = pygame.image.load('Combat pokemon/Combat_attaques_bag.png').convert_alpha()
                DS.blit(combat_menu_pokemon, (0, 0))
                pokemon_pos = [(159, 562), (505, 562), (159, 733), (506, 734)]
                i = 0
                for pokemon in self.joueur.equipe:
                    DS.blit(attaque.image, pokemon_pos[i])
                    i+=1
                
                offset11 = (int(mx - 159), int(my - 562))
                result11 = self.joueur.equipe[0].mask_image.overlap(combat_souris_mask, offset11)
                
                offset12 = (int(mx - 505), int(my - 562))
                result12 = self.joueur.equipe[1].mask_image.overlap(combat_souris_mask, offset12)
                
                offset13 = (int(mx - 159), int(my - 733))
                result13 = self.joueur.equipe[2].mask_image.overlap(combat_souris_mask, offset13)
                
                offset14 = (int(mx - 506), int(my - 734))
                result14 = self.joueur.equipe[3].mask_image.overlap(combat_souris_mask, offset14)
                
                if result11 and pygame.mouse.get_pressed()[0]:
                    pokemon_choisi = 0
                
                if result12 and pygame.mouse.get_pressed()[0]:
                    pokemon_choisi = 1
                    
                if result13 and pygame.mouse.get_pressed()[0]:
                    pokemon_choisi = 2
                    
                if result14 and pygame.mouse.get_pressed()[0]:
                    pokemon_choisi = 3
                    
                self.changement(pokemon_choisi)
            
            if isinstance(self.adversaire, PNJCombat) and len(adversaire.equipe) == 0:
                vainqueur = self.joueur
                self.etat = False
            
            elif isinstance(self.adversaire, Pokemon) and self.pokemon_adverse.pv <= 0:
                vainqueur = self.joueur
                self.etat = False
                
            self.pokemon_adverse.attaques[0].attaquer(self.pokemon_joueur)
            if self.pokemon_joueur.pv <= 0 and len(self.joueur.equipe) > 0:
                self.joueur.mort.append(self.pokemon_joueur)
                self.joueur.equipe.remove(self.pokemon_joueur)
                combat_menu_pokemon = pygame.image.load('Combat pokemon/Combat_attaques_bag.png').convert_alpha()
                DS.blit(combat_menu_pokemon, (0, 0))
                pokemon_pos = [(159, 562), (505, 562), (159, 733), (506, 734)]
                i = 0
                for pokemon in self.joueur.equipe:
                    DS.blit(attaque.image, pokemon_pos[i])
                    i+=1
                
            if len(self.joueur.equipe) == 0:
                self.etat = False
                vainqueur = self.adversaire
            
        if vainqueur == self.joueur:
            for pokemon in self.joueur.equipe:
                pokemon.xp += 10
            if isinstance(self.adversaire, PNJCombat):
                self.joueur.argent += self.adversaire.argent
        else:
            self.joueur.argent *= (19/20)
        
        pygame.mixer.music.stop()
        
    def changement(self, nbr):
        self.pokemon_joueur = self.joueur.equipe[nbr]
        
class Item:
    def __init__(self, nom, utilite):
        self.nom = nom
        self.utilite = utilite
        
    def utilisation(self, beneficiaire):
        if self.utilite == 'soin':
            beneficiaire.pv = beneficiaire.pvmax
            
        if self.utilite == 'capture':
            beneficiaire.capturer()
        
