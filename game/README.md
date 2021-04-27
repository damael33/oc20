# OC 2020 : Création du Jeu Pokémon

## Introduction

Le but de ce travail est de créer un jeu en python, en utilisant la bibliothèque ``pygame``, à l'aide des notions apprises en cours.


## Présentation de notre jeu

### Type de jeu
Notre jeu est un remake de **Pokémon** dans lequel le but est de constituer l'équipe la plus puissante possible afin de battre des dresseurs de pokémon de plus en plus puissants. Pour ce faire des pokémons pourront être capturés avec des capsules appelées *"pokéballs"*.


### Comment jouer à ce jeu
Il s'agit d'un jeu comportant deux phases qui sont respectivement la phase combat et la phase de déplacement dans le monde des pokémons.

La phase de combat :
- quatre attaques disponibles afin de faire des dégats au pokémon adverse
- possibilité de fuir un combat lorsque le combat est engagé par un pokemon sauvage. Ne fonctionne pas lors d'un combat avec un dresseur adverse. 
- possibilité de capturer un pokémon sauvage
- changer de pokémon durant le combat
- soigner à l'aide de potions les pokémons

La phase de déplacement :
- le personnage sera déplaçable avec avec les flèches
- interaction avec des élements de la map en appuyant sur la touche ``a``.
- pour rencontrer des pokémons sauvages, le joueur devra se déplacer dans des fourrés

Il faudra néanmoins faire attention aux autres dresseurs qui vous barreront la route et qui voudront vous combattre !

![Capture d’écran 2021-04-22 à 13 42 05](https://user-images.githubusercontent.com/77661971/115709310-5f463280-a371-11eb-8dcb-68ebccc7da8f.png)

### Stucture interne de notre jeu
Notre jeu est principalement basé sur l'usage de classes. En effet c'est la méthode la plus simple pour créer rapidement et facilement un grand nombre de pokemons, de types , d'attaques et plus encore.

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

Voici notamment un exemple de notre classe ``attaque``. 


### Classes contenues dans notre jeu

Comme cité auparavant notre jeu contient de nombreuses classes que vous pouvez voir ci-dessous :

![diagramclass](https://github.com/damael33/oc20/blob/main/game/img/Diagram%20Class%20(1).png)

Voici quelques commentaires concernant ce diagramme :
- tous les attributs concernants le sprite du joueur sont sous entendues dans la variable ``sprite variables``
- les paramètres des méthodes ne sont pas précisés, car parfois nombreux. Seul le ``self`` apparait. Si non, il s'agit d'une *staticmethod*

Bien entendu ces classes ainsi que leurs attributs et méthodes ne sont pas définitives : comme un grand nombre d'idées continue d'affluer, certaines classes pourront disparaître ou être créées, d'autres se compléter ou deux classes pourront converger pour qu'une classe hérite d'une autre. Nous ne somme qu'au début du projet, qui va sûrement encore évoluer.
