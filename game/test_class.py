import random

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
    def __init__(self, name, equipe, mort, argent, sac):
        self.name = name
        self.equipe = []
        self.ko = []
        self.argent = argent
        self.sac = {}
        
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